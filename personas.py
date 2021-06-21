# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:34:21 2021

@author: ansanchez
"""
from io import open

lineas=[]
personas=[]

fichero = open('personas.txt','r',encoding="utf8")

lineas=fichero.readlines()

fichero.close()


for i in lineas:
    campos=i.split(";")
    persona={"id":campos[0],"nombre":campos[1],"apellido":campos[2],"nacimiento":campos[3]}
    personas.append(persona)



for i in personas:
    print("El ID es {}, el nombre es {}, los apellidos {} y la fecha de nacimiento {}".format(i['id'],i['nombre'],i['apellido'],i['nacimiento']))