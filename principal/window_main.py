import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sqlite3

def ejecutar_sql():
    """Ejecuta el archivo .sql que contiene las instrucciones de creación de tablas."""
    try:
        with open("hotel.sql", "r") as archivo_sql:
            sql_script = archivo_sql.read()

        conexion = sqlite3.connect('hotel.db')
        cursor = conexion.cursor()
        cursor.executescript(sql_script)
        conexion.commit()
        conexion.close()
        print("Base de datos configurada correctamente.")
    except Exception as e:
        print(f"Error al ejecutar el script SQL: {e}")

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
        self.ventana_empleado = Login()
        self.ventana_empleado.show()
        self.hide()



if __name__ == "__main__":
    # se ejecuta la función para crear las tablas
    ejecutar_sql()
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = VentanaPrincipal()
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec()