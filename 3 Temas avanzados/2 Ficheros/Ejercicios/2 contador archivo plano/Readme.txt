2) En este ejercicio deber�s crear un script llamado contador.py que realice varias tareas sobre un fichero llamado contador.txt que almacenar� un contador de visitas (ser� un n�mero):
Nuestro script trabajar� sobre un fichero contador.txt. Comprobaremos si el fichero no existe o est� vac�o, en ese caso lo crearemos con el n�mero 0. Si existe simplemente leeremos el valor del contador.
Luego a partir de un argumento:
Si se env�a el argumento inc, se incrementar� el contador en uno y se mostrar� por pantalla.
Si se env�a el argumento dec, se decrementar� el contador en uno y se mostrar� por pantalla.
Si no se env�a ning�n argumento (o algo que no sea inc o dec), se mostrar� el valor del contador por pantalla.
Finalmente guardar� de nuevo el valor del contador de nuevo en el fichero.
Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.