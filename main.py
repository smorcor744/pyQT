import sys
import sqlite3
from PyQt6.QtWidgets import QApplication
from FireBase.firebase_config import auth
from FireBase.Login import Login  # Importa la ventana de login

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

if __name__ == "__main__":

    ejecutar_sql()
    # Se crea la instancia de la aplicación
    app = QApplication(sys.argv)

    # Se crea la instancia de la ventana de login
    login_window = Login()

    # Se muestra la ventana de login
    login_window.show()

    # Se entrega el control al sistema operativo
    sys.exit(app.exec())