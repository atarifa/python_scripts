# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 16:15:50 2021

@author: ansanchez
"""
import sqlite3

conexion = sqlite3.connect("usuarios.db")


cursor=conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios" \
               "(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
                    
conexion.commit()
conexion.close()