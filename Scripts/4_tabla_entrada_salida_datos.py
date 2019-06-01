# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("Error - Filas o columnas incorrectos")
        print("Ejemplo: tabla.py [1-9] [1-9]")   
    else:
        #Logica
        for f in range(filas):
            print("") #Aca estamos agregando vacio, para q haga el salto de linea
            for c in range(columnas):
                print(" * ", end='')     #(end='' evita el salto de línea).       
else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9] [1-9]")