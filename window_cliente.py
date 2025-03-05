import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sqlite3
from bd_clientes import BD_clientes


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

class VentanaClientes(QMainWindow):
    def __init__(self):
        super(VentanaClientes, self).__init__()

        uic.loadUi("./registro_user.ui",self)
        self.setWindowTitle("Registro Cliente")

        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
        """)

        self.bt_registrar_cliente.clicked.connect(self.registrar_cliente)
        self.bt_mostrar_clientes.clicked.connect(self.mostrar_clientes)
        self.bt_eliminar_cliente.clicked.connect(self.eliminar_cliente)
        self.bt_actualizar_cliente.clicked.connect(self.actualizar_cliente)
        self.bt_atras.clicked.connect(self.ir_atras)

    def registrar_cliente(self):
        nombre = self.textNombre.text()
        apellido1 = self.textApellido1.text()
        apellido2 = self.textApellido2.text()
        dni = self.textDNI.text()
        email = self.textEmail.text()

        # Validar que los campos no estén vacíos
        if not (nombre and apellido1 and apellido2 and dni and email):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_clientes()
        exito, msg = bd.insertar_cliente(nombre, apellido1, apellido2, dni, email)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            # Limpiar los campos después de registrar
            self.textNombre.clear()
            self.textApellido1.clear()
            self.textApellido2.clear()
            self.textDNI.clear()
            self.textEmail.clear()
        else:
            QMessageBox.warning(self, "Error", msg)


    def mostrar_clientes(self):
        clientes = BD_clientes().obtener_clientes()

        if (clientes.__len__() == 0):
            QMessageBox.warning(self, "Advertencia", "No hay clientes registrados.")
        else:
            # Crear una tabla para mostrar los usuarios
            self.tablaClientes.setRowCount(len(clientes))  # Número de filas
            self.tablaClientes.setColumnCount(6)  # 6 columnas: id, nombre, apellido1, apellido2, dni, email

            # Configurar los encabezados de las columnas
            self.tablaClientes.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido1", "Apellido2", "Email", "DNI"])

            # Llenar la tabla con los datos de los usuarios
            for row, cliente in enumerate(clientes):
                for col, value in enumerate(cliente):
                    self.tablaClientes.setItem(row, col, QTableWidgetItem(str(value)))


    def eliminar_cliente(self):
        # Obtener el ID del usuario que se desea eliminar (puede ser desde una selección en una tabla, por ejemplo)
        cliente_id = self.textIdDelete.text()  # Suponiendo que tienes un campo de texto para ingresar el ID del usuario

        if not cliente_id.isdigit():  # Verificar que el ID ingresado sea válido
            QMessageBox.warning(self, "Error", "El ID ingresado no es válido.")
            return

        bd = BD_clientes()
        exito, msg = bd.eliminar_cliente(int(cliente_id))

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_clientes()  # Volver a cargar la lista de usuarios
        else:
            QMessageBox.warning(self, "Error", msg)
        
        self.textIdDelete.clear()


    def actualizar_cliente(self):
        # Obtener los datos del cliente (suponiendo que tienes campos de texto en la UI)
        user_id = self.textUserID.text()  # ID del usuario que deseas actualizar
        nombre = self.textNombre.text()  # Nuevo nombre
        apellido1 = self.textApellido1.text()  # Nuevo apellido
        apellido2 = self.textApellido2.text()  # Nuevo apellido
        dni = self.textDNI.text()  # Nuevo DNI
        email = self.textEmail.text()  # Nuevo email

        # Validar que los campos no estén vacíos
        if not (nombre and apellido1 and apellido2 and dni and email and user_id.isdigit()):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios y el ID debe ser válido.")
            return

        bd = BD_clientes()
        exito, msg = bd.actualizar_cliente(int(user_id), nombre, apellido1, apellido2, dni, email)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_clientes()  # Volver a cargar la lista de clientes
        else:
            QMessageBox.warning(self, "Error", msg)

    
    # Vuelve a la ventana principal
    def ir_atras(self):
        from window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.hide()


if __name__ == "__main__":
    # se ejecuta la función para crear las tablas
    ejecutar_sql()
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = VentanaClientes()
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 