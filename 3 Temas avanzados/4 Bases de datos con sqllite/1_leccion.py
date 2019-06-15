import sqlite3 

conexion = sqlite3.connect("ejemplo.db")

# para ejecutar coigo sql
cursor = conexion.cursor()

#1. crear tabla
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
# 2. insertar un registro a la tabla
#cursor.execute("INSERT INTO usuarios values ('Walter',29,'walteralonso@ejemplo.com')")
# 3. select de tabla usuarios
#cursor.execute("SELECT * FROM usuarios")
# 4. obtenga el primer registro (lo devuelve como tupla)
#usuario = cursor.fetchone()
#print(usuario)

# 5. insercion de varios registros
"""
usuarios = [
    ('Pepito', 51, 'pepito@eje.com'),
    ('Maria', 38, 'maria@eje.com'),
    ('Juan', 47, 'juan@eje.com')
]
cursor.executemany("INSERT INTO  usuarios VALUES (?,?,?)", usuarios)
"""
# 6. obetener todos los registros
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
print(usuarios)
for usuario in usuarios:
    print(usuario)
    print("Nombre:"+usuario[0])

conexion.commit()

conexion.close()