import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS clientes
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        apellido1 TEXT NOT NULL,
        apellido2 TEXT NOT NULL,
        email TEXT NOT NULL,
        dni TEXT NOT NULL)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS habitaciones
        (id INTEGER PRIMARY KEY,
        numero TEXT NOT NULL,
        tipo TEXT NOT NULL,
        precio_noche REAL NOT NULL,
        disponible BOOLEAN DEFAULT TRUE)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS reservas
        (id INTEGER PRIMARY KEY,
        id_cliente INTEGER NOT NULL,
        id_habitacion INTEGER NOT NULL,
        fecha_checkin DATE NOT NULL,
        fecha_checkout DATE NOT NULL,
        estado TEXT DEFAULT 'Pendiente')''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS pagos
        (id INTEGER PRIMARY KEY,
        id_reserva INTEGER NOT NULL,
        monto REAL NOT NULL,
        metodo_pago TEXT NOT NULL,
        fecha_pago DATE NOT NULL)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS empleados
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        cargo TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT NOT NULL)''')
conn.commit()

c.close()
