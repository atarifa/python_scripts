# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:12:17 2021

@author: ansanchez
"""
from io import open
import sys

fichero = open('contador.txt','a+')
fichero.seek(0)
cont = fichero.readline()


if len(cont) == 0:
    cont = "0"
    fichero.write(cont)


fichero.close()

            
try:
    contador=int(cont)

    if len(sys.argv)==2:
    
        if sys.argv[1]=="inc":
            contador += 1
        
        elif sys.argv[1]=="dec":
            contador -= 1
           
    print(contador)    
    fichero = open("contador.txt","w")
    
    fichero.write(str(contador))
    fichero.close()            

except:
    print("Fichero no catholic")
        
        
