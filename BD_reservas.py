import sqlite3

class BD_reservas:
    def __init__(self):
        self.conexion = sqlite3.connect('hotel.db')
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_cliente TEXT NOT NULL,
            numero_habitacion TEXT NOT NULL,
            fecha_checkin TEXT NOT NULL,
            fecha_checkout TEXT NOT NULL,
            estado TEXT NOT NULL
        );
        """
        self.cursor.execute(query)
        self.conexion.commit()

    def insertar_reserva(self, email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado):
        try:
            query = "INSERT INTO reservas (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(query, (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado))
            self.conexion.commit()
            return True, "Reserva registrada correctamente."
        except sqlite3.Error as e:
            return False, f"Error al registrar reserva: {e}"

    def obtener_reservas(self):
        query = "SELECT * FROM reservas"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def eliminar_reserva(self, id_reserva):
        try:
            query = "DELETE FROM reservas WHERE id = ?"
            self.cursor.execute(query, (id_reserva,))
            self.conexion.commit()
            return True, "Reserva eliminada correctamente."
        except sqlite3.Error as e:
            return False, f"Error al eliminar reserva: {e}"

    def actualizar_reserva(self, id_reserva, email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado):
        try:
            query = "UPDATE reservas SET email_cliente = ?, numero_habitacion = ?, fecha_checkin = ?, fecha_checkout = ?, estado = ? WHERE id = ?"
            self.cursor.execute(query, (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado, id_reserva))
            self.conexion.commit()
            return True, "Reserva actualizada correctamente."
        except sqlite3.Error as e:
            return False, f"Error al actualizar reserva: {e}"

    def cerrar_conexion(self):
        self.conexion.close()
