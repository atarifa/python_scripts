# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:48:33 2021

@author: ansanchez


Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
"""
texto="un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

#print(texto)

listexto=texto.split("#")


for i,n in enumerate(listexto):
    listexto[i].capitalize()
    if i ==0:
        listexto[i] = listexto[i] + "..."
    else:
        listexto[i] = " - "  + listexto[i] + "."
    
for linea in listexto:  
    print(linea)




