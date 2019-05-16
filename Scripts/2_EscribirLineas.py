# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:58:30 2019

@author: walonsor
"""

import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce los argumentos correctamente")
    print("Ejemplo: 2_EscribirLineas.py 'texto' 5")
