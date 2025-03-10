import sqlite3

class BD_habitaciones():

    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name

    def _conectar(self):
        """Método privado para realizar la conexión a la base de datos."""
        return sqlite3.connect(self.db_name)

    def insertar_habitacion(self, numero, tipo, precio_noche, disponible):
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Insertar los datos en la base de datos
            cursor.execute('''
                INSERT INTO habitaciones (numero, tipo, precio_noche, disponible) 
                VALUES (?, ?, ?, ?)''',
                (numero, tipo, precio_noche, disponible))

            conexion.commit()
            conexion.close()

            return True, "Habitación registrado correctamente."

        except sqlite3.IntegrityError:
            return (False, "La habitación ya está registrado.")
        except Exception as e:
            return (False, f"Error al registrar la habitación: {e}")
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

        
    def obtener_habitaciones(self):
        """Obtiene todas las habitaciones registradas en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar todos las habitaciones
            cursor.execute("SELECT * FROM habitaciones")
            habitaciones = cursor.fetchall()  # Obtener todos los registros

            return habitaciones  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener las habitaciones: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def buscar_habitacion_por_numero(self, numero):
        """Obtiene la habitación registrada en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar la  habitacion
            cursor.execute("SELECT * FROM habitaciones WHERE numero = ?", (numero,))
            habitacion = cursor.fetchone()  # Obtener todos los registros

            return habitacion  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener las habitaciones: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def eliminar_habitacion(self, numero):
        """Elimina una habitacion de la base de datos mediante su ID."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Eliminar el usuario de la base de datos
            cursor.execute("DELETE FROM habitaciones WHERE numero = ?", (numero,))
            conexion.commit()

            # Verificar si el usuario fue eliminado
            if cursor.rowcount > 0:
                return True, "Habitación eliminada correctamente."
            else:
                return False, "No se encontró una habitación con ese número."

        except Exception as e:
            return False, f"Error al eliminar la habitación: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura


    def actualizar_habitacion(self, numero, disponible):
        """Actualiza los datos de una habitación en la base de datos mediante su NÚMERO."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consulta SQL para actualizar la disponibilidad de la habitación
            query = '''
                UPDATE habitaciones
                SET disponible = ?
                WHERE numero = ?
            '''

            # Actualizar los datos del usuario
            cursor.execute(query, (disponible, numero))
            conexion.commit()

            # Verificar si se actualizó algún registro
            if cursor.rowcount > 0:
                return True, "Habitación actualizada correctamente."
            else:
                return False, "No se encontró una habitación con ese NÚMERO."

        except Exception as e:
            return False, f"Error al actualizar la habitación: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura