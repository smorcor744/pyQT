import sqlite3

class BD_pagos():

    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name

    def _conectar(self):
        """Método privado para realizar la conexión a la base de datos."""
        return sqlite3.connect(self.db_name)
    
    def insertar_pago(self, id_reserva, monto, metodo_pago, fecha_pago):
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Insertar los datos en la base de datos
            cursor.execute('''
                INSERT INTO pagos (id_reserva, monto, metodo_pago, fecha_pago) 
                VALUES (?, ?, ?, ?, ?)''',
                (id_reserva, monto, metodo_pago, fecha_pago))

            conexion.commit()
            conexion.close()

            return True, "Pago registrado correctamente."

        except sqlite3.IntegrityError:
            return (False, "El pago ya está registrado.")
        except Exception as e:
            return (False, f"Error al registrar el pago: {e}")
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

        
    def obtener_pagos(self):
        """Obtiene todos los pagos registrados en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Consultar todos los pagos
            cursor.execute("SELECT * FROM pagos")
            pagos = cursor.fetchall()  # Obtener todos los registros

            return pagos  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener los pagos: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def obtener_pagos_por_email(self, email):
        """Obtiene los pagos registrados de un cliente meidante su email en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            query = """
            SELECT 
                p.id AS pago_id,
                p.monto,
                p.metodo_pago,
                p.fecha_pago,
                r.id AS reserva_id,
                r.estado AS estado_reserva,
                c.email
            FROM 
                pagos p
            JOIN 
                reservas r ON p.id_reserva = r.id
            JOIN 
                clientes c ON r.email_cliente = c.email
            WHERE 
                c.email = ?
            """

            # Consultar los pagos que ha realizado un cliente
            cursor.execute(query, (email))
            pagos = cursor.fetchall()  # Obtener todos los registros

            return pagos  # Devolver los resultados

        except Exception as e:
            print(f"Error al obtener los pagos: {e}")
            return []
        finally:
            conexion.close()  # Cerrar la conexión de manera segura

    def eliminar_pago(self, id):
        """Elimina un pago de la base de datos mediante el id del pago."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Eliminar el usuario de la base de datos
            cursor.execute("DELETE FROM pagos WHERE id = ?", (id))
            conexion.commit()

            # Verificar si la reserva fue eliminada
            if cursor.rowcount > 0:
                return True, "Pago eliminado correctamente."
            else:
                return False, "No se encontró un pago con ese ID."

        except Exception as e:
            return False, f"Error al eliminarel pago: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura


    def actualizar_pago(self, id, id_reserva, monto, metodo_pago, fecha_pago):
        """Actualiza los datos de un pago en la base de datos."""
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()

            # Actualizar los datos del pago
            cursor.execute('''
                UPDATE pagos
                SET id_reserva = ?, monto = ?, metodo_pago = ?, fecha_pago = ?
                WHERE id = ?''', (id_reserva, monto, metodo_pago, fecha_pago, id))

            conexion.commit()

            # Verificar si se actualizó algún registro
            if cursor.rowcount > 0:
                return True, "Pago actualizado correctamente."
            else:
                return False, "No se encontró un pago con ese ID."

        except Exception as e:
            return False, f"Error al actualizar lel pago: {e}"
        finally:
            conexion.close()  # Cerrar la conexión de manera segura