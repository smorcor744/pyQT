import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sqlite3

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        uic.loadUi("./ventana_principal.ui",self)
        self.setWindowTitle("Bienvenido a OMAHA")

        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
        """)

        self.bt_clientes.clicked.connect(self.abrir_ventana_clientes)

    # Vuelve a la ventana principal
    def abrir_ventana_clientes(self):
        from window_cliente import VentanaClientes
        self.window_cliente = VentanaClientes()
        self.window_cliente.show()
        self.hide()



if __name__ == "__main__":
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = VentanaPrincipal()
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec()