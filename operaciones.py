# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:42:30 2021

@author: ansanchez
"""


def suma(a,b):

    try:
        r=a+b  
    except:
        print("Error: Tipo de dato no válido.")
    else:
        return r
    
def resta(a,b):

    try:
        r=a-b
    except:
        print("Error: Tipo de dato no válido.")
    else:
        return r

def producto(a,b):

    try:
        r=a*b
    except:
        print("Error: Tipo de dato no válido.")
    else:
        return r
    
def division(a,b):

    try:
        r=a/b
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    except:
        print("Error: Tipo de dato no válido.")
    else:
        return r
        
        

