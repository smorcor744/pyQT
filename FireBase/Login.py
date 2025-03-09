import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from firebase_config import auth

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("FireBase/ui/login.ui", self)
        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
            }
        """)        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
            }
        """)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(2)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        if not email or not password:
            QMessageBox.warning(self, "Input Error", "Please enter both email and password.")
            return
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            QMessageBox.information(self, "Success", f"Welcome {user['email']}!")
            try:
                from principal.window_main import VentanaPrincipal
                self.window_main = VentanaPrincipal()
                self.window_main.show()
                self.hide()
            except Exception as e:
                print(e)
                QMessageBox.critical(self, "Login Error", "No se hha podido acceder al menú principal.")
        except:
            self.invalid.setVisible(True)
            QMessageBox.critical(self, "Login Error", "Invalid email or password. Please try again.")

    def gotocreate(self):
        self.createacc = CreateAcc()
        self.createacc.show()
        self.hide()

class CreateAcc(QMainWindow):
    def __init__(self):
        super().__init__()
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
            self.login = Login()
            self.login.show()
            self.hide()
        except:
            QMessageBox.critical(self, "Signup Error", "Failed to create account. Please try again.")

    def gotologin(self):
        self.login = Login()
        self.login.show()
        self.hide()
        self.createacc = CreateAcc()
        self.createacc.show()
        self.hide()

class CreateAcc(QMainWindow):
    def __init__(self):
        super().__init__()
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
            self.login = Login()
            self.login.show()
            self.hide()
        except:
            QMessageBox.critical(self, "Signup Error", "Failed to create account. Please try again.")

    def gotologin(self):
        self.login = Login()
        self.login.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec())