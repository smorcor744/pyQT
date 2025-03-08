import sqlite3

class BD_clientes():

    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name

    def _conectar(self):
        """Método privado para realizar la conexión a la base de datos."""
        return sqlite3.connect(self.db_name)

    def insertar_cliente(self, nombre, apellido1, apellido2, dni, email):
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

        
    def obtener_clientes(self):
        """Obtiene todos los clientes registrados en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar todos los usuarios
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()  # Obtener todos los registros

            return clientes  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener los clientes: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def buscar_cliente_por_email(self, email):
        """Busca un cliente en la base de datos por su email."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consulta SQL para buscar el cliente por email
            cursor.execute('''
                SELECT id, nombre, apellido1, apellido2, email, dni
                FROM clientes
                WHERE email = ?''', (email,))

            # Obtener el resultado
            cliente = cursor.fetchone()
            return cliente
            
        except Exception as e:
            print(f"Error al obtener el cliente: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def eliminar_cliente(self, email):
        """Elimina un usuario de la base de datos mediante su ID."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Eliminar el usuario de la base de datos
            cursor.execute("DELETE FROM clientes WHERE email = ?", (email))
            conexion.commit()

            # Verificar si el usuario fue eliminado
            if cursor.rowcount > 0:
                return True, "Cliente eliminado correctamente."
            else:
                return False, "No se encontró un cliente con ese ID."

        except Exception as e:
            return False, f"Error al eliminar el cliente: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura


    def actualizar_cliente(self, user_id, nombre, apellido1, apellido2, dni, email):
        """Actualiza los datos de un usuario en la base de datos mediante su ID."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Actualizar los datos del usuario
            cursor.execute('''
                UPDATE clientes
                SET nombre = ?, apellido1 = ?, apellido2 = ?, dni = ?, email = ?
                WHERE id = ?''', (nombre, apellido1, apellido2, dni, email, user_id))

            conexion.commit()

            # Verificar si se actualizó algún registro
            if cursor.rowcount > 0:
                return True, "Cliente actualizado correctamente."
            else:
                return False, "No se encontró un cliente con ese ID."

        except Exception as e:
            return False, f"Error al actualizar el cliente: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura


