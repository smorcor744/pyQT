# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'habitaciones.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 724)
        MainWindow.setMinimumSize(QSize(1050, 680))
        MainWindow.setStyleSheet(u"background-color:;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 60, 91, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 155, 131, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 220, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 290, 121, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 350, 71, 16))
        self.bt_registrar_habitacion = QPushButton(self.centralwidget)
        self.bt_registrar_habitacion.setObjectName(u"bt_registrar_habitacion")
        self.bt_registrar_habitacion.setGeometry(QRect(130, 420, 75, 24))
        self.bt_registrar_habitacion.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.textNumero = QLineEdit(self.centralwidget)
        self.textNumero.setObjectName(u"textNumero")
        self.textNumero.setGeometry(QRect(50, 180, 241, 31))
        self.textprecio_noche = QLineEdit(self.centralwidget)
        self.textprecio_noche.setObjectName(u"textprecio_noche")
        self.textprecio_noche.setGeometry(QRect(50, 310, 241, 31))
        self.bt_mostrar_habitaciones = QPushButton(self.centralwidget)
        self.bt_mostrar_habitaciones.setObjectName(u"bt_mostrar_habitaciones")
        self.bt_mostrar_habitaciones.setGeometry(QRect(630, 510, 121, 31))
        self.bt_mostrar_habitaciones.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.tablahabitaciones = QTableWidget(self.centralwidget)
        self.tablahabitaciones.setObjectName(u"tablahabitaciones")
        self.tablahabitaciones.setEnabled(True)
        self.tablahabitaciones.setGeometry(QRect(390, 10, 611, 481))
        self.textIdDelete = QLineEdit(self.centralwidget)
        self.textIdDelete.setObjectName(u"textIdDelete")
        self.textIdDelete.setGeometry(QRect(80, 560, 181, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 540, 271, 16))
        self.bt_eliminar_habitacion = QPushButton(self.centralwidget)
        self.bt_eliminar_habitacion.setObjectName(u"bt_eliminar_habitacion")
        self.bt_eliminar_habitacion.setGeometry(QRect(130, 600, 75, 24))
        self.bt_eliminar_habitacion.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.bt_actualizar_habitacion = QPushButton(self.centralwidget)
        self.bt_actualizar_habitacion.setObjectName(u"bt_actualizar_habitacion")
        self.bt_actualizar_habitacion.setGeometry(QRect(130, 460, 75, 24))
        self.bt_actualizar_habitacion.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.textUserID = QLineEdit(self.centralwidget)
        self.textUserID.setObjectName(u"textUserID")
        self.textUserID.setGeometry(QRect(240, 460, 61, 31))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 460, 21, 16))
        self.bt_atras = QPushButton(self.centralwidget)
        self.bt_atras.setObjectName(u"bt_atras")
        self.bt_atras.setGeometry(QRect(450, 610, 75, 51))
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.bt_atras.setIcon(icon)
        self.text_buscar_numero = QLineEdit(self.centralwidget)
        self.text_buscar_numero.setObjectName(u"text_buscar_numero")
        self.text_buscar_numero.setGeometry(QRect(790, 560, 181, 31))
        self.text_numero_habitacion = QLabel(self.centralwidget)
        self.text_numero_habitacion.setObjectName(u"text_numero_habitacion")
        self.text_numero_habitacion.setGeometry(QRect(780, 540, 211, 16))
        self.bt_buscar_habitacion = QPushButton(self.centralwidget)
        self.bt_buscar_habitacion.setObjectName(u"bt_buscar_habitacion")
        self.bt_buscar_habitacion.setGeometry(QRect(840, 600, 75, 24))
        self.bt_buscar_habitacion.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.comboTipo = QComboBox(self.centralwidget)
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.setObjectName(u"comboTipo")
        self.comboTipo.setGeometry(QRect(50, 250, 81, 22))
        self.disponible = QCheckBox(self.centralwidget)
        self.disponible.setObjectName(u"disponible")
        self.disponible.setGeometry(QRect(50, 370, 75, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Habitaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de habitaci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Precio por noche", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Disponible", None))
        self.bt_registrar_habitacion.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.bt_mostrar_habitaciones.setText(QCoreApplication.translate("MainWindow", u"Mostrar habitaciones", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Introduce el n\u00famero de la habitaci\u00f3n.", None))
        self.bt_eliminar_habitacion.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.bt_actualizar_habitacion.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.bt_atras.setText("")
        self.text_buscar_numero.setText("")
        self.text_numero_habitacion.setText(QCoreApplication.translate("MainWindow", u"Introduce el n\u00famero de la habitaci\u00f3n.", None))
        self.bt_buscar_habitacion.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.comboTipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Individual", None))
        self.comboTipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Doble", None))

        self.disponible.setText("")
    # retranslateUi

