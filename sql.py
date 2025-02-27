import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS clientes
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido1 TEXT NOT NULL,
        apellido2 TEXT NOT NULL,
        email TEXT NOT NULL,
        dni TEXT NOT NULL)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS habitaciones
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero TEXT NOT NULL,
        tipo TEXT NOT NULL,
        precio_noche REAL NOT NULL,
        disponible BOOLEAN DEFAULT TRUE)''') # 'Individual', 'Doble', 'Suite'
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS reservas
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        id_habitacion INTEGER NOT NULL,
        fecha_checkin DATE NOT NULL,
        fecha_checkout DATE NOT NULL,
        estado TEXT DEFAULT 'Pendiente' CHECK(estado IN ('Pendiente', 'Confirmada', 'Cancelada', 'Finalizada')),
        FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE,
        FOREIGN KEY (id_habitacion) REFERENCES habitaciones(id) ON DELETE CASCADE)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS pagos
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_reserva INTEGER NOT NULL,
        monto REAL NOT NULL,
        metodo_pago TEXT NOT NULL CHECK(metodo_pago IN ('Tarjeta', 'Efectivo', 'Transferencia')),
        fecha_pago DATE NOT NULL,
        FOREIGN KEY (id_reserva) REFERENCES reservas(id) ON DELETE CASCADE)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS empleados
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        cargo TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT NOT NULL)''')
conn.commit()

conn.close()
