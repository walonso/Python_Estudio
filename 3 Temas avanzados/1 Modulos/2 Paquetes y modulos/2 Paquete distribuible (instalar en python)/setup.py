# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:50:17 2019

@author: walonsor
"""

from setuptools import setup

setup(name="paquete", 
      version="0.1",
      description="Este es un paquete de ejemplo",
      autor="Walter Alonso",
      author_email="walteralonso20@yahoo.com",
      script=[], # para asociar varios ficheros (no dentro de paquetes)
      packages=["paquete", "paquete.adios", "paquete.hola"] # se colocan los paquetes, primero el grande.. luego los subpaquetes.
)

#creamos el distribuible: (como un instalador)
###
# Se debe abrir en el terminal ubicado en la carpeta padre (donde esta este archivo)
# para este caso: E:\Walonso\Estudio\Python\Python_Estudio\3 Temas avanzados\1 Modulos\2 Paquetes y modulos\2 Paquete distribuible (instalar en python)
# y se ejecuta el comando: python setup.py sdist
# despues de eso.. se crea una carpeta dist (distribuible)
# si estas en linux crea un archivo tar.gz si es windows .zip.


## Instalarlo:
# se entra al dist: cd dist.
# se ejecuta el comando: pip install [Nombre del archivo comprimido]
# ejemplo: pip3 install paquete-0.1.tar.gz