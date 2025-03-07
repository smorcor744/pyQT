import sqlite3

class BD_reservas():

    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name

    def _conectar(self):
        """Método privado para realizar la conexión a la base de datos."""
        return sqlite3.connect(self.db_name)
    
    def insertar_reserva(self, email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado):
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Insertar los datos en la base de datos
            cursor.execute('''
                INSERT INTO reservas (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado) 
                VALUES (?, ?, ?, ?, ?)''',
                (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado))

            conexion.commit()
            conexion.close()

            return True, "Reserva registrada correctamente."

        except sqlite3.IntegrityError:
            return (False, "La habitación ya está registrada.")
        except Exception as e:
            return (False, f"Error al registrar la reserva: {e}")
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

        
    def obtener_reservas(self):
        """Obtiene todos las reservas registradas en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar todas las reservas
            cursor.execute("SELECT * FROM reservas")
            reservas = cursor.fetchall()  # Obtener todos los registros

            return reservas  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener las reservas: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def obtener_reservas_por_email(self, email):
        """Obtiene las reservas registradas de un cliente en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar todas las reservas
            cursor.execute("SELECT * FROM reservas WHERE email_cliente = ?", (email))
            reservas = cursor.fetchall()  # Obtener todos los registros

            return reservas  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener las reservas: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def eliminar_reserva(self, email_cliente):
        """Elimina una reserva de la base de datos mediante el email del cliente."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Eliminar el usuario de la base de datos
            cursor.execute("DELETE FROM reservas WHERE email_cliente = ?", (email_cliente))
            conexion.commit()

            # Verificar si la reserva fue eliminada
            if cursor.rowcount > 0:
                return True, "Reserva eliminada correctamente."
            else:
                return False, "No se encontró una reserva con ese EMAIL."

        except Exception as e:
            return False, f"Error al eliminar la reserva: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura


    def actualizar_reserva(self, email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado):
        """Actualiza los datos de una reserva en la base de datos mediante el email del cliente."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Actualizar los datos de la reserva
            cursor.execute('''
                UPDATE reservas
                SET email_cliente = ?, numero_habitacion = ?, fecha_checkin = ?, fecha_checkout = ?, estado = ?
                WHERE email_cliente = ?''', (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado))

            conexion.commit()

            # Verificar si se actualizó algún registro
            if cursor.rowcount > 0:
                return True, "Reserva actualizada correctamente."
            else:
                return False, "No se encontró una reserva con ese EMAIL."

        except Exception as e:
            return False, f"Error al actualizar la reserva: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura