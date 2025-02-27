import sqlite3

class Base_de_datos():

    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name

    def _conectar(self):
        """Método privado para realizar la conexión a la base de datos."""
        return sqlite3.connect(self.db_name)

    def insertar_usuario(self, nombre, apellido1, apellido2, dni, email):
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Insertar los datos en la base de datos
            cursor.execute('''
                INSERT INTO clientes (nombre, apellido1, apellido2, dni, email) 
                VALUES (?, ?, ?, ?, ?)''',
                (nombre, apellido1, apellido2, dni, email))

            conexion.commit()
            conexion.close()

            return True, "Cliente registrado correctamente."

        except sqlite3.IntegrityError:
            return (False, "El DNI o email ya está registrado.")
        except Exception as e:
            return (False, f"Error al registrar el cliente: {e}")
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

        
    def obtener_usuarios(self):
        """Obtiene todos los clientes registrados en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar todos los usuarios
            cursor.execute("SELECT * FROM clientes")
            usuarios = cursor.fetchall()  # Obtener todos los registros

            return usuarios  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener los clientes: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def eliminar_usuario(self, user_id):
        """Elimina un usuario de la base de datos mediante su ID."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Eliminar el usuario de la base de datos
            cursor.execute("DELETE FROM clientes WHERE id = ?", (user_id,))
            conexion.commit()

            # Verificar si el usuario fue eliminado
            if cursor.rowcount > 0:
                return True, "Usuario eliminado correctamente."
            else:
                return False, "No se encontró un usuario con ese ID."

        except Exception as e:
            return False, f"Error al eliminar el usuario: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura