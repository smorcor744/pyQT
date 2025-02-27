import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sqlite3
from bd import Base_de_datos


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

class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()

        uic.loadUi("C:/Users/Sebas/DAM_2/Desarrollo_de_interfaces/pyQT-1/registro_user.ui",self)
        self.setWindowTitle("Registro Cliente")

        self.bt_registrar.clicked.connect(self.registrar)
        self.bt_mostrar_usuarios.clicked.connect(self.mostrarUsuarios)
        self.bt_eliminar_cliente.clicked.connect(self.eliminarUsuario)

    def registrar(self):
        nombre = self.textNombre.text()
        apellido1 = self.textApellido1.text()
        apellido2 = self.textApellido2.text()
        dni = self.textDNI.text()
        email = self.textEmail.text()

        # Validar que los campos no estén vacíos
        if not (nombre and apellido1 and apellido2 and dni and email):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = Base_de_datos()
        exito, msg = bd.insertar_usuario(nombre, apellido1, apellido2, dni, email)

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


    def mostrarUsuarios(self):
        usuarios = Base_de_datos().obtener_usuarios()

        if (usuarios.__len__() == 0):
            QMessageBox.warning(self, "No hay usuarios registrados.")
        else:
            # Crear una tabla para mostrar los usuarios
            self.tablaUsuarios.setRowCount(len(usuarios))  # Número de filas
            self.tablaUsuarios.setColumnCount(6)  # 6 columnas: id, nombre, apellido1, apellido2, dni, email

            # Configurar los encabezados de las columnas
            self.tablaUsuarios.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido1", "Apellido2", "Email", "DNI"])

            # Llenar la tabla con los datos de los usuarios
            for row, usuario in enumerate(usuarios):
                for col, value in enumerate(usuario):
                    self.tablaUsuarios.setItem(row, col, QTableWidgetItem(str(value)))


    def eliminarUsuario(self):
        # Obtener el ID del usuario que se desea eliminar (puede ser desde una selección en una tabla, por ejemplo)
        user_id = self.textIdDelete.text()  # Suponiendo que tienes un campo de texto para ingresar el ID del usuario

        if not user_id.isdigit():  # Verificar que el ID ingresado sea válido
            QMessageBox.warning(self, "Error", "El ID ingresado no es válido.")
            return

        bd = Base_de_datos()
        exito, msg = bd.eliminar_usuario(int(user_id))

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrarUsuarios()  # Volver a cargar la lista de usuarios
        else:
            QMessageBox.warning(self, "Error", msg)


if __name__ == "__main__":
    # se ejecuta la función para crear las tablas
    ejecutar_sql()
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = Ventana()
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 