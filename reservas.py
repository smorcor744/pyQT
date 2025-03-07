import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sqlite3
from BD_reservas import BD_reservas

def ejecutar_sql():
    """Ejecuta el archivo .sql que contiene las instrucciones de creación de tablas para reservas."""
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

class VentanaReservas(QMainWindow):
    def __init__(self):
        super(VentanaReservas, self).__init__()

        uic.loadUi("./reservas.ui", self)
        self.setWindowTitle("Gestión de Reservas")

        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
        """)

        self.bt_registrar_reserva.clicked.connect(self.registrar_reserva)
        self.bt_mostrar_reservas.clicked.connect(self.mostrar_reservas)
        self.bt_eliminar_reservas.clicked.connect(self.eliminar_reserva)
        self.bt_actualizar_reserva.clicked.connect(self.actualizar_reserva)
        self.bt_buscar_reserva.clicked.connect(self.buscar_reserva)
        self.bt_atras.clicked.connect(self.ir_atras)

    def registrar_reserva(self):
        email = self.textEmail.text()
        numero_habitacion = self.textNumero.text()
        checkin = self.checkIn.date().toString("yyyy-MM-dd")
        checkout = self.checkOut.date().toString("yyyy-MM-dd")
        estado = self.textDisponible.text()

        if not (email and numero_habitacion and checkin and checkout and estado):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_reservas()
        exito, msg = bd.insertar_reserva(email, numero_habitacion, checkin, checkout, estado)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.textEmail.clear()
            self.textNumero.clear()
            self.textDisponible.clear()
        else:
            QMessageBox.warning(self, "Error", msg)

    def mostrar_reservas(self):
        reservas = BD_reservas().obtener_reservas()

        if len(reservas) == 0:
            QMessageBox.warning(self, "Advertencia", "No hay reservas registradas.")
        else:
            self.tablaReservas.setRowCount(len(reservas))
            self.tablaReservas.setColumnCount(5)
            self.tablaReservas.setHorizontalHeaderLabels(["ID", "Email", "Habitación", "Check-in", "Check-out", "Estado"])

            for row, reserva in enumerate(reservas):
                for col, value in enumerate(reserva):
                    self.tablaReservas.setItem(row, col, QTableWidgetItem(str(value)))

    def eliminar_reserva(self):
        email = self.textIdDelete.text()

        if not email:
            QMessageBox.warning(self, "Error", "Debe ingresar un email válido.")
            return

        bd = BD_reservas()
        exito, msg = bd.eliminar_reserva(email)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_reservas()
        else:
            QMessageBox.warning(self, "Error", msg)

        self.textIdDelete.clear()

    def actualizar_reserva(self):
        email = self.textUserID.text()
        numero_habitacion = self.textNumero.text()
        checkin = self.checkIn.date().toString("yyyy-MM-dd")
        checkout = self.checkOut.date().toString("yyyy-MM-dd")
        estado = self.textDisponible.text()

        if not (email and numero_habitacion and checkin and checkout and estado):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_reservas()
        exito, msg = bd.actualizar_reserva(email, numero_habitacion, checkin, checkout, estado)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_reservas()
        else:
            QMessageBox.warning(self, "Error", msg)

    def buscar_reserva(self):
        email = self.textIdBuscar.text()

        if not email:
            QMessageBox.warning(self, "Error", "Debe ingresar un email válido.")
            return

        reservas = BD_reservas().obtener_reservas_por_email(email)

        if len(reservas) == 0:
            QMessageBox.warning(self, "Advertencia", "No se encontraron reservas con ese email.")
        else:
            self.tablaReservas.setRowCount(len(reservas))
            self.tablaReservas.setColumnCount(5)
            self.tablaReservas.setHorizontalHeaderLabels(["ID", "Email", "Habitación", "Check-in", "Check-out", "Estado"])

            for row, reserva in enumerate(reservas):
                for col, value in enumerate(reserva):
                    self.tablaReservas.setItem(row, col, QTableWidgetItem(str(value)))

    def ir_atras(self):
        from window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.hide()

if __name__ == "__main__":
    ejecutar_sql()
    app = QApplication(sys.argv)
    window = VentanaReservas()
    window.show()
    app.exec()
