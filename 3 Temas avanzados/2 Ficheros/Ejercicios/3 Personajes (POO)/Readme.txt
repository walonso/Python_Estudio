3) Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendr�s que crear un gestor de personajes (gestor.py) para a�adir y borrar la informaci�n de los siguientes personajes:

Vida
Ataque
Defensa
Alcance
Caballero
4
2
4
2
Guerrero
2
4
2
4
Arquero
2
4
1
8
Deber�s hacer uso del m�dulo pickle y todos los cambios que realices se ir�n guardando en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistir�n.
Crea dos clases, una Personaje y otra Gestor.
La clase Personaje deber� permitir crear un personaje con el nombre (que ser� la clase), y sus propiedades de vida, ataque, defensa y alcance (que deben ser n�meros enteros positivos mayor que cero obligatoriamente).**
Por otro lado la clase Gestor deber� incorporar todos los m�todos necesarios para a�adir personajes, mostrarlos y borrarlos (a partir de su nombre por ejemplo) (tendr�s que pensar una forma de hacerlo), adem�s de los m�todos esenciales para guardar los cambios en el fichero personajes.pckl que se deber�an ejecutar autom�ticamente. 
En caso de que el personaje ya exista en el Gestor entonces no se crear�.
Una vez lo tengas listo realiza las siguientes prueba en tu c�digo: 
Crea los tres personajes de la tabla anterior y a��delos al Gestor.
Muestra los personajes del Gestor.
Borra al Arquero.
Muestra de nuevo el Gestor.
Sugerencias: El ejemplo con pickle que realizamos puede servirte como base.