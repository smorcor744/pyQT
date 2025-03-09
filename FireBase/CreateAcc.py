from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from firebase_config import auth
from shared import BaseWindow

class CreateAcc(BaseWindow):
    def __init__(self, widget):
        super().__init__(widget)
        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
            }
        """)
        loadUi("FireBase/ui/createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(2)
        self.confirmpass.setEchoMode(2)
        self.login.clicked.connect(self.gotologin)
        self.invalid.setVisible(False)

    def createaccfunction(self):
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.confirmpass.text()
        if not email or not password or not confirm_password:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return
        if password != confirm_password:
            QMessageBox.warning(self, "Password Error", "Passwords do not match. Please try again.")
            return
        try:
            auth.create_user_with_email_and_password(email, password)
            QMessageBox.information(self, "Success", "Account created successfully!")
            from Login import Login  
            login = Login(self.widget)
            self.widget.addWidget(login)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        except:
            self.invalid.setVisible(True)
            QMessageBox.critical(self, "Signup Error", "Failed to create account. Please try again.")

    def gotologin(self):
        from Login import Login  
        login = Login(self.widget)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)