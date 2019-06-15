1.1) A lo largo de estos ejercicios vamos a crear un peque�o sistema para gestionar los platos del men� de un restaurante. Por ahora debes empezar creando un script llamado restaurante.py y dentro una funci�n crear_bd() que crear� una peque�a base de datos restaurante.db con las siguientes dos tablas:
Si ya existen deber� tratar la excepci�n y mostrar que las tablas ya existen. En caso contrario mostrar� que se han creado correctamente. 
CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)
CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
Nota: La l�nea FOREIGN KEY(categoria_id) REFERENCES categoria(id) indica un tipo de clave especial (for�nea), por la cual se crea una relaci�n entre la categor�a de un plato con el registro de categor�as.
Llama a la funci�n y comprueba que la base de datos se crea correctamente.

1.2) Crea una funci�n llamada agregar_categoria() que pida al usuario un nombre de categor�a y se encargue de crear la categor�a en la base de datos (ten en cuenta que si ya existe dar� un error, por que el nombre es UNIQUE).
Ahora, crea un peque�o men� de opciones dentro del script, que te de la bienvenida al sistema y te permita Crear una categor�a o Salir. A�ade las siguientes tres categor�as utilizando este men� de opciones:
Primeros 
Segundos 
Postres
1.3) Crea una funci�n llamada agregar_plato() que muestre al usuario las categor�as disponibles y le permita escoger una (escribiendo un n�mero).
Luego le pedir� introducir el nombre del plato y lo a�adir� a la base de datos, teniendo en cuenta que la categoria del plato concuerde con el id de la categor�a y que el nombre del plato no puede repetirse (no es necesario comprobar si la categor�a realmente existe, en ese caso simplemente no se insertar� el plato).
Agrega la nueva opci�n al men� de opciones y a�ade los siguientes platos:
Primeros: Ensalada del tiempo / Zumo de tomate
Segundos: Estofado de pescado / Pollo con patatas
Postres: Flan con nata / Fruta del tiempo
1.4) Crea una funci�n llamada mostrar_menu() que muestre el men� con todos los platos de forma ordenada: los primeros, los segundos y los postres. Optativamente puedes adornar la forma en que muestras el men� por pantalla.


2) En este ejercicios debes crear una interfaz gr�fica con tkinter (menu.py) que muestre de forma elegante el men� del restaurante.
T� eliges el nombre del restaurante y el precio del men�, as� como las tipograf�as, colores, adornos y tama�o de la ventana.
El �nico requisito es que el programa se conectar� a la base de datos para buscar la lista categor�as y platos.
Algunas ideas: https://www.google.es/search?tbm=isch&q=dise%C3%B1o+menu+restaurantes