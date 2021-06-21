# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:39:01 2021

@author: ansanchez
"""
import math

def area_rectangulo(base, altura):
    return(base*altura)
print(area_rectangulo(5,4))

def area_circulo(radio):
    return(2**radio*math.pi)
print(area_circulo(5))

def relacion(a, b):
    if a > b:
        return 1
    elif b>a:
        return -1
    return 0

print(relacion(5,5))



def intermedio(a, b):
    return((a +b)/2)

print (intermedio(-12,24))


def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

print(recortar(15,0,10))
        

def separar(lista):
    par=[]
    impar=[]
    lista.sort()
    for i in lista:
        if i %2 == 0:
            par.append(i)
        else:
            impar.append(i)
    return(par,impar)

par,impar=separar([3,6,8,8,5,4,45,23,5])

print(par)
print(impar)