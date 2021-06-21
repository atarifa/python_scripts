# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:33:07 2021

@author: ansanchez
"""
import sqlite3


def crear_bd():
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    try:    
        cursor.execute("CREATE TABLE categoria("\
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"\
        "nombre VARCHAR(100) UNIQUE NOT NULL)")
    except:
        print("DB already exists")
    else:
        print("Table ok")
    try:
        
        cursor.execute("CREATE TABLE plato("\
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"\
        "nombre VARCHAR(100) UNIQUE NOT NULL,"\
        "categoria_id INTEGER NOT NULL,"\
        "FOREIGN KEY(categoria_id) REFERENCES categoria(id))")
    except:
        print("DB already exists")
    else:
        print("Table ok")

              
    conexion.commit()
    conexion.close()




def mostrar_menu():
    while True:
        try:
            opcion = int (input ("""Choose your option:\n
                  1.-Create a category\n
                  2.-Insert a dish\n
                  3.-Day menu\n
                  4.-Exit"""))
           
            if opcion == 1:
                agregar_categoria()
                
            if opcion == 2:
                agregar_plato()
            
            if opcion == 3:
                mostrar_menu2()
                
            if opcion == 4:
                break
        except:
            print("Choose a valid option")
            



def agregar_categoria():
    try:
        conexion=sqlite3.connect("restaurante.db")
        cursor=conexion.cursor()
        categorida=input("Insert a category\n>")
        cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(categorida))
        conexion.commit()
        conexion.close()
    except:
        print("That category already exists")        
        
    else:
        print("The category {} is inserted".format(categorida))

    


def agregar_plato():

        conexion=sqlite3.connect("restaurante.db")
        cursor=conexion.cursor()
        
        categorias = cursor.execute("SELECT * from categoria").fetchall()
        
        print("Choose a category:\n")
        
        for categoria in categorias:
            print("choose a {} for the category {}".format(categoria[0],categoria[1]))
            
        opcion=int(input(">"))

        plato=input("What dish you want to insert?\n>")
        
        
        try:
            cursor.execute("INSERT INTO plato VALUES (null,'{}','{}')".format(plato,opcion))
        
        except sqlite3.InegrityError:
            print("The dish already exists")  
        else:
            print("The dish is inserted")     
                
        conexion.commit()
        conexion.close()            


def mostrar_menu2():
     conexion=sqlite3.connect("restaurante.db")
     cursor=conexion.cursor()
        
     categorias = cursor.execute("SELECT * from categoria").fetchall()
        
     print("Day menu:\n")
        
     for categoria in categorias:
         platos = cursor.execute("SELECT * from plato WHERE categoria_id = '{}'".format(categoria[0])).fetchall()
         print("Inside the category \"{}\" we have:\n".format(categoria[1]))
         for plato in platos:
            print( "- {} \n".format(plato[1]) )
                  
     conexion.commit()
     conexion.close()                    
    
    



mostrar_menu()   