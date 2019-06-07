Ejrcicio:
1) Crea el siguiente m�dulo:
El m�dulo se denominar� operaciones y contendr� 4 funciones para realizar una suma, una resta, un producto y una division entres dos n�meros. Todas ellas devolver�n el resultado.
En las funciones del m�dulo deber� de haber tratamiento e invocaci�n manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
TypeError: En caso de que se env�en valores a las funciones que no sean n�meros. Adem�s deber� aparecer un mensaje que informe "Error: Tipo de dato no v�lido".
ZeroDivisionError: En caso de realizar una divisi�n por cero. Adem�s deber� aparecer un mensaje que informe "Error: No es posible dividir entre cero".

Una vez creado el m�dulo, crea un script calculos.py en el mismo directorio en el que deber�s importar el m�dulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado:
from operaciones import * 

a, b, c, d = (10, 5, 0, "Hola")

print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, producto(b, b) ) ) 
print( "{} / {} = {}".format(a, c, division(a, c) ) )


Ejecutar:

python calculos.py