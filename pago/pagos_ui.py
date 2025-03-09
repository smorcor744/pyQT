# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagos.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

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
        self.label.setGeometry(QRect(140, 70, 91, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 170, 51, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 300, 101, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 230, 71, 16))
        self.bt_registrar_pago = QPushButton(self.centralwidget)
        self.bt_registrar_pago.setObjectName(u"bt_registrar_pago")
        self.bt_registrar_pago.setGeometry(QRect(130, 420, 75, 24))
        self.bt_registrar_pago.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.textIdReserva = QLineEdit(self.centralwidget)
        self.textIdReserva.setObjectName(u"textIdReserva")
        self.textIdReserva.setGeometry(QRect(50, 195, 241, 31))
        self.textMonto = QLineEdit(self.centralwidget)
        self.textMonto.setObjectName(u"textMonto")
        self.textMonto.setGeometry(QRect(50, 250, 241, 31))
        self.bt_mostrar_pagos = QPushButton(self.centralwidget)
        self.bt_mostrar_pagos.setObjectName(u"bt_mostrar_pagos")
        self.bt_mostrar_pagos.setGeometry(QRect(630, 510, 121, 31))
        self.bt_mostrar_pagos.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.tablaPagos = QTableWidget(self.centralwidget)
        self.tablaPagos.setObjectName(u"tablaPagos")
        self.tablaPagos.setEnabled(True)
        self.tablaPagos.setGeometry(QRect(390, 10, 611, 481))
        self.textIdDelete = QLineEdit(self.centralwidget)
        self.textIdDelete.setObjectName(u"textIdDelete")
        self.textIdDelete.setGeometry(QRect(80, 560, 181, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 540, 141, 16))
        self.bt_eliminar_pago = QPushButton(self.centralwidget)
        self.bt_eliminar_pago.setObjectName(u"bt_eliminar_pago")
        self.bt_eliminar_pago.setGeometry(QRect(130, 600, 75, 24))
        self.bt_eliminar_pago.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.bt_actualizar_pago = QPushButton(self.centralwidget)
        self.bt_actualizar_pago.setObjectName(u"bt_actualizar_pago")
        self.bt_actualizar_pago.setGeometry(QRect(130, 460, 75, 24))
        self.bt_actualizar_pago.setStyleSheet(u"background-color: rgb(255, 170, 0);")
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
        self.text_email_cliente = QLineEdit(self.centralwidget)
        self.text_email_cliente.setObjectName(u"text_email_cliente")
        self.text_email_cliente.setGeometry(QRect(790, 560, 181, 31))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(800, 540, 161, 16))
        self.bt_buscar_pago = QPushButton(self.centralwidget)
        self.bt_buscar_pago.setObjectName(u"bt_buscar_pago")
        self.bt_buscar_pago.setGeometry(QRect(840, 600, 75, 24))
        self.bt_buscar_pago.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.comboMetodo_pago = QComboBox(self.centralwidget)
        self.comboMetodo_pago.addItem("")
        self.comboMetodo_pago.addItem("")
        self.comboMetodo_pago.setObjectName(u"comboMetodo_pago")
        self.comboMetodo_pago.setGeometry(QRect(50, 330, 81, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pagos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"idReserva", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"metodo de pago", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"monto", None))
        self.bt_registrar_pago.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.bt_mostrar_pagos.setText(QCoreApplication.translate("MainWindow", u"Mostrar pagos", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Introduce el id del pago", None))
        self.bt_eliminar_pago.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.bt_actualizar_pago.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.bt_atras.setText("")
        self.text_email_cliente.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Introduce el email del cliente", None))
        self.bt_buscar_pago.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.comboMetodo_pago.setItemText(0, QCoreApplication.translate("MainWindow", u"Tarjeta", None))
        self.comboMetodo_pago.setItemText(1, QCoreApplication.translate("MainWindow", u"Efectivo", None))

    # retranslateUi

