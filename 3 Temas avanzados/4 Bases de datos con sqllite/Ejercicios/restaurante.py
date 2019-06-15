import sqlite3

def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:        
        cursor.execute('''
            CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)
        ''')
    except sqlite3.OperationalError:
        print('La tabla Categoria ya existe')
    else:
        print('Categoria se creo correctamente')
    
    try:
        cursor.execute('''
            CREATE TABLE plato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL, 
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        ''')
    except sqlite3.OperationalError:
        print('La tabla Plato ya existe')
    else:
        print('plato se creo correctamente')
    
    conexion.close()

def agregar_categoria():
    categoria = input("Nombre de la nueva categoria\n>")
    
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoría '{}' ya existe".format(categoria))
    else:
        print("Categoria agregada")
    conexion.commit()
    conexion.close()

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato = input("Nombre del nuevo plato\n>")
    
    try:
        cursor.execute("INSERT INTO plato VALUES (null,'{}',{})".format(plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe".format(plato))
    else:
        print("plato agregado")

    conexion.commit()
    conexion.close()

def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("\t{}".format(plato[1]))
    conexion.close()


# Crear la bd
crear_db()

# Menu de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input("\nIntroduce una opción: \n[1] Agregar una categoría\n[2] Agregar un plato\n[3] Mostrar el menu\n[4] Salir del programa\n\n")

    if opcion == "1":
        agregar_categoria()
    elif opcion=="2":
        agregar_plato()
    elif opcion=="3":
        mostrar_menu()
    elif opcion=="4":
        print("Nos vemos!")
        break
    else:
        print("Opción incorrecta")