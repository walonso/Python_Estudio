import sqlite3 

#claves unicas, foraneas

# conexion para usuarios
conexion = sqlite3.connect("usuarios.db")
#conexion = sqlite3.connect("productos.db")

# para ejecutar coigo sql
cursor = conexion.cursor()

# 1. crear tabla e insertarle registros
"""
cursor.execute('''
    CREATE TABLE usuarios (
        dni VARCHAR(9) PRIMARY KEY,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
''')

usuarios = [
    ('111A','Walter', 29, 'walter@eje.com'),
    ('222B','Pepito', 51, 'pepito@eje.com'),
    ('333C','Maria', 38, 'maria@eje.com'),
    ('444D','Juan', 47, 'juan@eje.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)",usuarios)
"""

# 2. con conexion productos
"""
cursor.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        marca VARCHAR(50) NOT NULL,
        precio FLOAT NOT NULL
    )
''')
"""

# 3. CREANDO productos
"""
productos = [
    ('Teclado', 'Logitech', 19.95),
    ('Pantalla 19"','LG',89.95)
]
# se coloca null, para que sepa q es autoincremental
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
"""

# 4. consultarlos
"""
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
"""

# 5. claves unicas, añadir otros campos como unicos
# con la conexion usuarios.db
"""
cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
''')

usuarios = [
    ('111A','Walter', 29, 'walter@eje.com'),
    ('222B','Pepito', 51, 'pepito@eje.com'),
    ('333C','Maria', 38, 'maria@eje.com'),
    ('444D','Juan', 47, 'juan@eje.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)",usuarios)
"""
cursor.execute("INSERT INTO usuarios VALUES (null,'444D','d',23,'d@eje.com')")

conexion.commit()

conexion.close()