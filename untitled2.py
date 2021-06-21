# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:27:04 2021

@author: ansanchez
"""
import sys


if len(sys.argv)==2:
    numero=int(sys.argv[1])
    cadena=str(numero)
    longitud=len(cadena)
    for i in range(longitud):
        print("{:04d}".format(int(cadena[longitud-1-i] )*10**i ) )
    
    
else:
    print("Por favor ejecuta el script de forma correcta")
    print("python script.py parametro1")

