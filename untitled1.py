# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:48:00 2021

@author: ansanchez
"""

import sys

#print("Por favor introduzca los dos numeros",sys.argv())

if len(sys.argv)==3:
    filas=int(sys.argv[1])
    columnas=int(sys.argv[2])
    
    for n in range(filas):
        for m in range(columnas):
            print("*",end='')
        print("\n")





else:
    print("Por favor introduce el numero correcto de argumentos")
    print("python script.py argumento1 argumento2")
