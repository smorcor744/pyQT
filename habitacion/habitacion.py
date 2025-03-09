import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
from bd.bd_habitaciones import BD_habitaciones

class VentanaHabitaciones(QMainWindow):
    def __init__(self):
        super(VentanaHabitaciones, self).__init__()

        uic.loadUi("./habitacion/habitacion.ui", self)
        self.setWindowTitle("Registro de Habitaciones")

        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
            }
        """)

        # Conectar botones con funciones
        self.bt_registrar_habitacion.clicked.connect(self.registrar_habitacion)
        self.bt_mostrar_habitaciones.clicked.connect(self.mostrar_habitaciones)
        self.bt_eliminar_habitacion.clicked.connect(self.eliminar_habitacion)
        self.bt_actualizar_habitacion.clicked.connect(self.actualizar_habitacion)
        self.bt_atras.clicked.connect(self.ir_atras)

    # AHORA LOS MÉTODOS ESTÁN DENTRO DE LA CLASE
    def registrar_habitacion(self):
        numero = self.textNumero.text()
        tipo = self.comboTipo.currentText()
        precio_noche = self.textprecio_noche.text()
        disponible = self.disponible.isChecked()

        if not (numero and tipo and precio_noche):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        
        bd = BD_habitaciones()
        exito, msg = bd.insertar_habitacion(numero, tipo, precio_noche, disponible)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.textNumero.clear()
            self.comboTipo.setCurrentIndex(0)
            self.textprecio_noche.clear()
            self.disponible.setChecked(False)
        else:
            QMessageBox.warning(self, "Error", msg)

    def mostrar_habitaciones(self):
        habitaciones = BD_habitaciones().obtener_habitacion()

        if len(habitaciones) == 0:
            QMessageBox.warning(self, "Advertencia", "No hay habitaciones registradas.")
        else:
            self.tablahabitaciones.setRowCount(len(habitaciones))
            self.tablahabitaciones.setColumnCount(5)
            self.tablahabitaciones.setHorizontalHeaderLabels(["Número", "Precio por Noche","Tipo" , "Disponible"])

            for row, habitacion in enumerate(habitaciones):
             for col, value in enumerate(habitacion):
                if col == 3:  # Suponiendo que "disponible" está en la columna 3
                 value = "Sí" if int(value) == 1 else "No"
                self.tablahabitaciones.setItem(row, col, QTableWidgetItem(str(value)))


    def eliminar_habitacion(self):
        numero = self.textIdDelete.text()

        if not numero.isdigit():
            QMessageBox.warning(self, "Error", "El número ingresado no es válido.")
            return

        bd = BD_habitaciones()
        exito, msg = bd.eliminar_habitacion(int(numero))

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_habitaciones()
        else:
            QMessageBox.warning(self, "Error", msg)

        self.textIdDelete.clear()

    def actualizar_habitacion(self):
        numero = self.textUserID.text()
        disponible = self.textDisponible.text()

        if not (numero.isdigit() and disponible):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios y el número debe ser válido.")
            return

        bd = BD_habitaciones()
        exito, msg = bd.actualizar_habitacion(int(numero), disponible)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_habitaciones()
        else:
            QMessageBox.warning(self, "Error", msg)

    def ir_atras(self):
        from principal.window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaHabitaciones()
    window.show()
    app.exec()
