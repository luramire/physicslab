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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(210, 60, 861, 161))
        self.tab_analog = QWidget()
        self.tab_analog.setObjectName(u"tab_analog")
        self.gridLayoutWidget_4 = QWidget(self.tab_analog)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 0, 841, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.A2_value = QLineEdit(self.gridLayoutWidget_4)
        self.A2_value.setObjectName(u"A2_value")
        self.A2_value.setReadOnly(True)

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
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.A0_value = QLineEdit(self.gridLayoutWidget_4)
        self.A0_value.setObjectName(u"A0_value")
        self.A0_value.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.A0_value)

        self.zero_A0 = QPushButton(self.gridLayoutWidget_4)
        self.zero_A0.setObjectName(u"zero_A0")
        font = QFont()
        font.setPointSize(10)
        self.zero_A0.setFont(font)

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
        self.label_A0.setFont(font)

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
        self.A3_value.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.A3_value)

        self.zero_A3 = QPushButton(self.gridLayoutWidget_4)
        self.zero_A3.setObjectName(u"zero_A3")

        self.horizontalLayout_5.addWidget(self.zero_A3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.A1_value = QLineEdit(self.gridLayoutWidget_4)
        self.A1_value.setObjectName(u"A1_value")
        self.A1_value.setReadOnly(True)

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
        self.analog_start_btn.setMinimumSize(QSize(94, 24))
        icon = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.MediaPlaybackStart):
            icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart)
        else:
            icon.addFile(u"../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.analog_start_btn.setIcon(icon)

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
        self.gridLayoutWidget_5.setGeometry(QRect(10, 0, 291, 111))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SPI_sensor = QComboBox(self.gridLayoutWidget_5)
        self.SPI_sensor.addItem("")
        self.SPI_sensor.setObjectName(u"SPI_sensor")

        self.gridLayout_2.addWidget(self.SPI_sensor, 1, 0, 1, 1)

        self.SPI_sens_value = QLineEdit(self.gridLayoutWidget_5)
        self.SPI_sens_value.setObjectName(u"SPI_sens_value")
        self.SPI_sens_value.setReadOnly(True)

        self.gridLayout_2.addWidget(self.SPI_sens_value, 2, 0, 1, 1)

        self.SPI_port_label = QLabel(self.gridLayoutWidget_5)
        self.SPI_port_label.setObjectName(u"SPI_port_label")
        self.SPI_port_label.setFont(font)

        self.gridLayout_2.addWidget(self.SPI_port_label, 0, 0, 1, 1)

        self.Time_SPI_label = QLabel(self.gridLayoutWidget_5)
        self.Time_SPI_label.setObjectName(u"Time_SPI_label")

        self.gridLayout_2.addWidget(self.Time_SPI_label, 0, 1, 1, 1)

        self.spi_start_btn = QPushButton(self.gridLayoutWidget_5)
        self.spi_start_btn.setObjectName(u"spi_start_btn")
        self.spi_start_btn.setMinimumSize(QSize(94, 25))
        self.spi_start_btn.setFont(font)
        self.spi_start_btn.setIcon(icon)

        self.gridLayout_2.addWidget(self.spi_start_btn, 2, 1, 1, 1)

        self.spi_time_select = QComboBox(self.gridLayoutWidget_5)
        self.spi_time_select.addItem("")
        self.spi_time_select.addItem("")
        self.spi_time_select.addItem("")
        self.spi_time_select.addItem("")
        self.spi_time_select.setObjectName(u"spi_time_select")

        self.gridLayout_2.addWidget(self.spi_time_select, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 6)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.tabWidget.addTab(self.tab_spi, "")
        self.tab_photogate = QWidget()
        self.tab_photogate.setObjectName(u"tab_photogate")
        self.size_entry = QLineEdit(self.tab_photogate)
        self.size_entry.setObjectName(u"size_entry")
        self.size_entry.setGeometry(QRect(500, 10, 81, 30))
        self.gridLayoutWidget_2 = QWidget(self.tab_photogate)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 321, 111))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.photo_option = QComboBox(self.gridLayoutWidget_2)
        self.photo_option.addItem("")
        self.photo_option.addItem("")
        self.photo_option.addItem("")
        self.photo_option.addItem("")
        self.photo_option.setObjectName(u"photo_option")
        font1 = QFont()
        font1.setPointSize(9)
        self.photo_option.setFont(font1)

        self.gridLayout_3.addWidget(self.photo_option, 1, 0, 1, 1)

        self.photo_start_btn = QPushButton(self.gridLayoutWidget_2)
        self.photo_start_btn.setObjectName(u"photo_start_btn")
        self.photo_start_btn.setMinimumSize(QSize(90, 25))
        self.photo_start_btn.setFont(font)
        self.photo_start_btn.setIcon(icon)

        self.gridLayout_3.addWidget(self.photo_start_btn, 2, 1, 1, 1)

        self.label_portD7 = QLabel(self.gridLayoutWidget_2)
        self.label_portD7.setObjectName(u"label_portD7")
        self.label_portD7.setFont(font)

        self.gridLayout_3.addWidget(self.label_portD7, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.photo_value = QLineEdit(self.gridLayoutWidget_2)
        self.photo_value.setObjectName(u"photo_value")
        self.photo_value.setReadOnly(True)

        self.horizontalLayout.addWidget(self.photo_value)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.label_photo_options = QLabel(self.gridLayoutWidget_2)
        self.label_photo_options.setObjectName(u"label_photo_options")
        self.label_photo_options.setPixmap(QPixmap(u"../../../../../.designer/backup/tiempo_oscuridad.bmp"))

        self.gridLayout_3.addWidget(self.label_photo_options, 0, 1, 2, 1)

        self.line = QFrame(self.tab_photogate)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(330, 0, 20, 131))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.operation_option = QComboBox(self.tab_photogate)
        self.operation_option.addItem("")
        self.operation_option.addItem("")
        self.operation_option.addItem("")
        self.operation_option.setObjectName(u"operation_option")
        self.operation_option.setGeometry(QRect(350, 75, 119, 30))
        self.label_operacion = QLabel(self.tab_photogate)
        self.label_operacion.setObjectName(u"label_operacion")
        self.label_operacion.setGeometry(QRect(350, 40, 91, 30))
        self.label_velocidad = QLabel(self.tab_photogate)
        self.label_velocidad.setObjectName(u"label_velocidad")
        self.label_velocidad.setGeometry(QRect(610, 10, 111, 30))
        self.label_velocidad.setFont(font)
        self.label_igual1 = QLabel(self.tab_photogate)
        self.label_igual1.setObjectName(u"label_igual1")
        self.label_igual1.setGeometry(QRect(470, 70, 31, 30))
        self.label_igual1.setFont(font)
        self.label_division = QLabel(self.tab_photogate)
        self.label_division.setObjectName(u"label_division")
        self.label_division.setGeometry(QRect(520, 40, 31, 30))
        self.label_division.setFont(font)
        self.operation_result = QLineEdit(self.tab_photogate)
        self.operation_result.setObjectName(u"operation_result")
        self.operation_result.setGeometry(QRect(500, 75, 81, 30))
        self.operation_result.setReadOnly(True)
        self.velocity_value = QLineEdit(self.tab_photogate)
        self.velocity_value.setObjectName(u"velocity_value")
        self.velocity_value.setGeometry(QRect(613, 40, 111, 30))
        self.velocity_value.setReadOnly(True)
        self.label_igual2 = QLabel(self.tab_photogate)
        self.label_igual2.setObjectName(u"label_igual2")
        self.label_igual2.setGeometry(QRect(580, 40, 31, 30))
        self.line_2 = QFrame(self.tab_photogate)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(725, 0, 20, 131))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.average_time = QLineEdit(self.tab_photogate)
        self.average_time.setObjectName(u"average_time")
        self.average_time.setGeometry(QRect(750, 39, 91, 29))
        self.average_time.setReadOnly(True)
        self.label_tiempo_medio = QLabel(self.tab_photogate)
        self.label_tiempo_medio.setObjectName(u"label_tiempo_medio")
        self.label_tiempo_medio.setGeometry(QRect(740, -11, 121, 50))
        self.label_tiempo_medio.setFont(font)
        self.Xaxis_checkBox = QCheckBox(self.tab_photogate)
        self.Xaxis_checkBox.setObjectName(u"Xaxis_checkBox")
        self.Xaxis_checkBox.setGeometry(QRect(740, 68, 121, 50))
        self.Xaxis_checkBox.setFont(font)
        self.Xaxis_checkBox.setAcceptDrops(False)
        self.label_tamano = QLabel(self.tab_photogate)
        self.label_tamano.setObjectName(u"label_tamano")
        self.label_tamano.setGeometry(QRect(380, 5, 111, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_tamano.setFont(font2)
        self.tabWidget.addTab(self.tab_photogate, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(360, 0, 381, 111))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.port6_value = QLineEdit(self.gridLayoutWidget_3)
        self.port6_value.setObjectName(u"port6_value")

        self.gridLayout_4.addWidget(self.port6_value, 1, 1, 1, 1)

        self.label_value_port6 = QLabel(self.gridLayoutWidget_3)
        self.label_value_port6.setObjectName(u"label_value_port6")

        self.gridLayout_4.addWidget(self.label_value_port6, 0, 1, 1, 1)

        self.label_mode_port6 = QLabel(self.gridLayoutWidget_3)
        self.label_mode_port6.setObjectName(u"label_mode_port6")

        self.gridLayout_4.addWidget(self.label_mode_port6, 0, 0, 1, 1)

        self.port6_option = QComboBox(self.gridLayoutWidget_3)
        self.port6_option.addItem("")
        self.port6_option.addItem("")
        self.port6_option.addItem("")
        self.port6_option.setObjectName(u"port6_option")

        self.gridLayout_4.addWidget(self.port6_option, 1, 0, 1, 1)

        self.port6_apply_btn = QPushButton(self.gridLayoutWidget_3)
        self.port6_apply_btn.setObjectName(u"port6_apply_btn")
        self.port6_apply_btn.setMinimumSize(QSize(0, 35))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.port6_apply_btn.setIcon(icon1)

        self.gridLayout_4.addWidget(self.port6_apply_btn, 2, 1, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayoutWidget_6 = QWidget(self.tab)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 0, 311, 111))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_mode_port5 = QLabel(self.gridLayoutWidget_6)
        self.label_mode_port5.setObjectName(u"label_mode_port5")

        self.gridLayout_5.addWidget(self.label_mode_port5, 0, 0, 1, 1)

        self.port5_option = QComboBox(self.gridLayoutWidget_6)
        self.port5_option.addItem("")
        self.port5_option.setObjectName(u"port5_option")

        self.gridLayout_5.addWidget(self.port5_option, 1, 0, 1, 1)

        self.port5_value = QLineEdit(self.gridLayoutWidget_6)
        self.port5_value.setObjectName(u"port5_value")

        self.gridLayout_5.addWidget(self.port5_value, 1, 1, 1, 1)

        self.label_value_port5 = QLabel(self.gridLayoutWidget_6)
        self.label_value_port5.setObjectName(u"label_value_port5")

        self.gridLayout_5.addWidget(self.label_value_port5, 0, 1, 1, 1)

        self.port5_apply_btn = QPushButton(self.gridLayoutWidget_6)
        self.port5_apply_btn.setObjectName(u"port5_apply_btn")
        self.port5_apply_btn.setMinimumSize(QSize(0, 35))
        self.port5_apply_btn.setIcon(icon1)

        self.gridLayout_5.addWidget(self.port5_apply_btn, 2, 1, 1, 1)

        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setColumnStretch(0, 2)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(330, 0, 20, 131))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab, "")
        self.tab_help = QWidget()
        self.tab_help.setObjectName(u"tab_help")
        self.label_qr = QLabel(self.tab_help)
        self.label_qr.setObjectName(u"label_qr")
        self.label_qr.setGeometry(QRect(730, 5, 120, 120))
        self.label_3 = QLabel(self.tab_help)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(570, 10, 151, 101))
        self.label_diagram = QLabel(self.tab_help)
        self.label_diagram.setObjectName(u"label_diagram")
        self.label_diagram.setGeometry(QRect(10, 5, 151, 120))
        self.textEdit = QTextEdit(self.tab_help)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(170, 5, 381, 120))
        self.textEdit.setReadOnly(True)
        self.tabWidget.addTab(self.tab_help, "")
        self.label_title_line1 = QLabel(self.centralwidget)
        self.label_title_line1.setObjectName(u"label_title_line1")
        self.label_title_line1.setGeometry(QRect(300, 0, 601, 29))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_title_line1.setFont(font3)
        self.label_title_line2 = QLabel(self.centralwidget)
        self.label_title_line2.setObjectName(u"label_title_line2")
        self.label_title_line2.setGeometry(QRect(400, 25, 601, 29))
        self.label_title_line2.setFont(font3)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 60, 201, 161))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setLineWidth(2)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 181, 141))
        self.layout_port = QGridLayout(self.gridLayoutWidget)
        self.layout_port.setObjectName(u"layout_port")
        self.layout_port.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.refresh_ports_btn = QPushButton(self.gridLayoutWidget)
        self.refresh_ports_btn.setObjectName(u"refresh_ports_btn")
        font4 = QFont()
        font4.setPointSize(12)
        self.refresh_ports_btn.setFont(font4)
        icon2 = QIcon()
        iconThemeName = u"view-refresh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.refresh_ports_btn.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.refresh_ports_btn)

        self.selectPort = QComboBox(self.gridLayoutWidget)
        self.selectPort.setObjectName(u"selectPort")
        self.selectPort.setFont(font4)

        self.horizontalLayout_6.addWidget(self.selectPort)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.layout_port.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.connect_btn = QPushButton(self.gridLayoutWidget)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setFont(font)

        self.layout_port.addWidget(self.connect_btn, 2, 0, 1, 1)

        self.label_port_4 = QLabel(self.gridLayoutWidget)
        self.label_port_4.setObjectName(u"label_port_4")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        self.label_port_4.setFont(font5)

        self.layout_port.addWidget(self.label_port_4, 0, 0, 1, 1)

        self.label_connection = QLabel(self.gridLayoutWidget)
        self.label_connection.setObjectName(u"label_connection")
        self.label_connection.setFont(font)

        self.layout_port.addWidget(self.label_connection, 3, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 230, 935, 405))
        self.tab_xyplot = QWidget()
        self.tab_xyplot.setObjectName(u"tab_xyplot")
        self.graphwidget = PlotWidget(self.tab_xyplot)
        self.graphwidget.setObjectName(u"graphwidget")
        self.graphwidget.setGeometry(QRect(1, 10, 800, 360))
        self.graphwidget.setFont(font)
        self.save_plot_btn = QPushButton(self.tab_xyplot)
        self.save_plot_btn.setObjectName(u"save_plot_btn")
        self.save_plot_btn.setGeometry(QRect(810, 330, 110, 30))
        icon3 = QIcon()
        iconThemeName = u"document-save-as"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.save_plot_btn.setIcon(icon3)
        self.clear_plot_btn = QPushButton(self.tab_xyplot)
        self.clear_plot_btn.setObjectName(u"clear_plot_btn")
        self.clear_plot_btn.setGeometry(QRect(810, 290, 110, 30))
        icon4 = QIcon()
        iconThemeName = u"edit-delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u"../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.clear_plot_btn.setIcon(icon4)
        self.Yaxis_plot = QComboBox(self.tab_xyplot)
        self.Yaxis_plot.setObjectName(u"Yaxis_plot")
        self.Yaxis_plot.setGeometry(QRect(810, 110, 110, 30))
        self.label = QLabel(self.tab_xyplot)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(810, 70, 49, 30))
        self.tabWidget_2.addTab(self.tab_xyplot, "")
        self.tab_histogram = QWidget()
        self.tab_histogram.setObjectName(u"tab_histogram")
        self.histowidget = PlotWidget(self.tab_histogram)
        self.histowidget.setObjectName(u"histowidget")
        self.histowidget.setGeometry(QRect(1, 10, 800, 360))
        self.clear_plotbar_btn = QPushButton(self.tab_histogram)
        self.clear_plotbar_btn.setObjectName(u"clear_plotbar_btn")
        self.clear_plotbar_btn.setGeometry(QRect(810, 290, 110, 30))
        self.clear_plotbar_btn.setIcon(icon4)
        self.save_plotbar_btn = QPushButton(self.tab_histogram)
        self.save_plotbar_btn.setObjectName(u"save_plotbar_btn")
        self.save_plotbar_btn.setGeometry(QRect(810, 330, 110, 30))
        self.save_plotbar_btn.setIcon(icon3)
        self.label_bins = QLabel(self.tab_histogram)
        self.label_bins.setObjectName(u"label_bins")
        self.label_bins.setGeometry(QRect(810, 50, 121, 51))
        self.label_bins.setFont(font)
        self.auto_bins = QRadioButton(self.tab_histogram)
        self.auto_bins.setObjectName(u"auto_bins")
        self.auto_bins.setGeometry(QRect(825, 90, 81, 41))
        self.auto_bins.setFont(font)
        self.auto_bins.setChecked(True)
        self.number_bins = QLineEdit(self.tab_histogram)
        self.number_bins.setObjectName(u"number_bins")
        self.number_bins.setEnabled(False)
        self.number_bins.setGeometry(QRect(830, 130, 51, 30))
        self.number_bins.setFont(font)
        self.tabWidget_2.addTab(self.tab_histogram, "")
        self.tab_table = QWidget()
        self.tab_table.setObjectName(u"tab_table")
        self.StatusText = QTextEdit(self.tab_table)
        self.StatusText.setObjectName(u"StatusText")
        self.StatusText.setGeometry(QRect(1, 10, 800, 360))
        self.StatusText.setReadOnly(True)
        self.clear_console_btn = QPushButton(self.tab_table)
        self.clear_console_btn.setObjectName(u"clear_console_btn")
        self.clear_console_btn.setGeometry(QRect(810, 290, 110, 30))
        self.clear_console_btn.setIcon(icon4)
        self.label_contact = QLabel(self.tab_table)
        self.label_contact.setObjectName(u"label_contact")
        self.label_contact.setGeometry(QRect(930, 190, 141, 111))
        self.tabWidget_2.addTab(self.tab_table, "")
        self.udea_logo_label = QLabel(self.centralwidget)
        self.udea_logo_label.setObjectName(u"udea_logo_label")
        self.udea_logo_label.setGeometry(QRect(960, 330, 100, 129))
        self.udea_logo_label.setTextFormat(Qt.TextFormat.PlainText)
        self.udea_logo_label.setOpenExternalLinks(True)
        self.udea_logo_label.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.gicm_logolabel = QLabel(self.centralwidget)
        self.gicm_logolabel.setObjectName(u"gicm_logolabel")
        self.gicm_logolabel.setGeometry(QRect(960, 500, 100, 129))
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.tabWidget.raise_()
        self.label_title_line1.raise_()
        self.label_title_line2.raise_()
        self.tabWidget_2.raise_()
        self.udea_logo_label.raise_()
        self.gicm_logolabel.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PHYSICSLAB v1.0", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(QCoreApplication.translate("MainWindow", u"Programmed by: L. Felipe Ramirez <luisf.ramirez@udea.edu.co>", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
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
        self.analog_start_btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.analog_time_select.setItemText(0, QCoreApplication.translate("MainWindow", u"100 ms", None))
        self.analog_time_select.setItemText(1, QCoreApplication.translate("MainWindow", u"500 ms", None))
        self.analog_time_select.setItemText(2, QCoreApplication.translate("MainWindow", u"1 s", None))
        self.analog_time_select.setItemText(3, QCoreApplication.translate("MainWindow", u"2 s", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analog), QCoreApplication.translate("MainWindow", u"Sensores anal\u00f3gicos", None))
        self.SPI_sensor.setItemText(0, QCoreApplication.translate("MainWindow", u"Temperatura (MAX6675)", None))

        self.SPI_sens_value.setText("")
        self.SPI_port_label.setText(QCoreApplication.translate("MainWindow", u"Puerto SPI", None))
        self.Time_SPI_label.setText(QCoreApplication.translate("MainWindow", u"Tiempo (s):", None))
        self.spi_start_btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.spi_time_select.setItemText(0, QCoreApplication.translate("MainWindow", u"200 ms", None))
        self.spi_time_select.setItemText(1, QCoreApplication.translate("MainWindow", u"500 ms", None))
        self.spi_time_select.setItemText(2, QCoreApplication.translate("MainWindow", u"1 s", None))
        self.spi_time_select.setItemText(3, QCoreApplication.translate("MainWindow", u"2 s", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spi), QCoreApplication.translate("MainWindow", u"Sensores SPI", None))
        self.size_entry.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.photo_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Tiempo de oscuridad", None))
        self.photo_option.setItemText(1, QCoreApplication.translate("MainWindow", u"Tiempo claro->oscuro", None))
        self.photo_option.setItemText(2, QCoreApplication.translate("MainWindow", u"Tiempo claro<->oscuro", None))
        self.photo_option.setItemText(3, QCoreApplication.translate("MainWindow", u"Tiempo doble fotocompuerta", None))

        self.photo_start_btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.label_portD7.setText(QCoreApplication.translate("MainWindow", u"Puerto D8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Valor:", None))
        self.label_photo_options.setText("")
        self.operation_option.setItemText(0, QCoreApplication.translate("MainWindow", u"t_n", None))
        self.operation_option.setItemText(1, QCoreApplication.translate("MainWindow", u"t_n - t_(n-1)", None))
        self.operation_option.setItemText(2, QCoreApplication.translate("MainWindow", u"t_n - t_(n-2)", None))

        self.label_operacion.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n:", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_igual1.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label_division.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.operation_result.setText("")
        self.label_igual2.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(whatsthis)
        self.label_tiempo_medio.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_tiempo_medio.setText(QCoreApplication.translate("MainWindow", u"Tiempo\n"
"medio (ms)", None))
        self.Xaxis_checkBox.setText(QCoreApplication.translate("MainWindow", u"Fijar como\n"
"eje X", None))
        self.label_tamano.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o (cm):", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_photogate), QCoreApplication.translate("MainWindow", u"Fotocompuertas", None))
        self.label_value_port6.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
        self.label_mode_port6.setText(QCoreApplication.translate("MainWindow", u"Modo del puerto D6:", None))
        self.port6_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Generador de se\u00f1al cuadrada", None))
        self.port6_option.setItemText(1, QCoreApplication.translate("MainWindow", u"Valor del puerto A0 Controla ON/OFF", None))
        self.port6_option.setItemText(2, QCoreApplication.translate("MainWindow", u"Definir estado del puerto (0 \u00f3 1)", None))

        self.port6_apply_btn.setText(QCoreApplication.translate("MainWindow", u"APLICAR", None))
        self.label_mode_port5.setText(QCoreApplication.translate("MainWindow", u"Modo del puerto D5", None))
        self.port5_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Se\u00f1al PWM de 490 Hz", None))

        self.label_value_port5.setText(QCoreApplication.translate("MainWindow", u"Duty Cycle (0-255):", None))
        self.port5_apply_btn.setText(QCoreApplication.translate("MainWindow", u"APLICAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Salidas digitales", None))
        self.label_qr.setText(QCoreApplication.translate("MainWindow", u"QR code", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Escanea el c\u00f3digo para\n"
"encontrar las gu\u00edas de\n"
"usuario e informaci\u00f3n\n"
"adicional.", None))
        self.label_diagram.setText(QCoreApplication.translate("MainWindow", u"board diagram", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Conecta los </span><span style=\" font-size:8pt; font-weight:700;\">sensores anal\u00f3gicos</span><span style=\" font-size:8pt;\"> en los puertos A0, A1, A2 \u00f3 A3 empleando los cables planos incluidos en el kit. En la pesta\u00f1a 'Sensores anal\u00f3gicos' selecciona el sensor conectado a cada puerto.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Los </span><span style=\" font-size:8pt; font-weight:700;\">sensores digitales</span><span style=\" font-size:8pt;\"> como la termocupla se conectan en el puerto SPI usando el cable plano incluido.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">El </span><span style=\" font-size:8pt; font-weight:700;\">sensor reflectivo (fotocompuerta)</span><span style=\" font-size:8pt;\"> se conecta al puerto D8. El segundo sensor reflectivo se conecta al pu"
                        "erto D38. Para que los sensores reflectivos funcionen, debes conectar un adaptador de 12 V para Arduino en el conector tipo DC-jack de la tarjeta. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Las </span><span style=\" font-size:8pt; font-weight:700;\">salidas digitales</span><span style=\" font-size:8pt;\"> se acceden desde los pines 5 \u00f3 6 empleando cables de protoboard. Las se\u00f1ales son generadas respecto al pin de tierra (GND). Puedes desactivar las se\u00f1ales en cualquier momento presionando el bot\u00f3n S1 de la tarjeta. </span><span style=\" font-size:8pt; font-weight:700;\">Ten cuidado</span><span style=\" font-size:8pt;\"> de no conectar los pines 5 \u00f3 6 a tierra ya que as\u00ed puedes da\u00f1"
                        "arlos.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Si tienes dudas, visita el sitio:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/luramire/physicslab/wiki\"><span style=\" text-decoration: underline; color:#004275;\">https://github.com/luramire/physicslab/wiki</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">o escr\u00edbeme a luisf.ramirez@udea.edu.co.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-----------------</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Programado por Luis Felipe Ram\u00edrez Garc\u00eda usando PySide6.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Instituto de F\u00edsica</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Universidad de Antioquia</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2025</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_help), QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label_title_line1.setText(QCoreApplication.translate("MainWindow", u"Sistema de Adquisici\u00f3n de datos para los Laboratorios Integrados de F\u00edsica", None))
        self.label_title_line2.setText(QCoreApplication.translate("MainWindow", u"Instituto de F\u00edsica, Universidad de Antioquia, 2025", None))
        self.refresh_ports_btn.setText("")
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.label_port_4.setText(QCoreApplication.translate("MainWindow", u"Puerto serial", None))
        self.label_connection.setText("")
        self.save_plot_btn.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.clear_plot_btn.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Eje Y:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_xyplot), QCoreApplication.translate("MainWindow", u"Gr\u00e1fica", None))
        self.clear_plotbar_btn.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.save_plotbar_btn.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.label_bins.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de bins:", None))
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
        self.label_contact.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Programmed by:</p><p><br/>L. Felipe Ram\u00edrez G.</p><p>Instituto de F\u00edsica</p><p>Universidad de Antioquia</p><p>2025</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_table), QCoreApplication.translate("MainWindow", u"Consola", None))
        self.udea_logo_label.setText(QCoreApplication.translate("MainWindow", u"udea logo", None))
        self.gicm_logolabel.setText(QCoreApplication.translate("MainWindow", u"gicm logo", None))
    # retranslateUi

