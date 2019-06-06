# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:31:00 2019

@author: walonsor
"""

## este archivo esta llamando otros ficheros en otras carpetas:
## Importar ficheros y usar sus funciones:
## DA ERROR: porque ese fichero no esta en la carpeta (saludos.py)
import saludos
saludos.saludar()

# Para verificar si nuestro interprete consulta nuestra ruta:
import sys
print(sys.path) # muestra todos los paths donde esta buscando los ficheros del import
# hay no esta nuestra ruta.
# por lo que lo agregamos manualmente:
sys.path.insert(1,'..') # en este caso q haga referencia al directorio anterior
print(sys.path)



## ya no da error.
import saludos
saludos.saludar()



## hay una forma mejor con paquetes.
