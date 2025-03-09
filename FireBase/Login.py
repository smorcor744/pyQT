from PyQt5.QtWidgets import QMessageBox, QStackedWidget
from PyQt5.uic import loadUi
from firebase_config import auth
from shared import BaseWindow


class Login(BaseWindow):
    def __init__(self, widget):
        super().__init__(widget)
        loadUi("FireBase/ui/login.ui", self)

        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(2)   
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.invalid.setVisible(False)

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
                self.invalid.setVisible(True)
                print(e)
                QMessageBox.critical(self, "Login Error", "No se a podido acceder al menú principal.")
        except:
            self.invalid.setVisible(True)
            QMessageBox.critical(self, "Login Error", "Invalid email or password. Please try again.")

    def gotocreate(self):
        from CreateAcc import CreateAcc 
        createacc = CreateAcc(self.widget)
        self.widget.addWidget(createacc)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    # Crea la instancia de QApplication
    app = QApplication(sys.argv)

    # Crea el QStackedWidget y la ventana de login
    widget = QStackedWidget()
    login_window = Login(widget)
    widget.addWidget(login_window)
    widget.show()

    # Ejecuta el bucle de eventos
    sys.exit(app.exec_())