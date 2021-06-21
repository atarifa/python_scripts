# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:20:04 2021

@author: ansanchez
"""
def divisor(numero):
    try:
        return(10/numero)
    except ZeroDivisionError:
        print("0 no bonico")
        
print(divisor(0))


def listaitem(lista,indice):
    try:
        return(lista[indice])
    except IndexError:
        print("donde vas???")
        
        
lista=[1,2,3,4,5]
item=listaitem(lista,3)
print(item)





def sumatorio(a,b):
    try:
        return(a+b)
    except:
        print("alguno no anda fino")

first=15
second=20

print(sumatorio(first,second))



def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
            return(lista)
    except ValueError:
        print("Tas chalao")
    
    
    

agregar_una_vez(lista,6)
print(lista) 

