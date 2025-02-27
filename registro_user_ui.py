# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_user.ui'
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
        MainWindow.resize(1015, 724)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 81, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 150, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 230, 71, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 390, 71, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 310, 71, 16))
        self.bt_registrar = QPushButton(self.centralwidget)
        self.bt_registrar.setObjectName(u"bt_registrar")
        self.bt_registrar.setGeometry(QRect(120, 480, 75, 24))
        self.textNombre = QLineEdit(self.centralwidget)
        self.textNombre.setObjectName(u"textNombre")
        self.textNombre.setGeometry(QRect(50, 95, 241, 31))
        self.textApellido1 = QLineEdit(self.centralwidget)
        self.textApellido1.setObjectName(u"textApellido1")
        self.textApellido1.setGeometry(QRect(50, 180, 241, 31))
        self.textApellido2 = QLineEdit(self.centralwidget)
        self.textApellido2.setObjectName(u"textApellido2")
        self.textApellido2.setGeometry(QRect(50, 250, 241, 31))
        self.textDNI = QLineEdit(self.centralwidget)
        self.textDNI.setObjectName(u"textDNI")
        self.textDNI.setGeometry(QRect(50, 330, 241, 31))
        self.textEmail = QLineEdit(self.centralwidget)
        self.textEmail.setObjectName(u"textEmail")
        self.textEmail.setGeometry(QRect(50, 410, 241, 31))
        self.bt_mostrar_usuarios = QPushButton(self.centralwidget)
        self.bt_mostrar_usuarios.setObjectName(u"bt_mostrar_usuarios")
        self.bt_mostrar_usuarios.setGeometry(QRect(630, 510, 121, 31))
        self.tablaUsuarios = QTableWidget(self.centralwidget)
        self.tablaUsuarios.setObjectName(u"tablaUsuarios")
        self.tablaUsuarios.setEnabled(True)
        self.tablaUsuarios.setGeometry(QRect(390, 10, 611, 481))
        self.textIdDelete = QLineEdit(self.centralwidget)
        self.textIdDelete.setObjectName(u"textIdDelete")
        self.textIdDelete.setGeometry(QRect(270, 570, 181, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 550, 141, 16))
        self.bt_eliminar_cliente = QPushButton(self.centralwidget)
        self.bt_eliminar_cliente.setObjectName(u"bt_eliminar_cliente")
        self.bt_eliminar_cliente.setGeometry(QRect(320, 620, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1015, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apellido 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apellido 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.bt_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.bt_mostrar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Mostrar usuarios", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Introduce la ID del cliente", None))
        self.bt_eliminar_cliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

