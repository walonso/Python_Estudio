# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:34:50 2019

@author: kokor
"""

from io import open
import sys

fichero = open("contador.txt","a+")
fichero.seek(0)
contenido = fichero.readline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)
    
fichero.close()

# intentar transformar texto a numero
try:
    contador = int(contenido)
    
    # segun lo  quiera el usuario
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
            
    print(contador)
        
    # escribir en el fichero
    fichero = open("contador.txt","w")
    fichero.write(str(contador))
    fichero.close()

except:
    print("Error: archivo corrupto")

       