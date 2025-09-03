# -*- coding: utf-8 -*-
"""
****************************************PHYSICS LAB -DESKTOP VERSION-
Created on Mon Jul 15 14:59:40 2024

To use pyqtgraph: promote QWidget to pyqtgraph.h as PlotWidget in Designer

Status: In progess: ok.

Warning: when running in windows 11 computers, the plot does not work.
#The problem was related to the PySide6 version. It was solved after downgrading the PySide6==6.9.1 to PySide6==6.5.2:
pip install "PySide6==6.5.2"
It also worked downgrading to: pip install "PySide==6.8.0.2" in Python 3.13.5 (windows 11)

Finished and debugged.

#*************note
This *_temp.py file is adpated to create the correct paths for the app building process.
It is called by the .spec file. This is not loaded to github.
Icons for buttons were created with: https://www.svgrepo.com/

@author: AIO520 Ci5
"""

import sys, os
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon
import threading
import pyqtgraph as pg
import serial
import serial.tools.list_ports
import time
import numpy as np

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller.
        Works with both files and folders.
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def load_stylesheet(filename):
    with open(filename, "r") as f:
        return f.read()

icons_dir = resource_path("icons")

ui_file = resource_path("PHYSICSLAB_GUI_V1_0.ui")
uiclass, baseclass = pg.Qt.loadUiType(ui_file)

serial_port = serial.Serial() #Create an instance of the serial port
serial_port.baudrate = 115200
vref=3.28 #Reference voltage for the ADC. For a next version we can use a calibrate buttom to enter the multimeter value.
analog_data=[0.0]*4 #List to store the received analog data
analog_offsets=[0.0]*4 #List to store the offsets to be substracted from analog_data
time_values=[] #list with the values of time for the photogate function.
time_units_conv=1000000 #conversion factor to convert to seconds the time values (/1000 if data is in ms)
time_units_str=" ms"
x=[] #Time list when the photogate operations tn-t_(n-1) or tn-t_(n-2) are selected
y=[] #Lists for the x,y plot


connected_flag=0 #To know whether if the serial port is conected or not.

class Communicate(QObject): #Signal to allow threading function to communicate with the main GUI
    data_received_signal = Signal(str)

def serial_data_thread(signal): #Separate thread that emits the serial data (signal) when there is new data in the serial port (threading eliminates the problem of freezing GUIs)
    global connected_flag
    while threading.current_thread().is_alive():
        #signal.data_received_signal.emit("Hola") #For debugging
        time.sleep(0.01) #Neccesary to not freeze the plot controls
        if (serial_port.is_open and connected_flag==1): #If port is open and connection is active
            if(serial_port.in_waiting>0): #If data has arrived
                data = serial_port.readline().decode('utf-8').strip()
                signal.data_received_signal.emit(data)

