# pyQT

# Estructura de la Base de Datos

## 1. Clientes
```sql
id_cliente (INT, PRIMARY KEY, AUTO_INCREMENT)
nombre (VARCHAR(100), NOT NULL)
apellido (VARCHAR(100), NOT NULL)
email (VARCHAR(150), UNIQUE, NOT NULL)
telefono (VARCHAR(15), NOT NULL)
dni_pasaporte (VARCHAR(50), UNIQUE, NOT NULL)
```

## 2. Habitaciones
```sql
id_habitacion (INT, PRIMARY KEY, AUTO_INCREMENT)
numero (VARCHAR(10), UNIQUE, NOT NULL)
tipo (ENUM('Individual', 'Doble', 'Suite'), NOT NULL)
precio_noche (DECIMAL(10,2), NOT NULL)
disponible (BOOLEAN, DEFAULT TRUE)
```

## 3. Reservas
```sql
id_reserva (INT, PRIMARY KEY, AUTO_INCREMENT)
id_cliente (INT, FOREIGN KEY → Clientes(id_cliente), NOT NULL)
id_habitacion (INT, FOREIGN KEY → Habitaciones(id_habitacion), NOT NULL)
fecha_checkin (DATE, NOT NULL)
fecha_checkout (DATE, NOT NULL)
estado (ENUM('Pendiente', 'Confirmada', 'Cancelada', 'Finalizada'), DEFAULT 'Pendiente')
```

## 4. Pagos
```sql
id_pago (INT, PRIMARY KEY, AUTO_INCREMENT)
id_reserva (INT, FOREIGN KEY → Reservas(id_reserva), NOT NULL)
monto (DECIMAL(10,2), NOT NULL)
metodo_pago (ENUM('Tarjeta', 'Efectivo', 'Transferencia'), NOT NULL)
fecha_pago (DATETIME, NOT NULL)
```

## 5. Empleados
```sql
id_empleado (INT, PRIMARY KEY, AUTO_INCREMENT)
nombre (VARCHAR(100), NOT NULL)
apellido (VARCHAR(100), NOT NULL)
cargo (VARCHAR(50), NOT NULL)
email (VARCHAR(150), UNIQUE, NOT NULL)
telefono (VARCHAR(15), NOT NULL)
```

---

# Estructura de la Aplicación

```
hotel_app/
│── main.py                # Punto de entrada principal
│── firebase_config.py      # Conexión con Firebase
│── auth.py                 # Manejo de autenticación (login, registro, logout)
│── database.py             # Operaciones con la base de datos (CRUD)
│── views/
│   ├── login.py            # Pantalla de Login
│   ├── home.py             # Página Principal (Dashboard)
│   ├── reservas.py         # Gestión de Reservas
│   ├── habitaciones.py     # Gestión de Habitaciones
│   ├── clientes.py         # Gestión de Clientes
│   ├── empleados.py        # Gestión de empleados
│── assets/                 # Iconos, imágenes, estilos
│── ui/                     # Archivos .ui de Qt Designer
│   ├── login.ui
│   ├── home.ui
│   ├── reservas.ui
│   ├── habitaciones.ui
│   ├── clientes.ui
└── README.md               # Instrucciones del proyecto
```

---

# Paleta de Colores (Estilo Moderno y Minimalista)

| Elemento | Color Primario | Color Secundario | Color de Fondo |
|----------|---------------|------------------|----------------|
| Fondo General | `#F5F7FA` (Gris Claro) | `#E0E6ED` (Gris Medio) | `#FFFFFF` (Blanco) |
| Botones Primarios | `#007BFF` (Azul) | `#0056b3` (Azul Oscuro) | `#004085` (Hover) |
| Botones Secundarios | `#28A745` (Verde) | `#218838` (Hover) | `#1E7E34` |
| Texto General | `#343A40` (Gris Oscuro) | `#6C757D` (Gris Medio) | `#495057` |
| Resaltado/Errores | `#DC3545` (Rojo) | `#C82333` (Hover) | `#BD2130` |

🔹 **Inspiración:** Una interfaz limpia, con colores neutros y botones bien definidos para una experiencia de usuario clara y atractiva.

---

# Tipografía

Usaremos **Roboto** o **Montserrat**, fuentes elegantes y legibles.

| Elemento | Tamaño |
|----------|--------|
| Títulos (QLabel) | 18px (Negrita) |
| Subtítulos (QLabel) | 16px (Semibold) |
| Texto normal (QLabel, QLineEdit) | 14px |
| Botones (QPushButton) | 14px (Negrita) |

Ejemplo de código CSS para la fuente en PyQt:
```python
font = self.labelTitulo.font()
font.setFamily("Roboto")
font.setPointSize(18)
self.labelTitulo.setFont(font)
```

---

# Distribución de Elementos en cada Ventana

## Pantalla de Login (`login.ui`)
📌 Diseño centrado, minimalista con:
- Logo del hotel arriba.
- Campos de usuario y contraseña al centro.
- Botón de "Iniciar sesión" bien visible.
- Enlace "¿Olvidaste tu contraseña?" debajo del botón.

📌 **Ejemplo de distribución en Qt Designer:**
```
┌──────────────────────────────────┐
│         🏨 [Logo del Hotel]         │
│----------------------------------│
│   Usuario:  [______________]   │
│  Contraseña: [______________] │
│                                  │
│     [ 🔵 Iniciar Sesión ]       │
│  ¿Olvidaste tu contraseña?     │
└──────────────────────────────────┘
```

### Código CSS para estilizar en PyQt:
```python
self.setStyleSheet("""
    background-color: #F5F7FA;
    QLabel {
        font-size: 16px;
        color: #343A40;
    }
    QLineEdit {
        border: 1px solid #E0E6ED;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton {
        background-color: #007BFF;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 8px;
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
""")
```

---

## Pantalla Principal (`home.ui`)
📌 **Diseño tipo "Dashboard" con menú lateral**
- A la izquierda: Menú de navegación (QVBoxLayout con iconos).
- A la derecha: Contenido dinámico con botones grandes.

📌 **Ejemplo de distribución en Qt Designer:**
```
┌───────────────────────────────────────────────────┐
│ [🏨 LOGO HOTEL]  |     [ 🔘 Reservas  ]   [ 🔘 Habitaciones ] │
│ [🏠 Inicio]      |     [ 🔘 Clientes  ]     [ 🔘 Empleados ] │
│ [📋 Reservas]   |                                          │
│ [🛏 Habitaciones] |     [ 📊 Dashboard ]                    │
│ [👤 Clientes]    |                                          │
│ [👥 Empleados]   |                                          │
│ [⚙ Configuración] |                                        │
└───────────────────────────────────────────────────┘
```

### Código CSS para estilizar en PyQt:
```python
self.setStyleSheet("""
    background-color: #FFFFFF;
    QPushButton {
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
""")
```

