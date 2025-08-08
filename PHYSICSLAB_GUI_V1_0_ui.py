# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PHYSICSLAB_GUI_V1_0.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_contact = QLabel(self.centralwidget)
        self.label_contact.setObjectName(u"label_contact")
        self.label_contact.setGeometry(QRect(710, 620, 201, 20))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(210, 50, 841, 121))
        self.tab_analog = QWidget()
        self.tab_analog.setObjectName(u"tab_analog")
        self.gridLayoutWidget_4 = QWidget(self.tab_analog)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 813, 81))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.A2_value = QLineEdit(self.gridLayoutWidget_4)
        self.A2_value.setObjectName(u"A2_value")

        self.horizontalLayout_4.addWidget(self.A2_value)

        self.zero_A2 = QPushButton(self.gridLayoutWidget_4)
        self.zero_A2.setObjectName(u"zero_A2")

        self.horizontalLayout_4.addWidget(self.zero_A2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 2, 1, 1)

        self.A3_sensors = QComboBox(self.gridLayoutWidget_4)
        self.A3_sensors.addItem("")
        self.A3_sensors.addItem("")
        self.A3_sensors.addItem("")
        self.A3_sensors.addItem("")
        self.A3_sensors.addItem("")
        self.A3_sensors.addItem("")
        self.A3_sensors.addItem("")
        self.A3_sensors.setObjectName(u"A3_sensors")

        self.gridLayout.addWidget(self.A3_sensors, 1, 3, 1, 1)

        self.label_A1 = QLabel(self.gridLayoutWidget_4)
        self.label_A1.setObjectName(u"label_A1")

        self.gridLayout.addWidget(self.label_A1, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.A0_value = QLineEdit(self.gridLayoutWidget_4)
        self.A0_value.setObjectName(u"A0_value")

        self.horizontalLayout_2.addWidget(self.A0_value)

        self.zero_A0 = QPushButton(self.gridLayoutWidget_4)
        self.zero_A0.setObjectName(u"zero_A0")

        self.horizontalLayout_2.addWidget(self.zero_A0)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.A1_sensors = QComboBox(self.gridLayoutWidget_4)
        self.A1_sensors.addItem("")
        self.A1_sensors.addItem("")
        self.A1_sensors.addItem("")
        self.A1_sensors.addItem("")
        self.A1_sensors.addItem("")
        self.A1_sensors.addItem("")
        self.A1_sensors.addItem("")
        self.A1_sensors.setObjectName(u"A1_sensors")

        self.gridLayout.addWidget(self.A1_sensors, 1, 1, 1, 1)

        self.A2_sensors = QComboBox(self.gridLayoutWidget_4)
        self.A2_sensors.addItem("")
        self.A2_sensors.addItem("")
        self.A2_sensors.addItem("")
        self.A2_sensors.addItem("")
        self.A2_sensors.addItem("")
        self.A2_sensors.addItem("")
        self.A2_sensors.addItem("")
        self.A2_sensors.setObjectName(u"A2_sensors")

        self.gridLayout.addWidget(self.A2_sensors, 1, 2, 1, 1)

        self.A0_sensors = QComboBox(self.gridLayoutWidget_4)
        self.A0_sensors.addItem("")
        self.A0_sensors.addItem("")
        self.A0_sensors.addItem("")
        self.A0_sensors.addItem("")
        self.A0_sensors.addItem("")
        self.A0_sensors.addItem("")
        self.A0_sensors.addItem("")
        self.A0_sensors.setObjectName(u"A0_sensors")

        self.gridLayout.addWidget(self.A0_sensors, 1, 0, 1, 1)

        self.label_A0 = QLabel(self.gridLayoutWidget_4)
        self.label_A0.setObjectName(u"label_A0")

        self.gridLayout.addWidget(self.label_A0, 0, 0, 1, 1)

        self.label_A2 = QLabel(self.gridLayoutWidget_4)
        self.label_A2.setObjectName(u"label_A2")

        self.gridLayout.addWidget(self.label_A2, 0, 2, 1, 1)

        self.label_A3 = QLabel(self.gridLayoutWidget_4)
        self.label_A3.setObjectName(u"label_A3")

        self.gridLayout.addWidget(self.label_A3, 0, 3, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.A3_value = QLineEdit(self.gridLayoutWidget_4)
        self.A3_value.setObjectName(u"A3_value")

        self.horizontalLayout_5.addWidget(self.A3_value)

        self.zero_A3 = QPushButton(self.gridLayoutWidget_4)
        self.zero_A3.setObjectName(u"zero_A3")

        self.horizontalLayout_5.addWidget(self.zero_A3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.A1_value = QLineEdit(self.gridLayoutWidget_4)
        self.A1_value.setObjectName(u"A1_value")

        self.horizontalLayout_3.addWidget(self.A1_value)

        self.zero_A1 = QPushButton(self.gridLayoutWidget_4)
        self.zero_A1.setObjectName(u"zero_A1")

        self.horizontalLayout_3.addWidget(self.zero_A1)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.analog_time_label = QLabel(self.gridLayoutWidget_4)
        self.analog_time_label.setObjectName(u"analog_time_label")

        self.gridLayout.addWidget(self.analog_time_label, 0, 4, 1, 1)

        self.analog_start_btn = QPushButton(self.gridLayoutWidget_4)
        self.analog_start_btn.setObjectName(u"analog_start_btn")

        self.gridLayout.addWidget(self.analog_start_btn, 2, 4, 1, 1)

        self.analog_time_select = QComboBox(self.gridLayoutWidget_4)
        self.analog_time_select.addItem("")
        self.analog_time_select.addItem("")
        self.analog_time_select.addItem("")
        self.analog_time_select.addItem("")
        self.analog_time_select.setObjectName(u"analog_time_select")

        self.gridLayout.addWidget(self.analog_time_select, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tab_analog, "")
        self.tab_spi = QWidget()
        self.tab_spi.setObjectName(u"tab_spi")
        self.gridLayoutWidget_5 = QWidget(self.tab_spi)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 251, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SPI_sensor = QComboBox(self.gridLayoutWidget_5)
        self.SPI_sensor.addItem("")
        self.SPI_sensor.setObjectName(u"SPI_sensor")

        self.gridLayout_2.addWidget(self.SPI_sensor, 1, 0, 1, 1)

        self.SPI_sens_value = QLineEdit(self.gridLayoutWidget_5)
        self.SPI_sens_value.setObjectName(u"SPI_sens_value")

        self.gridLayout_2.addWidget(self.SPI_sens_value, 2, 0, 1, 1)

        self.SPI_port_label = QLabel(self.gridLayoutWidget_5)
        self.SPI_port_label.setObjectName(u"SPI_port_label")

        self.gridLayout_2.addWidget(self.SPI_port_label, 0, 0, 1, 1)

        self.Time_SPI_label = QLabel(self.gridLayoutWidget_5)
        self.Time_SPI_label.setObjectName(u"Time_SPI_label")

        self.gridLayout_2.addWidget(self.Time_SPI_label, 0, 1, 1, 1)

        self.spi_start_btn = QPushButton(self.gridLayoutWidget_5)
        self.spi_start_btn.setObjectName(u"spi_start_btn")

        self.gridLayout_2.addWidget(self.spi_start_btn, 2, 1, 1, 1)

        self.spi_time_select = QComboBox(self.gridLayoutWidget_5)
        self.spi_time_select.addItem("")
        self.spi_time_select.addItem("")
        self.spi_time_select.addItem("")
        self.spi_time_select.addItem("")
        self.spi_time_select.setObjectName(u"spi_time_select")

        self.gridLayout_2.addWidget(self.spi_time_select, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 6)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab_spi, "")
        self.tab_photogate = QWidget()
        self.tab_photogate.setObjectName(u"tab_photogate")
        self.tabWidget.addTab(self.tab_photogate, "")
        self.tab_help = QWidget()
        self.tab_help.setObjectName(u"tab_help")
        self.tabWidget.addTab(self.tab_help, "")
        self.label_title_line1 = QLabel(self.centralwidget)
        self.label_title_line1.setObjectName(u"label_title_line1")
        self.label_title_line1.setGeometry(QRect(300, 0, 601, 29))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_title_line1.setFont(font)
        self.label_title_line2 = QLabel(self.centralwidget)
        self.label_title_line2.setObjectName(u"label_title_line2")
        self.label_title_line2.setGeometry(QRect(400, 20, 601, 29))
        self.label_title_line2.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 50, 191, 121))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 141, 61))
        self.layout_port = QGridLayout(self.gridLayoutWidget)
        self.layout_port.setObjectName(u"layout_port")
        self.layout_port.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_port_4 = QLabel(self.gridLayoutWidget)
        self.label_port_4.setObjectName(u"label_port_4")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_port_4.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_port_4)


        self.layout_port.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.selectPort = QComboBox(self.gridLayoutWidget)
        self.selectPort.setObjectName(u"selectPort")

        self.horizontalLayout_6.addWidget(self.selectPort)

        self.connect_btn = QPushButton(self.gridLayoutWidget)
        self.connect_btn.setObjectName(u"connect_btn")

        self.horizontalLayout_6.addWidget(self.connect_btn)


        self.layout_port.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.label_connection = QLabel(self.frame)
        self.label_connection.setObjectName(u"label_connection")
        self.label_connection.setGeometry(QRect(10, 100, 171, 16))
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 190, 901, 431))
        self.tab_xyplot = QWidget()
        self.tab_xyplot.setObjectName(u"tab_xyplot")
        self.graphwidget = PlotWidget(self.tab_xyplot)
        self.graphwidget.setObjectName(u"graphwidget")
        self.graphwidget.setGeometry(QRect(10, 10, 800, 380))
        self.save_plot_btn = QPushButton(self.tab_xyplot)
        self.save_plot_btn.setObjectName(u"save_plot_btn")
        self.save_plot_btn.setGeometry(QRect(820, 370, 71, 24))
        self.clear_plot_btn = QPushButton(self.tab_xyplot)
        self.clear_plot_btn.setObjectName(u"clear_plot_btn")
        self.clear_plot_btn.setGeometry(QRect(820, 340, 71, 24))
        self.Yaxis_plot = QComboBox(self.tab_xyplot)
        self.Yaxis_plot.setObjectName(u"Yaxis_plot")
        self.Yaxis_plot.setGeometry(QRect(820, 40, 69, 22))
        self.label = QLabel(self.tab_xyplot)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(820, 20, 49, 16))
        self.tabWidget_2.addTab(self.tab_xyplot, "")
        self.tab_histogram = QWidget()
        self.tab_histogram.setObjectName(u"tab_histogram")
        self.histowidget = PlotWidget(self.tab_histogram)
        self.histowidget.setObjectName(u"histowidget")
        self.histowidget.setGeometry(QRect(10, 10, 800, 380))
        self.clear_plotbar_btn = QPushButton(self.tab_histogram)
        self.clear_plotbar_btn.setObjectName(u"clear_plotbar_btn")
        self.clear_plotbar_btn.setGeometry(QRect(820, 340, 71, 24))
        self.save_plotbar_btn = QPushButton(self.tab_histogram)
        self.save_plotbar_btn.setObjectName(u"save_plotbar_btn")
        self.save_plotbar_btn.setGeometry(QRect(820, 370, 71, 24))
        self.label_bins = QLabel(self.tab_histogram)
        self.label_bins.setObjectName(u"label_bins")
        self.label_bins.setGeometry(QRect(810, 20, 91, 51))
        self.auto_bins = QRadioButton(self.tab_histogram)
        self.auto_bins.setObjectName(u"auto_bins")
        self.auto_bins.setGeometry(QRect(830, 50, 51, 51))
        self.auto_bins.setChecked(True)
        self.number_bins = QLineEdit(self.tab_histogram)
        self.number_bins.setObjectName(u"number_bins")
        self.number_bins.setEnabled(False)
        self.number_bins.setGeometry(QRect(830, 90, 51, 22))
        self.tabWidget_2.addTab(self.tab_histogram, "")
        self.tab_table = QWidget()
        self.tab_table.setObjectName(u"tab_table")
        self.StatusText = QTextEdit(self.tab_table)
        self.StatusText.setObjectName(u"StatusText")
        self.StatusText.setGeometry(QRect(0, 10, 811, 391))
        self.StatusText.setReadOnly(True)
        self.clear_console_btn = QPushButton(self.tab_table)
        self.clear_console_btn.setObjectName(u"clear_console_btn")
        self.clear_console_btn.setGeometry(QRect(820, 370, 71, 24))
        self.tabWidget_2.addTab(self.tab_table, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.label_contact.raise_()
        self.tabWidget.raise_()
        self.label_title_line1.raise_()
        self.label_title_line2.raise_()
        self.tabWidget_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PHYSICSLAB", None))
        self.label_contact.setText(QCoreApplication.translate("MainWindow", u"contacto: luisf.ramirez@udea.edu.co", None))
        self.zero_A2.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.A3_sensors.setItemText(0, QCoreApplication.translate("MainWindow", u"Voltaje (V)", None))
        self.A3_sensors.setItemText(1, QCoreApplication.translate("MainWindow", u"Iluminancia (AMS104)", None))
        self.A3_sensors.setItemText(2, QCoreApplication.translate("MainWindow", u"Campo magn\u00e9tico (A1302)", None))
        self.A3_sensors.setItemText(3, QCoreApplication.translate("MainWindow", u"%H.R. (HIH4000)", None))
        self.A3_sensors.setItemText(4, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5004)", None))
        self.A3_sensors.setItemText(5, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5100)", None))
        self.A3_sensors.setItemText(6, QCoreApplication.translate("MainWindow", u"Valor ADC (10 bits)", None))

        self.label_A1.setText(QCoreApplication.translate("MainWindow", u"Puerto A1", None))
        self.A0_value.setText("")
        self.zero_A0.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.A1_sensors.setItemText(0, QCoreApplication.translate("MainWindow", u"Voltaje (V)", None))
        self.A1_sensors.setItemText(1, QCoreApplication.translate("MainWindow", u"Iluminancia (AMS104)", None))
        self.A1_sensors.setItemText(2, QCoreApplication.translate("MainWindow", u"Campo magn\u00e9tico (A1302)", None))
        self.A1_sensors.setItemText(3, QCoreApplication.translate("MainWindow", u"%H.R. (HIH4000)", None))
        self.A1_sensors.setItemText(4, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5004)", None))
        self.A1_sensors.setItemText(5, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5100)", None))
        self.A1_sensors.setItemText(6, QCoreApplication.translate("MainWindow", u"Valor ADC (10 bits)", None))

        self.A2_sensors.setItemText(0, QCoreApplication.translate("MainWindow", u"Voltaje (V)", None))
        self.A2_sensors.setItemText(1, QCoreApplication.translate("MainWindow", u"Iluminancia (AMS104)", None))
        self.A2_sensors.setItemText(2, QCoreApplication.translate("MainWindow", u"Campo magn\u00e9tico (A1302)", None))
        self.A2_sensors.setItemText(3, QCoreApplication.translate("MainWindow", u"%H.R. (HIH4000)", None))
        self.A2_sensors.setItemText(4, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5004)", None))
        self.A2_sensors.setItemText(5, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5100)", None))
        self.A2_sensors.setItemText(6, QCoreApplication.translate("MainWindow", u"Valor ADC (10 bits)", None))

        self.A0_sensors.setItemText(0, QCoreApplication.translate("MainWindow", u"Voltaje (V)", None))
        self.A0_sensors.setItemText(1, QCoreApplication.translate("MainWindow", u"Iluminancia (AMS104)", None))
        self.A0_sensors.setItemText(2, QCoreApplication.translate("MainWindow", u"Campo magn\u00e9tico (A1302)", None))
        self.A0_sensors.setItemText(3, QCoreApplication.translate("MainWindow", u"%H.R. (HIH4000)", None))
        self.A0_sensors.setItemText(4, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5004)", None))
        self.A0_sensors.setItemText(5, QCoreApplication.translate("MainWindow", u"Presi\u00f3n (MPXV5100)", None))
        self.A0_sensors.setItemText(6, QCoreApplication.translate("MainWindow", u"Valor ADC (10 bits)", None))

        self.label_A0.setText(QCoreApplication.translate("MainWindow", u"Puerto A0", None))
        self.label_A2.setText(QCoreApplication.translate("MainWindow", u"Puerto A2", None))
        self.label_A3.setText(QCoreApplication.translate("MainWindow", u"Puerto A3", None))
        self.zero_A3.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.zero_A1.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.analog_time_label.setText(QCoreApplication.translate("MainWindow", u"Tiempo (s):", None))
        self.analog_start_btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR!", None))
        self.analog_time_select.setItemText(0, QCoreApplication.translate("MainWindow", u"100 ms", None))
        self.analog_time_select.setItemText(1, QCoreApplication.translate("MainWindow", u"500 ms", None))
        self.analog_time_select.setItemText(2, QCoreApplication.translate("MainWindow", u"1 s", None))
        self.analog_time_select.setItemText(3, QCoreApplication.translate("MainWindow", u"2 s", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analog), QCoreApplication.translate("MainWindow", u"Sensores anal\u00f3gicos", None))
        self.SPI_sensor.setItemText(0, QCoreApplication.translate("MainWindow", u"Temperatura (MAX6674/5)", None))

        self.SPI_sens_value.setText("")
        self.SPI_port_label.setText(QCoreApplication.translate("MainWindow", u"Puerto SPI", None))
        self.Time_SPI_label.setText(QCoreApplication.translate("MainWindow", u"Tiempo (s):", None))
        self.spi_start_btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR!", None))
        self.spi_time_select.setItemText(0, QCoreApplication.translate("MainWindow", u"100 ms", None))
        self.spi_time_select.setItemText(1, QCoreApplication.translate("MainWindow", u"500 ms", None))
        self.spi_time_select.setItemText(2, QCoreApplication.translate("MainWindow", u"1 s", None))
        self.spi_time_select.setItemText(3, QCoreApplication.translate("MainWindow", u"2 s", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spi), QCoreApplication.translate("MainWindow", u"Sensores SPI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_photogate), QCoreApplication.translate("MainWindow", u"Fotocompuertas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_help), QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label_title_line1.setText(QCoreApplication.translate("MainWindow", u"Sistema de Adquisici\u00f3n de datos para los Laboratorios Integrados de F\u00edsica", None))
        self.label_title_line2.setText(QCoreApplication.translate("MainWindow", u"Instituto de F\u00edsica, Universidad de Antioquia, 2025", None))
        self.label_port_4.setText(QCoreApplication.translate("MainWindow", u"Puerto serial", None))
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label_connection.setText("")
        self.save_plot_btn.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.clear_plot_btn.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Eje Y:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_xyplot), QCoreApplication.translate("MainWindow", u"Gr\u00e1fica", None))
        self.clear_plotbar_btn.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.save_plotbar_btn.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.label_bins.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de bins", None))
        self.auto_bins.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.number_bins.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_histogram), QCoreApplication.translate("MainWindow", u"Histograma", None))
        self.StatusText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Not connected</p></body></html>", None))
        self.clear_console_btn.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_table), QCoreApplication.translate("MainWindow", u"Consola", None))
    # retranslateUi

