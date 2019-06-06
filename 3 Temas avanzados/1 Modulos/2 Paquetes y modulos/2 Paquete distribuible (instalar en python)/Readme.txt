* 
1. Se debe crear el archivo setup.py:
	from setuptools import setup
		***
2. Si esta en windows, Revice que tenga python y pip3 en el path.
Pip3 esta dentro de la carepta Scripts dentro del folder de python.

3. Para crear el distrbuible: (carpeta dist)

#creamos el distribuible: (como un instalador)
3.1 Se debe abrir en el terminal ubicado en la carpeta padre (donde esta este archivo)
# para este caso: E:\Walonso\Estudio\Python\Python_Estudio\3 Temas avanzados\1 Modulos\2 Paquetes y modulos\2 Paquete distribuible (instalar en python)
3.2 y se ejecuta el comando: python setup.py sdist
# despues de eso.. se crea una carpeta dist (distribuible)
# si estas en linux crea un archivo tar.gz si es windows .zip.

## Instalarlo:
3.3 se entra al dist: cd dist.
3.4 se ejecuta el comando: pip install [Nombre del archivo comprimido]
# ejemplo: pip3 install paquete-0.1.tar.gz
