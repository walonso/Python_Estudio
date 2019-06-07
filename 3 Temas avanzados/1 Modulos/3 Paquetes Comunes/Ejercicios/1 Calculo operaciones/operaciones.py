# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("Error tipo de dato no valido")
    else:
        return r;

def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("Error tipo de dato no valido")
    else:
        return r;

def producto(a,b):
    try:
        r = a * b
    except TypeError:
        print("Error tipo de dato no valido")
    else:
        return r;

def division(a,b):
    try:
        r = a / b
    except TypeError:
        print("Error tipo de dato no valido")
    except ZeroDivisionError:
        print("No es posible dividir por 0")
    else:
        return r;