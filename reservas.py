import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sqlite3
from BD_reservas import BD_reservas

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

class VentanaReservas(QMainWindow):
    def __init__(self):
        super(VentanaReservas, self).__init__()

        uic.loadUi("./reservas.ui", self)
        self.setWindowTitle("Registro de Reservas")

        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
        """)

        # Conectar botones a funciones
        self.bt_registrar_reserva.clicked.connect(self.registrar_reserva)
        self.bt_mostrar_reservas.clicked.connect(self.mostrar_reservas)
        self.bt_eliminar_reservas.clicked.connect(self.eliminar_reserva)
        self.bt_actualizar_reserva.clicked.connect(self.actualizar_reserva)
        self.bt_atras.clicked.connect(self.ir_atras)

        # Agregar opciones al QComboBox de estado
        self.comboEstado.addItems(["Pendiente", "Confirmada", "Cancelada", "Finalizada"])

    def registrar_reserva(self):
        email_cliente = self.textEmail.text()
        numero_habitacion = self.textNumero_habitacion.text()
        fecha_checkin = self.checkIn.text()
        fecha_checkout = self.checkOut.text()
        estado = self.comboEstado.currentText()  # Obtiene el estado seleccionado

        if not (email_cliente and numero_habitacion and fecha_checkin and fecha_checkout):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_reservas()
        exito, msg = bd.insertar_reserva(email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.textEmail.clear()
            self.textNumero_habitacion.clear()
            self.textFechaCheckin.clear()
            self.textFechaCheckout.clear()
            self.comboEstado.setCurrentIndex(0)  # Reiniciar selección
        else:
            QMessageBox.warning(self, "Error", msg)

    def mostrar_reservas(self):
        reservas = BD_reservas().obtener_reservas()

        if len(reservas) == 0:
            QMessageBox.warning(self, "Advertencia", "No hay reservas registradas.")
        else:
            self.tablaReservas.setRowCount(len(reservas))
            self.tablaReservas.setColumnCount(5)
            self.tablaReservas.setHorizontalHeaderLabels(["ID", "Email Cliente", "N° Habitación", "Check-in", "Check-out", "Estado"])

            for row, reserva in enumerate(reservas):
                for col, value in enumerate(reserva):
                    self.tablaReservas.setItem(row, col, QTableWidgetItem(str(value)))

    def eliminar_reserva(self):
        email_cliente = self.textEmailDelete.text()

        if not email_cliente:
            QMessageBox.warning(self, "Error", "Debe ingresar un email válido.")
            return

        bd = BD_reservas()
        exito, msg = bd.eliminar_reserva(email_cliente)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_reservas()
        else:
            QMessageBox.warning(self, "Error", msg)

        self.textEmailDelete.clear()

    def actualizar_reserva(self):
        email_cliente = self.textEmailUpdate.text()
        numero_habitacion = self.textHabitacionUpdate.text()
        fecha_checkin = self.textFechaCheckinUpdate.text()
        fecha_checkout = self.textFechaCheckoutUpdate.text()
        estado = self.comboEstado.currentText()  # Obtiene el estado actualizado

        if not (email_cliente and numero_habitacion and fecha_checkin and fecha_checkout):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_reservas()
        exito, msg = bd.actualizar_reserva(email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_reservas()
        else:
            QMessageBox.warning(self, "Error", msg)

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
