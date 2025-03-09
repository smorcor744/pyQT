import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import os

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

         # Obtener la ruta correcta al archivo .ui
        ui_file = self.get_ui_path("principal/ventana_principal.ui")

        # Cargar el archivo .ui
        uic.loadUi(ui_file, self)

        # Obtener la ruta correcta a la imagen de fondo
        fondo_path = self.get_ui_path("fondo.jpg")

        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet(f"""
            QMainWindow {{
                background-image: url({fondo_path});
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

    def get_ui_path(self, relative_path):
        """
        Obtiene la ruta absoluta al archivo .ui, teniendo en cuenta si el programa
        está empaquetado con PyInstaller o no.
        """
        if getattr(sys, 'frozen', False):
            # Si está empaquetado con PyInstaller
            base_dir = sys._MEIPASS
        else:
            # Si se está ejecutando desde el código fuente
            base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta completa al archivo .ui
        return os.path.join(base_dir, relative_path)

    # Abre la ventana de clientes
    def abrir_ventana_clientes(self):
        from cliente.window_cliente import VentanaClientes
        self.window_cliente = VentanaClientes()
        self.window_cliente.show()
        self.hide()

    # Abre la ventana de habitaciones
    def abrir_ventana_habitaciones(self):
        from habitacion.habitacion import VentanaHabitaciones
        self.habitacion = VentanaHabitaciones()
        self.habitacion.show()
        self.hide()

    # Abre la ventana de reservas
    def abrir_ventana_reservas(self):
        from reserva.reservas import VentanaReservas
        self.reservas = VentanaReservas()
        self.reservas.show()
        self.hide()

    # Abre la ventana de pagos
    def abrir_ventana_pagos(self):
        from pago.pagos import VentanaPagos
        self.pagos = VentanaPagos()
        self.pagos.show()
        self.hide()

    # Abre la ventana de empleados
    def abrir_ventana_empleados(self):
        from empleado.ventana_empleado import VentanaEmpleados
        self.ventana_empleado = VentanaEmpleados()
        self.ventana_empleado.show()
        self.hide()

    # Abre la ventana de login
    def cerrar_sesion(self):
        from FireBase.Login import Login
        self.Login = Login()
        self.Login.show()
        self.hide()

if __name__ == "__main__":
    

    app = QApplication(sys.argv)  # Esto debe ir al principio, antes de crear cualquier ventana

    login_window = VentanaPrincipal()  # Aquí instanciamos Login
    login_window.show()

    sys.exit(app.exec())  # Ejecuta la aplicación y entra al bucle de eventos