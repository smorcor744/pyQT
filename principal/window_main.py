import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        uic.loadUi("./principal/ventana_principal.ui",self)
        self.setWindowTitle("Bienvenido a OMAHA")

        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
            }
        """)

        self.bt_clientes.clicked.connect(self.abrir_ventana_clientes)
        self.bt_habitaciones.clicked.connect(self.abrir_ventana_habitaciones)
        self.bt_reservas.clicked.connect(self.abrir_ventana_reservas)
        self.bt_pagos.clicked.connect(self.abrir_ventana_pagos)
        self.bt_empleados.clicked.connect(self.abrir_ventana_empleados)
        self.bt_cerrar_sesion.clicked.connect(self.cerrar_sesion)

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
