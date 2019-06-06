# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:06:08 2019

@author: walonsor
"""

## importamos el modulo que esta en el paquete y llamamos la clase Saludo.
#from paquete.saludos import *
#Saludo()

# se importan las carpetas.
from paquete.hola.saludos import * #Saludo
from paquete.adios.despedidas import * # Despedida

saludar()
Despedida()