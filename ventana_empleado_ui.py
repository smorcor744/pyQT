# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_empleado.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1045, 731)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_borrar_empleado = QLineEdit(self.centralwidget)
        self.text_borrar_empleado.setObjectName(u"text_borrar_empleado")
        self.text_borrar_empleado.setGeometry(QRect(80, 560, 181, 31))
        self.text_telefono_empleado = QLineEdit(self.centralwidget)
        self.text_telefono_empleado.setObjectName(u"text_telefono_empleado")
        self.text_telefono_empleado.setGeometry(QRect(50, 370, 241, 31))
        self.bt_registrar_empleado = QPushButton(self.centralwidget)
        self.bt_registrar_empleado.setObjectName(u"bt_registrar_empleado")
        self.bt_registrar_empleado.setGeometry(QRect(130, 420, 75, 24))
        self.bt_registrar_empleado.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(780, 500, 161, 20))
        self.text_nombre_empleado = QLineEdit(self.centralwidget)
        self.text_nombre_empleado.setObjectName(u"text_nombre_empleado")
        self.text_nombre_empleado.setGeometry(QRect(50, 95, 241, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 540, 161, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 140, 71, 16))
        self.tabla_empleados = QTableWidget(self.centralwidget)
        self.tabla_empleados.setObjectName(u"tabla_empleados")
        self.tabla_empleados.setEnabled(True)
        self.tabla_empleados.setGeometry(QRect(390, 10, 611, 481))
        self.bt_buscar_empleado = QPushButton(self.centralwidget)
        self.bt_buscar_empleado.setObjectName(u"bt_buscar_empleado")
        self.bt_buscar_empleado.setGeometry(QRect(830, 560, 75, 24))
        self.bt_buscar_empleado.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 460, 21, 16))
        self.text_email_empleado = QLineEdit(self.centralwidget)
        self.text_email_empleado.setObjectName(u"text_email_empleado")
        self.text_email_empleado.setGeometry(QRect(50, 300, 241, 31))
        self.bt_atras = QPushButton(self.centralwidget)
        self.bt_atras.setObjectName(u"bt_atras")
        self.bt_atras.setGeometry(QRect(450, 610, 75, 51))
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.bt_atras.setIcon(icon)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 350, 71, 16))
        self.bt_eliminar_empleado = QPushButton(self.centralwidget)
        self.bt_eliminar_empleado.setObjectName(u"bt_eliminar_empleado")
        self.bt_eliminar_empleado.setGeometry(QRect(130, 600, 75, 24))
        self.bt_eliminar_empleado.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.text_id_empleado = QLineEdit(self.centralwidget)
        self.text_id_empleado.setObjectName(u"text_id_empleado")
        self.text_id_empleado.setGeometry(QRect(240, 460, 61, 31))
        self.text_email_buscar_empleado = QLineEdit(self.centralwidget)
        self.text_email_buscar_empleado.setObjectName(u"text_email_buscar_empleado")
        self.text_email_buscar_empleado.setGeometry(QRect(770, 520, 181, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 101, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.text_apellido_empleado = QLineEdit(self.centralwidget)
        self.text_apellido_empleado.setObjectName(u"text_apellido_empleado")
        self.text_apellido_empleado.setGeometry(QRect(50, 160, 241, 31))
        self.bt_actualizar_empleado = QPushButton(self.centralwidget)
        self.bt_actualizar_empleado.setObjectName(u"bt_actualizar_empleado")
        self.bt_actualizar_empleado.setGeometry(QRect(130, 460, 75, 24))
        self.bt_actualizar_empleado.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.text_cargo = QLineEdit(self.centralwidget)
        self.text_cargo.setObjectName(u"text_cargo")
        self.text_cargo.setGeometry(QRect(50, 230, 241, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 49, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 280, 71, 16))
        self.bt_mostrar_empleados = QPushButton(self.centralwidget)
        self.bt_mostrar_empleados.setObjectName(u"bt_mostrar_empleados")
        self.bt_mostrar_empleados.setGeometry(QRect(500, 510, 121, 31))
        self.bt_mostrar_empleados.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 210, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1045, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_registrar_empleado.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Introduce email del empleado", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Introduce email del empleado", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.bt_buscar_empleado.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.bt_atras.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.bt_eliminar_empleado.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EMPLEADO", None))
        self.bt_actualizar_empleado.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.bt_mostrar_empleados.setText(QCoreApplication.translate("MainWindow", u"Mostrar empleados", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
    # retranslateUi