class MainWindow(uiclass, baseclass):
    analog_active_flag = 0 #Flag that is set while the analog sensors function is active
    spi_active_flag = 0 #Flag that is set while the spi sensors function is active
    photo_active_flag = 0 #Flag that is set while the photogate sensors functions are active
    on_off_controller_active_flag = 0 #Flag that is set while the ON/OFF controller of port D6 is active

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_thread()
        self.connectWidgets()
        self.refresh_com_ports()
        self.confplot("w")

        self.pixmap_oscuridad = QPixmap(os.path.join(icons_dir, "tiempo_oscuridad.bmp"))
        self.pixmap_claro_oscuro = QPixmap(os.path.join(icons_dir, "tiempos_claro_oscuro.bmp"))
        self.pixmap_claro_oscuro_claro = QPixmap(os.path.join(icons_dir, "tiempos_claro_oscuro_claro.bmp"))
        self.pixmap_doble_photogate = QPixmap(os.path.join(icons_dir, "tiempos_doble_compuerta.bmp"))
        
        self.label_photo_options.setPixmap(self.pixmap_oscuridad)
        self.pixmap_logoudea = QPixmap(os.path.join(icons_dir, "udea_logo.png"))
        self.udea_logo_label.setPixmap(self.pixmap_logoudea)
        self.pixmap_logogicm = QPixmap(os.path.join(icons_dir, "gicm_logo_small.png"))
        self.gicm_logolabel.setPixmap(self.pixmap_logogicm)
        self.pixmap_qrcode = QPixmap(os.path.join(icons_dir, "QR-code.png"))
        self.label_qr.setPixmap(self.pixmap_qrcode) 
        self.pixmap_board_diagram  =  QPixmap(os.path.join(icons_dir, "board_drawing.png"))
        self.label_diagram.setPixmap(self.pixmap_board_diagram)

        self.analog_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
        self.spi_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
        self.photo_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
        self.port5_apply_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
        self.port6_apply_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
        self.clear_plot_btn.setIcon(QIcon(os.path.join(icons_dir, "edit-delete.svg")))
        self.save_plot_btn.setIcon(QIcon(os.path.join(icons_dir, "document-save.svg")))
        self.clear_plotbar_btn.setIcon(QIcon(os.path.join(icons_dir, "edit-delete.svg")))
        self.save_plotbar_btn.setIcon(QIcon(os.path.join(icons_dir, "document-save.svg")))
        self.clear_console_btn.setIcon(QIcon(os.path.join(icons_dir, "edit-delete.svg")))
        self.refresh_ports_btn.setIcon(QIcon(os.path.join(icons_dir, "view-refresh.svg")))
        
    ######################### Main funcions
    def start_thread(self):
        self.comm = Communicate()
        self.comm.data_received_signal.connect(self.process_message) #When the signal data_receive_signal is received, the function (slot) process_message is called.
        self.thread = threading.Thread(target=serial_data_thread, args=(self.comm,))
        self.thread.daemon = True  # Allows the thread to be killed when the main program exits
        self.thread.start()
    
    def connectWidgets(self): #Function to connect widget events to functions
        self.connect_btn.clicked.connect(self.con_discon_serial)
        self.refresh_ports_btn.clicked.connect(self.refresh_com_ports)
        self.analog_start_btn.clicked.connect(self.analog_start)
        self.analog_start_btn.setEnabled(False)
        self.spi_start_btn.clicked.connect(self.spi_start)
        self.spi_start_btn.setEnabled(False)
        self.photo_start_btn.clicked.connect(self.photo_start)
        self.photo_start_btn.setEnabled(False)
        self.port5_apply_btn.clicked.connect(self.port5_apply)
        self.port5_apply_btn.setEnabled(False)
        self.port6_apply_btn.clicked.connect(self.port6_apply)
        self.port6_apply_btn.setEnabled(False)
        self.save_plot_btn.clicked.connect(self.save_plot_data)
        self.save_plotbar_btn.clicked.connect(self.save_plotbar_data)
        self.auto_bins.clicked.connect(self.show_nbins)
        self.clear_plot_btn.clicked.connect(self.clear_plot_data)
        self.clear_plotbar_btn.clicked.connect(self.clear_plotbar_data)
        self.clear_console_btn.clicked.connect(self.clear_console)
        self.zero_A0.clicked.connect(self.zeroa0)
        self.zero_A1.clicked.connect(self.zeroa1)
        self.zero_A2.clicked.connect(self.zeroa2)
        self.zero_A3.clicked.connect(self.zeroa3)
        self.photo_option.currentIndexChanged.connect(self.photo_opt_changed)
        self.port5_option.currentIndexChanged.connect(self.port5_opt_changed)
        self.port6_option.currentIndexChanged.connect(self.port6_opt_changed)
        
    def refresh_com_ports(self):
        self.selectPort.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.selectPort.addItem(port.device)

    def confplot(self, bgcolor):
        self.graphwidget.setBackground(bgcolor)
        styles = {"color": "black", "font-size": "14px"}
        self.graphwidget.setLabel("left", "Valor", **styles)
        self.graphwidget.setLabel("bottom", "Índice", **styles)
        axispen = pg.mkPen(color=(0,0,0), width=1)
        self.graphwidget.plotItem.getAxis('left').setPen(axispen)
        self.graphwidget.plotItem.getAxis('bottom').setPen(axispen)
        pen = pg.mkPen(color=(255, 0, 0)) #define the line color of the plot
        self.plot_data=self.graphwidget.plot([], [], pen=pen, symbol='o', symbolPen ='r', symbolSize = 4)
        #Histogram plot:
        self.histowidget.setBackground(bgcolor)
        self.histowidget.setLabel("left", "Frecuencia", **styles)
        self.histowidget.setLabel("bottom", "Valor", **styles)
        self.histowidget.plotItem.getAxis('left').setPen(axispen)
        self.histowidget.plotItem.getAxis('bottom').setPen(axispen)
        self.plot_bar_data = pg.BarGraphItem(x=[], height=[], width=1.0, brush='skyblue')
        self.histowidget.addItem(self.plot_bar_data)

    ######################## Functions deployed by pressing buttons
    def con_discon_serial(self): #Connect or disconnect serial
        global connected_flag
        selected_port = self.selectPort.currentText()
        number_ports = self.selectPort.count() #Count the number of items (ports) in the Qcombobox
        if serial_port.is_open: #If port is open
            connected_flag = 0
            serial_port.close()
            if(not serial_port.is_open): #Check if really closed
                self.connect_btn.setText("CONECTAR")
                self.StatusText.setText("Desconectado.")
                self.analog_start_btn.setEnabled(False)
                self.spi_start_btn.setEnabled(False)
                self.photo_start_btn.setEnabled(False)         
        else: #If port is not opened
            if(number_ports > 0): #Check first if at least there is one port in the list
                serial_port.port=selected_port
                serial_port.open()
                if(serial_port.is_open): #Check if really opened
                    self.connect_btn.setText("DESCONECTAR")
                    self.StatusText.setText("Conectado a "+selected_port+". Esperando inicialización del sistema...")
                    self.label_connection.setText("Inicializando...")
                    connected_flag = 1
                else:
                    self.StatusText.setText("Fallo en la conexión a "+selected_port)
            else:
                self.StatusText.setText("No se encontraron puertos. Revise las conexiones e intenrte de nuevo")

    def analog_start(self): #Start analog sensors function

        if serial_port.is_open: #If port is open
            analog_time_selected_index=self.analog_time_select.currentIndex()
            analog_time_option=''
            if(analog_time_selected_index==0):
                analog_time_option='a'
            elif(analog_time_selected_index==1):
                analog_time_option='b'
            elif(analog_time_selected_index==2):
                analog_time_option='c'
            elif(analog_time_selected_index==3):
                analog_time_option='d'
            
            serial_port.write(('1'+analog_time_option+'\n').encode('utf-8')) #Command to start reading of analog sensors with the give time delay option

    def spi_start(self): #Start spi sensors function

        if serial_port.is_open: #If port is open
            spi_time_selected_index=self.spi_time_select.currentIndex()
            spi_time_option=''
            if(spi_time_selected_index==0):
                spi_time_option='a'
            elif(spi_time_selected_index==1):
                spi_time_option='b'
            elif(spi_time_selected_index==2):
                spi_time_option='c'
            elif(spi_time_selected_index==3):
                spi_time_option='d'
            
            serial_port.write(('2'+spi_time_option+'\n').encode('utf-8')) #Command to start reading of spi sensors with the give time delay option. For now, this will just take the fifth column of data. Later the Arduino program will be modified with another menu entry dedicated to spi sensors            
    
    def photo_start(self): #Start photogate measurements

        if serial_port.is_open: #If port is open
            photo_option_selected_index=self.photo_option.currentIndex()
            serial_port.write((str(3+photo_option_selected_index)+'\n').encode('utf-8')) #Command to start selected photogate

    def port5_apply(self): #Apply port 5 state

        if serial_port.is_open: #If port is open
            port5_option_selected_index=self.port5_option.currentIndex()
            port5_option=''
            if(port5_option_selected_index==0):
                port5_option='a'
            #elif for future option
            serial_port.write(('7'+port5_option+'\n'+self.port5_value.text()).encode('utf-8')) #Command to start port5 function


    def port6_apply(self): #Apply port 6 state

        if serial_port.is_open: #If port is open
            port6_option_selected_index=self.port6_option.currentIndex()
            port6_option=''
            if(port6_option_selected_index==0):
                port6_option='b'
            elif(port6_option_selected_index==1):
                port6_option='c'
            elif(port6_option_selected_index==2):
                port6_option='d'

            if self.on_off_controller_active_flag == 0:
                serial_port.write(('7'+port6_option+'\n'+self.port6_value.text()).encode('utf-8')) #Command to start port5 function
            elif self.on_off_controller_active_flag == 1:
                serial_port.write('.'.encode('utf-8')) #Send any character to end the function

    def photo_opt_changed(self): #Function to change the illustration of the selected photogate function
        if(self.photo_option.currentIndex()==0):
            self.label_photo_options.setPixmap(self.pixmap_oscuridad)
            self.label_portD7.setText("Puerto D8")
        elif(self.photo_option.currentIndex()==1):
            self.label_photo_options.setPixmap(self.pixmap_claro_oscuro)
            self.label_portD7.setText("Puerto D8")
        elif(self.photo_option.currentIndex()==2):
            self.label_photo_options.setPixmap(self.pixmap_claro_oscuro_claro)
            self.label_portD7.setText("Puerto D8")
        elif(self.photo_option.currentIndex()==3):
            self.label_photo_options.setPixmap(self.pixmap_doble_photogate)
            self.label_portD7.setText("Puertos D8 y D38")

    def port5_opt_changed(self): #Function to change the label of the value to be inserted by the user
        if(self.port5_option.currentIndex()==0):
            self.label_value_port5.setText('Duty Cycle (0-255)')
    
    def port6_opt_changed(self): #Function to change the label of the value to be inserted by the user
        if(self.port6_option.currentIndex()==0):
            self.label_value_port6.setText('Frecuencia (Hz)')
        elif(self.port6_option.currentIndex()==1):
            self.label_value_port6.setText('Umbral (1 si <)')
        elif(self.port6_option.currentIndex()==2):
            self.label_value_port6.setText('Estado (0 ó 1) ')

    def save_plot_data(self):
        # Open file dialog to select file name and location
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar datos como:", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=options)
        
        if file_name:
            # Query data from graphwidget plot
            x, y = self.plot_data.getData()
            ylabel = self.graphwidget.plotItem.getAxis('left').labelText
            xlabel = self.graphwidget.plotItem.getAxis('bottom').labelText
            header=""
            current_tab=self.tabWidget.currentIndex()
            current_photo_option=self.photo_option.currentText()
            if(current_tab==0):
                header="Tiempo entre datos: "+self.analog_time_select.currentText()+"\n\n"
            elif(current_tab==1):
                header="Tiempo entre datos: "+self.spi_time_select.currentText()+"\n\n"
            elif(current_tab==2):
                if(current_photo_option=="Tiempo de oscuridad"):
                    header="Tiempo de oscuridad (us)."+"\n\n"
                elif(current_photo_option=="Tiempo claro->oscuro"):
                    header="Tiempos de transicion claro -> oscuro (ms)."+"\n\n"
                elif(current_photo_option=="Tiempo claro<->oscuro"):
                    header="Tiempos de transicion claro <-> oscuro (ms)"+"\n\n"
                elif(current_photo_option=="Tiempo doble fotocompuerta"):
                    header="Tiempo entre sensores reflectivos (ms)."+"\n\n"
            # Save data to file
            with open(file_name, 'w') as file:
                file.write("")
                file.write(header)
                file.write(xlabel+"\t"+ylabel+"\n")
                for x_val, y_val in zip(x, y):
                    file.write("{:.3f}".format(x_val)+"\t"+"{:.3f}".format(y_val)+"\n")
            self.StatusText.append("Archivo de datos guardado existosamente")

    def save_plotbar_data(self):
        # Open file dialog to select file name and location
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar histograma como:", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=options)
        
        if file_name:
            # Query data from histowidget plot
            x, y = self.plot_bar_data.getData()
            ylabel = "Frecuencia"
            xlabel = self.histowidget.plotItem.getAxis('bottom').labelText
            header=""
            current_tab=self.tabWidget.currentIndex()
            current_photo_option=self.photo_option.currentText()
            if(current_tab==0):
                header="Tiempo entre datos: "+self.analog_time_select.currentText()+"\n\n"
            elif(current_tab==1):
                header="Tiempo entre datos: "+self.spi_time_select.currentText()+"\n\n"
            elif(current_tab==2):
                if(current_photo_option=="Tiempo de oscuridad"):
                    header="Tiempo de oscuridad (us).""\n\n"
                elif(current_photo_option=="Tiempo claro->oscuro"):
                    header="Tiempos de transicion claro -> oscuro (ms).""\n\n"
                elif(current_photo_option=="Tiempo claro<->oscuro"):
                    header="Tiempos de transicion claro <-> oscuro (ms)""\n\n"
                elif(current_photo_option=="Tiempo doble fotocompuerta"):
                    header="Tiempo entre sensores reflectivos (ms).""\n\n"
            # Save data to file
            with open(file_name, 'w') as file:
                file.write("")
                file.write(header)
                file.write(xlabel+"\t"+ylabel+"\n")
                for x_val, y_val in zip(x, y):
                    file.write(f"{x_val:.3f}\t{y_val}\n")
            self.StatusText.append("Histograma guardado existosamente")

    def show_nbins(self):
        if self.auto_bins.isChecked():
            self.number_bins.setEnabled(False)
        else:
            self.number_bins.setEnabled(True)

    def clear_plot_data(self):
        global y
        global x
        x=[]
        y=[]
        self.plot(np.arange(len(y)),np.array(y))

    def clear_plotbar_data(self):
        global y
        global x
        x=[]
        y=[]
        self.plotbar([],[],1)

    def clear_console(self):
        self.StatusText.clear()

    def zeroa0(self):
        global analog_data
        global analog_offsets
        analog_offsets[0]=analog_data[0]
    
    def zeroa1(self):
        global analog_data
        global analog_offsets
        analog_offsets[1]=analog_data[1]
    
    def zeroa2(self):
        global analog_data
        global analog_offsets
        analog_offsets[2]=analog_data[2]
    
    def zeroa3(self):
        global analog_data
        global analog_offsets
        analog_offsets[3]=analog_data[3]
    ########################## Functions for plotting and analysis
    def plot(self, xdata, ydata):
        self.plot_data.setData(xdata, ydata)

    def plotbar(self, xdata, ydata, width):
        self.plot_bar_data.setOpts(x=xdata, height=ydata, width=width)

    def units_converter(self,index,adc_value,adc_offset): #It takes the integer ADC value and return the values with the units given by index
        global vref #Check equations to use vref in all of them
        converted_value=0
        converted_value_str=""
        ylabel=""
        A0_index=self.A0_sensors.currentIndex()
        if(index==0):  #Voltage (V)
            converted_value=(adc_value-adc_offset)*vref/1023.0
            converted_value_str="{:.3f}".format(converted_value)+" V"
            ylabel="Voltaje (V)"
        elif(index==1): #Lux (lx) (AMS104)
            converted_value=(adc_value-adc_offset)/1457.0
            converted_value_str="{:.3f}".format(converted_value)+" lx"
            ylabel="Iluminancia (lx)"
        elif(index==2): #Magnetic field (Gauss) (A1302)
            converted_value=1000*(((adc_value-adc_offset)/403.0)-(25.0/13.0))
            converted_value_str="{:.3f}".format(converted_value)+" Gauss"
            ylabel="Campo magnético (Gauss)"
        elif(index==3): #Relative humidity (%) (HIH4000)
            converted_value=(2000.0/31.0)*(((adc_value-adc_offset)/310.0)-(2.0/5.0))
            converted_value_str="{:.3f}".format(converted_value)+" %"
            ylabel="% Humedad relativa"
        elif(index==4): #Pressure (kPa) (MPXV5004)
            converted_value=1000.0*(((adc_value-adc_offset)/155.0)-1.0)
            converted_value_str="{:.3f}".format(converted_value)+" kPa"
            ylabel="Presión (kPa)"
        elif(index==5): #Pressure (kPa) (MPXV5100)
            converted_value=1000.0*(40.0*((adc_value-adc_offset)/279.0)-(40.0/9.0))
            converted_value_str="{:.3f}".format(converted_value)+" kPa"
            ylabel="Presión (kPa)"
        else: #Raw adc value (10 bits)
            converted_value=adc_value-adc_offset
            converted_value_str="{:.0f}".format(converted_value)+"  "
            ylabel="valor ADC (10bits)"

        return converted_value_str, ylabel

    def process_message(self, message):
        global analog_offsets
        global analog_data
        global time_values
        global time_units_conv
        global time_units_str
        self.StatusText.append(message)
        ##print(repr(message))
        #Messages that corresponds to initialization or ending
        if message == "7 : Salidas digitales en los pines 5 y 6.":
            self.analog_start_btn.setText("INICIAR")
            self.analog_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.spi_start_btn.setText("INICIAR")
            self.spi_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.photo_start_btn.setText("INICIAR")
            self.photo_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.port5_apply_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.port6_apply_btn.setText("APLICAR")
            self.port5_apply_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.analog_start_btn.setEnabled(True)
            self.spi_start_btn.setEnabled(True)
            self.photo_start_btn.setEnabled(True)
            self.port5_apply_btn.setEnabled(True)
            self.port6_apply_btn.setEnabled(True)
            self.label_connection.setText("")
            return
        if message == "A0\t A1\t A2\t A3":
            self.analog_active_flag=1
            self.analog_start_btn.setText("PARAR")
            self.analog_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-stop.svg")))
            items = ["A0", "A1", "A2", "A3"]
            self.Yaxis_plot.addItems(items)
            analog_offsets=[0.0]*4
            self.spi_start_btn.setEnabled(False)
            self.photo_start_btn.setEnabled(False)
            self.port5_apply_btn.setEnabled(False)
            self.port6_apply_btn.setEnabled(False)
            self.connect_btn.setEnabled(False) #To prevent stopping the data transfer when pressing the disconnect button

            return
        if message == "Temperatura":
            self.spi_active_flag=1
            self.spi_start_btn.setText("PARAR")
            self.spi_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-stop.svg")))
            items = ["Temp."]
            self.Yaxis_plot.addItems(items)
            self.analog_start_btn.setEnabled(False)
            self.photo_start_btn.setEnabled(False)
            self.port5_apply_btn.setEnabled(False)
            self.port6_apply_btn.setEnabled(False)
            self.connect_btn.setEnabled(False) #To prevent stopping the data transfer when pressing the disconnect button

            return
        if message == "Tiempo de oscuridad (us)." or message == "Tiempos de transicion claro -> oscuro (ms)." or message == "Tiempos de transicion claro <-> oscuro (ms)" or message == "Tiempo entre sensores reflectivos (ms).":
            self.photo_active_flag=1
            self.photo_start_btn.setText("PARAR")
            self.photo_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-stop.svg")))
            items = ["Valor", "Operación", "Velocidad"]
            self.Yaxis_plot.addItems(items)
            self.analog_start_btn.setEnabled(False)
            self.spi_start_btn.setEnabled(False)
            self.photo_option.setEnabled(False)
            self.port5_apply_btn.setEnabled(False)
            self.port6_apply_btn.setEnabled(False)
            self.connect_btn.setEnabled(False) #To prevent stopping the data transfer when pressing the disconnect button

            if(message == "Tiempo de oscuridad (us)."):
                time_units_conv=1000000 #Only this option give the time in us
                time_units_str=" us"
            else:
                time_units_conv=1000
                time_units_str=" ms"
            time_values=[]

            return
        
        if message == "Función Iniciada. Presione una tecla para terminar...":
            self.on_off_controller_active_flag=1
            self.port6_apply_btn.setText("PARAR")
            self.port6_apply_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-stop.svg")))
            items= ["A0 (10 bits)"]
            self.Yaxis_plot.addItems(items)
            self.analog_start_btn.setEnabled(False)
            self.spi_start_btn.setEnabled(False)
            self.photo_start_btn.setEnabled(False)
            self.port5_apply_btn.setEnabled(False)
            self.connect_btn.setEnabled(False) #To prevent stopping the data transfer when pressing the disconnect button

            return
        
        if message == "FIN.":
            self.analog_active_flag=0
            self.spi_active_flag=0
            self.photo_active_flag=0
            self.on_off_controller_active_flag=0
            self.analog_start_btn.setText("INICIAR")
            self.analog_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.spi_start_btn.setText("INICIAR")
            self.spi_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.photo_start_btn.setText("INICIAR")
            self.photo_start_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.port6_apply_btn.setText("APLICAR")
            self.port6_apply_btn.setIcon(QIcon(os.path.join(icons_dir, "media-playback-start.svg")))
            self.Yaxis_plot.clear()
            self.connect_btn.setEnabled(True) #To activate again the disconnect function
            self.analog_start_btn.setEnabled(True)
            self.spi_start_btn.setEnabled(True)
            self.photo_start_btn.setEnabled(True)
            self.photo_option.setEnabled(True)
            self.port5_apply_btn.setEnabled(True)
            self.port6_apply_btn.setEnabled(True)
            return
        
        #Messages that are processed depending on the active flag
        if self.analog_active_flag == 1:  #Analog Sensors
            analog_data=list(map(float, message.split('\t')))
            #indicators array are created according to the units_converter function and the analog_data[] array
            indicators = [""]*4 #Analog indicators
            ylabels = [""]*4 # Labels associated with each indicator for plotting purposes
            indicators[0], ylabels[0]=self.units_converter(self.A0_sensors.currentIndex(),analog_data[0],analog_offsets[0])
            indicators[1], ylabels[1]=self.units_converter(self.A1_sensors.currentIndex(),analog_data[1],analog_offsets[1])
            indicators[2], ylabels[2]=self.units_converter(self.A2_sensors.currentIndex(),analog_data[2],analog_offsets[2])
            indicators[3], ylabels[3]=self.units_converter(self.A3_sensors.currentIndex(),analog_data[3],analog_offsets[3])
           
            self.A0_value.setText(indicators[0]) 
            self.A1_value.setText(indicators[1])
            self.A2_value.setText(indicators[2])
            self.A3_value.setText(indicators[3])
            val_to_plot=float(indicators[self.Yaxis_plot.currentIndex()].split(' ')[0]) #Removes the units before converting to float
            ylabel=ylabels[self.Yaxis_plot.currentIndex()]
            y.append(val_to_plot)
            self.plot(np.arange(len(y)),np.array(y))
            self.graphwidget.setLabel("left", ylabel)
            #Generate histogram:
            nbins = 'auto' #Default value for the number of bins
            if(not self.auto_bins.isChecked()):
                try:
                    nbins_user=int(self.number_bins.text())
                    if(nbins_user>0):
                        nbins=nbins_user
                    else:
                        nbins='auto'
                except ValueError:
                    nbins='auto'
            
            y_histo, x_histo=np.histogram(y, bins=nbins) #Generate histogram data
            x_histo_centers = (x_histo[:-1] + x_histo[1:]) / 2
            histo_width = x_histo[1] - x_histo[0]
            
            #Aqui va la grafica del histograma
            self.plotbar(x_histo_centers,y_histo,histo_width)
            self.histowidget.setLabel("bottom", ylabel)
            return
        
        elif self.spi_active_flag == 1: #SPI temperature sensor
            temperature_data=float(message)
            indicator=message+' °C'
           
            self.SPI_sens_value.setText(indicator) 

            val_to_plot=temperature_data
            ylabel="Temperatura (°C)"
            y.append(val_to_plot)
            self.plot(np.arange(len(y)),np.array(y))
            self.graphwidget.setLabel("left", ylabel)
            #Generate histogram:
            nbins = 'auto' #Default value for the number of bins
            if(not self.auto_bins.isChecked()):
                try:
                    nbins_user=int(self.number_bins.text())
                    if(nbins_user>0):
                        nbins=nbins_user
                    else:
                        nbins='auto'
                except ValueError:
                    nbins='auto'
            
            y_histo, x_histo=np.histogram(y, bins=nbins) #Generate histogram data
            x_histo_centers = (x_histo[:-1] + x_histo[1:]) / 2
            histo_width = x_histo[1] - x_histo[0]
            
            #Aqui va la grafica del histograma
            self.plotbar(x_histo_centers,y_histo,histo_width)
            self.histowidget.setLabel("bottom", ylabel)
            self.connect_btn.setEnabled(False) #To prevent stopping the data transfer when pressing the disconnect button
            return

        elif self.photo_active_flag == 1: #Photogate sensor functions
            value=int(message)
            time_values.append(value)
            len_time_values=len(time_values)
            indicator=message+time_units_str
            operation=0
            size=float(self.size_entry.text())
            velocity=0.0
            avrg_time=0.0 #average time
            self.photo_value.setText(indicator)

            operation=self.operation_option.currentIndex()
            xaxis_option=self.Xaxis_checkBox.isChecked()
            if(operation==0): # t_n
                self.operation_result.setText(message+time_units_str)
                operation=value
                if operation>0:
                    velocity=size*time_units_conv/operation
                else:
                    velocity=0
                self.velocity_value.setText("{:.3f}".format(velocity)+" cm/s")
                self.average_time.setText("")
            elif(operation==1): #t_n-t_(n-1)
                if(len_time_values>1):
                    operation=time_values[len_time_values-1]-time_values[len_time_values-2]
                    self.operation_result.setText(str(operation)+time_units_str)
                    if operation>0:
                        velocity=size*time_units_conv/operation
                    else:
                        velocity=0
                    avrg_time=(time_values[len_time_values-1]+time_values[len_time_values-2])/(2*time_units_conv)
                    self.velocity_value.setText("{:.3f}".format(velocity)+" cm/s")
                    self.average_time.setText("{:.3f}".format(avrg_time)+" s")
                else:
                    self.operation_result.setText("")
                    self.velocity_value.setText("")
                    self.average_time.setText("")
            elif(operation==2): #t_n-t_(n-2)
                if(len_time_values>2):
                    operation=time_values[len_time_values-1]-time_values[len_time_values-3]
                    self.operation_result.setText(str(operation)+time_units_str)
                    if operation>0:
                        velocity=size*time_units_conv/operation
                    else:
                        velocity=0
                    avrg_time=(time_values[len_time_values-1]+time_values[len_time_values-3])/(2*time_units_conv)
                    self.velocity_value.setText("{:.3f}".format(velocity)+" cm/s")
                    self.average_time.setText("{:.3f}".format(avrg_time)+" s")
                else:
                    self.operation_result.setText("")
                    self.velocity_value.setText("")
                    self.average_time.setText("")

            #Select the value to plot:
            selected_index=self.Yaxis_plot.currentIndex()
            ylabel=""
            xlabel="Índice"
            if(selected_index==0):
                ylabel="Valor ("+time_units_str+")"
                y.append(value)
            elif(selected_index==1):
                ylabel="Operación ("+time_units_str+")"
                y.append(operation)
            elif(selected_index==2):
                ylabel="Velocidad (cm/s)"
                y.append(velocity)

            if(xaxis_option==True):
                xlabel="Tiempo promedio (s)"
                x.append(avrg_time)
                xsize=len(x)
                y_plot=np.array(y)[-xsize:]
                self.plot(np.array(x),y_plot)
            else:
                xlabel="Índice"
                self.plot(np.arange(len(y)),np.array(y))

            self.graphwidget.setLabel("left", ylabel)
            self.graphwidget.setLabel("bottom", xlabel)
            #Generate histogram:
            nbins = 'auto' #Default value for the number of bins
            if(not self.auto_bins.isChecked()):
                try:
                    nbins_user=int(self.number_bins.text())
                    if(nbins_user>0):
                        nbins=nbins_user
                    else:
                        nbins='auto'
                except ValueError:
                    nbins='auto'
            
            y_histo, x_histo=np.histogram(y, bins=nbins) #Generate histogram data
            x_histo_centers = (x_histo[:-1] + x_histo[1:]) / 2
            histo_width = x_histo[1] - x_histo[0]
            
            #Aqui va la grafica del histograma
            self.plotbar(x_histo_centers,y_histo,histo_width)
            self.histowidget.setLabel("bottom", ylabel)
            self.connect_btn.setEnabled(False) #To prevent stopping the data transfer when pressing the disconnect button
            
            return
        
        elif self.on_off_controller_active_flag == 1: #ON/OFF controller option
            A0_value=int(message)
           
            val_to_plot=A0_value
            ylabel="valor ADC (10bits)"
            y.append(val_to_plot)
            self.plot(np.arange(len(y)),np.array(y))
            self.graphwidget.setLabel("left", ylabel)
            #Generate histogram:
            nbins = 'auto' #Default value for the number of bins
            if(not self.auto_bins.isChecked()):
                try:
                    nbins_user=int(self.number_bins.text())
                    if(nbins_user>0):
                        nbins=nbins_user
                    else:
                        nbins='auto'
                except ValueError:
                    nbins='auto'
            
            y_histo, x_histo=np.histogram(y, bins=nbins) #Generate histogram data
            x_histo_centers = (x_histo[:-1] + x_histo[1:]) / 2
            histo_width = x_histo[1] - x_histo[0]
            
            #Aqui va la grafica del histograma
            self.plotbar(x_histo_centers,y_histo,histo_width)
            self.histowidget.setLabel("bottom", ylabel)
            self.connect_btn.setEnabled(False) #To prevent stopping the data transfer when pressing the disconnect button

            return
        
app = QApplication(sys.argv)
style_file = resource_path("style.css")
app.setStyleSheet(load_stylesheet(style_file))
app.setWindowIcon(QIcon(os.path.join(icons_dir, "app_icon.ico")))
window = MainWindow()
window.show()
app.exec()