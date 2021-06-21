# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:25:03 2021

@author: ansanchez
"""



def modificar(lista):
    lista2=lista.copy()
    lista2=list(set(lista2))

    lista2.sort(reverse=True)

    
    for i,n in enumerate(lista2):
 
        if n % 2 != 0:
            del(lista2[i])


    suma=sum(lista2)
    lista2.insert(0,suma)

    return(lista2)


lista=[29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

nueva_lista = modificar(lista)
print(lista,nueva_lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
                
        
            
    
    