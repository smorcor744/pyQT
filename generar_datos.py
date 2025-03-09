import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializar Faker
fake = Faker('es_ES')  # Usamos 'es_ES' para datos en español

# Conectar a la base de datos
conexion = sqlite3.connect('hotel.db')
cursor = conexion.cursor()

# Función para generar y insertar 100 habitaciones
def insertar_habitaciones():
    tipos = ['Individual', 'Doble']
    habitaciones = []

    # Generar números de habitación del 101 al 520
    for planta in range(1, 6):  # Plantas del 1 al 5
        for habitacion in range(1, 21):  # Habitaciones del 1 al 20 por planta
            numero = f"{planta}{habitacion:02d}"  # Formato: 101, 102, ..., 120, 201, ..., 520
            habitaciones.append(numero)

    # Insertar las habitaciones en la base de datos
    for numero in habitaciones:
        tipo = random.choice(tipos)
        precio_noche = round(random.uniform(50, 200), 2)  # Precio entre 50 y 200
        disponible = random.choice([True, False])
        cursor.execute(
            "INSERT INTO habitaciones (numero, tipo, precio_noche, disponible) VALUES (?, ?, ?, ?)",
            (numero, tipo, precio_noche, disponible)
        )
    print("100 habitaciones insertadas (del 101 al 520).")

# Función para generar y insertar 100 clientes
def insertar_clientes():
    for _ in range(100):
        nombre = fake.first_name()
        apellido1 = fake.last_name()
        apellido2 = fake.last_name()
        email = fake.unique.email()
        dni = fake.unique.bothify('########?')  # Genera un DNI ficticio
        cursor.execute(
            "INSERT INTO clientes (nombre, apellido1, apellido2, email, dni) VALUES (?, ?, ?, ?, ?)",
            (nombre, apellido1, apellido2, email, dni)
        )
    print("100 clientes insertados.")

# Función para generar y insertar 100 reservas
def insertar_reservas():
    cursor.execute("SELECT email FROM clientes")
    emails_clientes = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT numero FROM habitaciones")
    numeros_habitaciones = [row[0] for row in cursor.fetchall()]

    for _ in range(100):
        email_cliente = random.choice(emails_clientes)
        numero_habitacion = random.choice(numeros_habitaciones)
        fecha_checkin = fake.date_between(start_date='-30d', end_date='today')
        fecha_checkout = fecha_checkin + timedelta(days=random.randint(1, 14))
        estado = random.choice(['Pendiente', 'Confirmada', 'Cancelada', 'Finalizada'])
        cursor.execute(
            "INSERT INTO reservas (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado) VALUES (?, ?, ?, ?, ?)",
            (email_cliente, numero_habitacion, fecha_checkin, fecha_checkout, estado)
        )
    print("100 reservas insertadas.")

# Función para generar y insertar 100 pagos
def insertar_pagos():
    cursor.execute("SELECT id FROM reservas")
    ids_reservas = [row[0] for row in cursor.fetchall()]

    # Asegurarse de que cada reserva tenga solo un pago
    for id_reserva in ids_reservas:
        monto = round(random.uniform(50, 500), 2)
        metodo_pago = random.choice(['Tarjeta', 'Efectivo'])
        fecha_pago = fake.date_between(start_date='-30d', end_date='today')
        cursor.execute(
            "INSERT INTO pagos (id_reserva, monto, metodo_pago, fecha_pago) VALUES (?, ?, ?, ?)",
            (id_reserva, monto, metodo_pago, fecha_pago)
        )
    print(f"{len(ids_reservas)} pagos insertados (uno por reserva).")

# Función para generar y insertar 50 empleados
def insertar_empleados():
    cargos = ['Recepcionista', 'Limpieza', 'Gerente', 'Cocinero', 'Seguridad']
    for _ in range(50):
        nombre = fake.first_name()
        apellido = fake.last_name()
        cargo = random.choice(cargos)
        email = fake.unique.email()
        telefono = fake.phone_number()
        cursor.execute(
            "INSERT INTO empleados (nombre, apellido, cargo, email, telefono) VALUES (?, ?, ?, ?, ?)",
            (nombre, apellido, cargo, email, telefono)
        )
    print("50 empleados insertados.")

# Ejecutar las funciones para insertar datos
insertar_habitaciones()
insertar_clientes()
insertar_reservas()
insertar_pagos()
insertar_empleados()

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
print("Base de datos alimentada con datos de prueba.")