# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:21:00 2019

@author: kokor
"""

import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error - número es incorrecto")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        
else:
    print("Error - Agumentos incorrectos")
    print("Ejemplo: descomposicion.py [0-9999]")