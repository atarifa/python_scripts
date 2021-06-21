# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:09:02 2021

@author: ansanchez
"""
import random
import math

def leer_numero(ini,fin,mensaje):
    while True:
        try:
            valor=int(input(mensaje))

        except:
            print("wrong value")
        else:
            if valor >= ini and valor <= fin:
                break
    return valor
    
    
def generador():
    numeros=leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]:")
    modo=leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:")

    lista=[]    
    listarnd=[]

    for i in range(numeros):
        x=random.uniform(0,101)
        lista.append(x)

        if modo == 1:
            y=math.ceil(x)
        elif modo ==2:
            y=math.floor(x)
        elif modo ==3:
            y=round(x)
            
        listarnd.append(y)
        print("El numero aleatorio es {} y se redondea a {} ".format(x,y))
    return(lista)

generador()

    