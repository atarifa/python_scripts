# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:00:54 2021

@author: ansanchez
"""
numeros = [200, -50, 30, 87, -116]
colores = ["rojo", "azul", "verde", "amarillo"]
lista = []
 
# Completa el ejercicio
lista.append("python")
lista.extend(numeros[:2])
lista.extend(colores[-2:])
print(lista)
lista.append(lista[1]+lista[2])
print(lista)
lista.pop(0)
print(lista)