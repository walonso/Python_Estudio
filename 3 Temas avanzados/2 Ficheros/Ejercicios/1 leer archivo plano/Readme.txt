1) En este ejercicio deber�s crear un script llamado personas.py que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y lo a�ada a una lista llamada personas. Luego rocorre las personas de la lista y para cada una muestra de forma amigable todos sus campos.
El fichero de texto se denominar� personas.txt y tendr� el siguiente contenido en texto plano (cr�alo previamente):
1;Carlos;P�rez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;Garc�a;25/07/2006
Los campos del diccionario ser�n por orden: id, nombre, apellido y nacimiento.
Aviso importante: Si quieres leer un fichero que no se ha escrito directamente con Python, entonces es posible que encuentres errores de codificaci�n al mostrar algunos caracteres. Aseg�rate de indicar la codificaci�n del fichero manualmente durante la apertura como argumento en el open, por ejemplo con UTF-8:
open(..., encoding="utf8")