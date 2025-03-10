import sqlite3
import os

class BD_empleados():

    def _conectar(self):
        """Método privado para realizar la conexión a la base de datos."""
        bd_file = os.path.join(os.path.dirname(__file__), "hotel.db")
        return sqlite3.connect(bd_file)

    def insertar_empleado(self, nombre, apellido, cargo, email, telefono):
        """Inserta un nuevo empleado en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Insertar los datos en la base de datos
            cursor.execute('''
                INSERT INTO empleados (nombre, apellido, cargo, email, telefono) 
                VALUES (?, ?, ?, ?, ?)''',
                (nombre, apellido, cargo, email, telefono))

            conexion.commit()
            return True, "Empleado registrado correctamente."

        except sqlite3.IntegrityError:
            return False, "El email ya está registrado."
        except Exception as e:
            return False, f"Error al registrar el empleado: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def obtener_empleados(self):
        """Obtiene todos los empleados registrados en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar todos los empleados
            cursor.execute("SELECT * FROM empleados")
            empleados = cursor.fetchall()  # Obtener todos los registros

            return empleados  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener los empleados: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def buscar_empleado_por_email(self, email):
        """Busca un empleado en la base de datos por su email."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consulta SQL para buscar el empleado por email
            cursor.execute('''
                SELECT id, nombre, apellido, cargo, email, telefono
                FROM empleados
                WHERE email = ?''', (email,))

            # Obtener el resultado
            empleado = cursor.fetchone()
            return empleado  # Devuelve una tupla con los datos del empleado

        except Exception as e:
            print(f"Error al obtener el empleado: {e}")
            return None
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def eliminar_empleado(self, email):
        """Elimina un empleado de la base de datos mediante su email."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Eliminar el empleado de la base de datos
            cursor.execute("DELETE FROM empleados WHERE email = ?", (email,))
            conexion.commit()

            # Verificar si el empleado fue eliminado
            if cursor.rowcount > 0:
                return True, "Empleado eliminado correctamente."
            else:
                return False, "No se encontró un empleado con ese email."

        except Exception as e:
            return False, f"Error al eliminar el empleado: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def actualizar_empleado(self, id, nombre, apellido, cargo, email, telefono):
        """Actualiza los datos de un empleado en la base de datos mediante su ID."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Actualizar los datos del empleado
            cursor.execute('''
                UPDATE empleados
                SET nombre = ?, apellido = ?, cargo = ?, email = ?, telefono = ?
                WHERE id = ?''', (nombre, apellido, cargo, email, telefono, id))

            conexion.commit()

            # Verificar si se actualizó algún registro
            if cursor.rowcount > 0:
                return True, "Empleado actualizado correctamente."
            else:
                return False, "No se encontró un empleado con ese ID."

        except Exception as e:
            return False, f"Error al actualizar el empleado: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura