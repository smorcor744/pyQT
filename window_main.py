import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import os


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "ventana_principal.ui")
        uic.loadUi(ui_file,self)
        self.setWindowTitle("Bienvenido a OMAHA")

        fondo = os.path.join(os.path.dirname(__file__), "fondo.jpg")
        fondo = fondo.replace("\\", "/")  # Asegura compatibilidad con QSS en Windows

        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet(f"""
            QMainWindow {{
                background-image: url("{fondo}");  /* Se agregan comillas */
                background-position: center;
                background-repeat: no-repeat;
            }}
        """)

        self.bt_clientes.clicked.connect(self.abrir_ventana_clientes)
        self.bt_habitaciones.clicked.connect(self.abrir_ventana_habitaciones)
        self.bt_reservas.clicked.connect(self.abrir_ventana_reservas)
        self.bt_pagos.clicked.connect(self.abrir_ventana_pagos)
        self.bt_empleados.clicked.connect(self.abrir_ventana_empleados)
        self.bt_cerrar_sesion.clicked.connect(self.cerrar_sesion)

    # Abre la ventana de clientes
    def abrir_ventana_clientes(self):
        from window_cliente import VentanaClientes
        self.window_cliente = VentanaClientes()
        self.window_cliente.show()
        self.hide()

    # Abre la ventana de habitaciones
    def abrir_ventana_habitaciones(self):
        from habitacion import VentanaHabitaciones
        self.habitacion = VentanaHabitaciones()
        self.habitacion.show()
        self.hide()

    # Abre la ventana de reservas
    def abrir_ventana_reservas(self):
        from reservas import VentanaReservas
        self.reservas = VentanaReservas()
        self.reservas.show()
        self.hide()

    # Abre la ventana de pagos
    def abrir_ventana_pagos(self):
        from pagos import VentanaPagos
        self.pagos = VentanaPagos()
        self.pagos.show()
        self.hide()

    # Abre la ventana de empleados
    def abrir_ventana_empleados(self):
        from ventana_empleado import VentanaEmpleados
        self.ventana_empleado = VentanaEmpleados()
        self.ventana_empleado.show()
        self.hide()

    # Abre la ventana de login
    def cerrar_sesion(self):
        from Login import Login
        self.Login = Login()
        self.Login.show()
        self.hide()

if __name__ == "__main__":
    

    app = QApplication(sys.argv)  # Esto debe ir al principio, antes de crear cualquier ventana

    login_window = VentanaPrincipal()  # Aquí instanciamos Login
    login_window.show()

    sys.exit(app.exec())  # Ejecuta la aplicación y entra al bucle de eventos