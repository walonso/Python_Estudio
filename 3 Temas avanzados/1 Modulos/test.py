# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:31:00 2019

@author: walonsor
"""

## Importar ficheros y usar sus funciones:

# 1. importamos el fichero saludos.py y se usa el nombre de la clase para llamar la funcion:
import saludos
saludos.saludar()

#

# 2. para obviar la clase se debe cambiar el import y llamamos la funcion q se necesita
from saludos import saludar
saludar()

# 3. para importar todas las funciones se usa el asterisco:
from saludos import *
saludar()


################ Manejo de clases de ficheros ####################
# 4. Llamar clases:
import saludos
s = saludos.Saludo()

# 5. importamdo directamente la clase
from saludos import Saludo
Saludo()
