3) Crea un script llamado generador.py que cumpla las siguientes necesidades:
Debe incluir una funci�n llamada leer_numero(). Esta funci�n tomar� 3 valores: ini, fin y mensaje. El objetivo es leer por pantalla un n�mero >= que ini y <= que fin. Adem�s a la hora de hacer la lectura se mostrar� en el input el mensaje enviado a la funci�n. Finalmente se devolver� el valor. Esta funci�n tiene que devolver un n�mero, y tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no sea un n�mero del ini al fin).
Una vez la tengas creada, deber�s crear una nueva funci�n llamada generador, no recibir� ning�n par�metro. Dentro leer�s dos n�meros con la funci�n leer_numero():
El primer numero ser� llamado numeros, deber� ser entre 1 y 20, ambos incluidos, y se mostrar� el mensaje �Cuantos n�meros quieres generar? [1-20]:
El segundo n�mero ser� llamado modo y requerir� un n�mero entre 1 y 3, ambos incluidos. El mensaje que mostrar� ser�: *�C�mo quieres redondear los n�meros? [1]Al alza [2]A la baja [3]Normal: *.
Una vez sepas los n�meros a generar y c�mo redondearlos, tendr�s que realizar lo siguiente:
Generar�s una lista de n�meros aleatorios decimales entre 0 y 100 con tantos n�meros como el usuario haya indicado. 
A cada uno de esos n�meros deber�s redondearlos en funci�n de lo que el usuario ha especificado en el modo.
Para cada n�mero muestra durante el redondeo, el n�mero normal y despu�s del redondeo.
Finalmente devolver�s la lista de n�meros redondeados.
** El objetivo de este ejercicio es practicar la reutilizaci�n de c�digo y los m�dulos random y math.**
Nota: Recuerda que el redondeo tradicional round() no requiere ning�n m�dulo.