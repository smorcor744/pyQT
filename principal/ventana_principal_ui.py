# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 615)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(750, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 130, 131, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_clientes = QPushButton(self.verticalLayoutWidget)
        self.bt_clientes.setObjectName(u"bt_clientes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_clientes.sizePolicy().hasHeightForWidth())
        self.bt_clientes.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.bt_clientes)

        self.bt_habitaciones = QPushButton(self.verticalLayoutWidget)
        self.bt_habitaciones.setObjectName(u"bt_habitaciones")
        sizePolicy1.setHeightForWidth(self.bt_habitaciones.sizePolicy().hasHeightForWidth())
        self.bt_habitaciones.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.bt_habitaciones)

        self.bt_reservas = QPushButton(self.verticalLayoutWidget)
        self.bt_reservas.setObjectName(u"bt_reservas")
        sizePolicy1.setHeightForWidth(self.bt_reservas.sizePolicy().hasHeightForWidth())
        self.bt_reservas.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.bt_reservas)

        self.bt_pagos = QPushButton(self.verticalLayoutWidget)
        self.bt_pagos.setObjectName(u"bt_pagos")
        sizePolicy1.setHeightForWidth(self.bt_pagos.sizePolicy().hasHeightForWidth())
        self.bt_pagos.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.bt_pagos)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 10, 451, 91))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.bt_empleados = QPushButton(self.centralwidget)
        self.bt_empleados.setObjectName(u"bt_empleados")
        self.bt_empleados.setGeometry(QRect(590, 130, 129, 69))
        sizePolicy1.setHeightForWidth(self.bt_empleados.sizePolicy().hasHeightForWidth())
        self.bt_empleados.setSizePolicy(sizePolicy1)
        self.bt_cerrar_sesion = QPushButton(self.centralwidget)
        self.bt_cerrar_sesion.setObjectName(u"bt_cerrar_sesion")
        self.bt_cerrar_sesion.setGeometry(QRect(370, 490, 101, 41))
        sizePolicy1.setHeightForWidth(self.bt_cerrar_sesion.sizePolicy().hasHeightForWidth())
        self.bt_cerrar_sesion.setSizePolicy(sizePolicy1)
        self.bt_cerrar_sesion.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_clientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.bt_habitaciones.setText(QCoreApplication.translate("MainWindow", u"HABITACIONES", None))
        self.bt_reservas.setText(QCoreApplication.translate("MainWindow", u"RESERVAS", None))
        self.bt_pagos.setText(QCoreApplication.translate("MainWindow", u"PAGOS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BIENVENIDO A HOTEL OMAHA", None))
        self.bt_empleados.setText(QCoreApplication.translate("MainWindow", u"EMPLEADOS", None))
        self.bt_cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
    # retranslateUi

