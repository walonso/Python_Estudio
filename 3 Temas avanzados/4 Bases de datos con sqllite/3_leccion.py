import sqlite3 

#claves unicas, foraneas

# conexion para usuarios
conexion = sqlite3.connect("usuarios.db")
#conexion = sqlite3.connect("productos.db")

# para ejecutar coigo sql
cursor = conexion.cursor()

# 1. clausula Where
"""
cursor.execute("SELECT * FROM usuarios WHERE id=1")
usuario = cursor.fetchone()
print(usuario)
"""

# 2. modificar
#cursor.execute("UPDATE usuarios SET nombre='Walter Alonso' WHERE id=1")

# 3.MODIFICAR VARIOS campos
#cursor.execute("UPDATE usuarios SET nombre='Walter Alonso', edad=30 WHERE id=1")

# 4. borrar
#cursor.execute("DELETE FROM usuarios WHERE id=1")


conexion.commit()

conexion.close()