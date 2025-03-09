# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(475, 626)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(170, 270, 231, 41))
        font = QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet(u"password {\n"
"    background-color: black;  /* Color de fondo negro */\n"
"    color: white;             /* Color de texto blanco para contraste */\n"
"    padding: 10px;            /* Espaciado interno */\n"
"    border-radius: 5px;       /* Bordes redondeados */\n"
"    font-family: Arial, sans-serif;  /* Fuente */\n"
"    font-size: 16px;          /* Tama\u00f1o de la fuente */\n"
"    text-align: center;       /* Alinear el texto al centro */\n"
"    display: inline-block;    /* Para que el label se ajuste al contenido */\n"
"}\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 260, 141, 61))
        self.label_3.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 340, 161, 16))
        self.label_4.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 40, 131, 61))
        self.label.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\"; color: rgb(243, 243, 243)")
        self.email = QLineEdit(self.centralwidget)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(170, 170, 231, 41))
        self.email.setMaximumSize(QSize(16777215, 16777203))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setHintingPreference(QFont.PreferNoHinting)
        self.email.setFont(font1)
        self.email.setTabletTracking(False)
        self.email.setStyleSheet(u"email {\n"
"        background-color: #ffffff;\n"
"        max-width: 600px;  \n"
"        margin: 20px auto; \n"
"        padding: 20px;\n"
"        border-radius: 5px;\n"
"        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);  \n"
"    }")
        self.createaccbutton = QPushButton(self.centralwidget)
        self.createaccbutton.setObjectName(u"createaccbutton")
        self.createaccbutton.setGeometry(QRect(310, 340, 91, 21))
        self.createaccbutton.setStyleSheet(u"background-color:#363636; font-size:14px; color: rgb(230, 230, 230)")
        self.loginbutton = QPushButton(self.centralwidget)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(260, 390, 141, 41))
        self.loginbutton.setStyleSheet(u"background-color:rgb(167, 168, 167); font-size:14px")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 160, 141, 61))
        self.label_2.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"Don't have an account? ", None))
        self.label.setText(QCoreApplication.translate("Login", u"Login ", None))
        self.email.setText("")
        self.createaccbutton.setText(QCoreApplication.translate("Login", u"Click here!", None))
        self.loginbutton.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Email", None))
    # retranslateUi

