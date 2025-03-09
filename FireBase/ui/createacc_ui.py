# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createacc.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 619)
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.confirmpass = QLineEdit(self.centralwidget)
        self.confirmpass.setObjectName(u"confirmpass")
        self.confirmpass.setGeometry(QRect(200, 360, 241, 41))
        font = QFont()
        font.setPointSize(12)
        self.confirmpass.setFont(font)
        self.confirmpass.setStyleSheet(u"confirmpass {\n"
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 160, 141, 61))
        self.label_2.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.email = QLineEdit(self.centralwidget)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(200, 170, 241, 41))
        self.email.setFont(font)
        self.email.setStyleSheet(u"email {\n"
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
        self.label_3.setGeometry(QRect(40, 260, 141, 61))
        self.label_3.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.signupbutton = QPushButton(self.centralwidget)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(300, 460, 141, 41))
        self.signupbutton.setStyleSheet(u"background-color:rgb(167, 168, 167); font-size:14px")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 40, 181, 61))
        self.label.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\"; color: rgb(243, 243, 243)")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 350, 171, 61))
        self.label_4.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 420, 141, 16))
        self.label_5.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.invalid = QLabel(self.centralwidget)
        self.invalid.setObjectName(u"invalid")
        self.invalid.setGeometry(QRect(200, 130, 141, 31))
        self.invalid.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.login = QPushButton(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(350, 420, 91, 21))
        self.login.setStyleSheet(u"background-color:#363636; font-size:14px; color: rgb(230, 230, 230)")
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(200, 270, 241, 41))
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
        Dialog.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Dialog)
        self.statusbar.setObjectName(u"statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"MainWindow", None))
        self.confirmpass.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.email.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.signupbutton.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Confirm Pass", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Already have an account? ", None))
        self.invalid.setText(QCoreApplication.translate("Dialog", u"Invalid email", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Click here!", None))
    # retranslateUi

