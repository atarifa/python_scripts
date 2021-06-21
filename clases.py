# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:43:21 2021

@author: ansanchez
"""
import math

class Punto:
    
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
        
    def __str__(self):
        return("({},{})".format(self.x,self.y))
    
    def cuadrante(self):
        
        if self.x > 0 and self.y > 0 :
            cuadrante = 1
            print("El punto {} pertenece al cuadrante {}".format(self,cuadrante))
        elif self.x > 0 and self.y < 0 :
            cuadrante = 4
            print("El punto {} pertenece al cuadrante {}".format(self,cuadrante))

        elif self.x < 0 and self.y > 0 :
            cuadrante = 2
            print("El punto {} pertenece al cuadrante {}".format(self,cuadrante))

        elif self.x < 0 and self.y < 0 :
            cuadrante = 3
            print("El punto {} pertenece al cuadrante {}".format(self,cuadrante))
        else:
            cuadrante = 0
            print("El punto {} pertenece al cuadrante {}".format(self,cuadrante))
    
    def vector(self,p):
        print("El vector entre {} y {} es ({},{})".format(self,p,p.x-self.x,p.y-self.y))



    def distancia(self,punto2):
        e=punto2.x-self.x
        e2=punto2.y-self.y
        d=math.sqrt((e**2)+(e2**2))
        print("La distancia entre {} y {} es {}".format(self,punto2,d))



class Rectangulo:


    def __init__(self,p1=Punto(),p2=Punto()):
        self.p1=p1
        self.p2=p2
        
    def base(self):
        self.base=abs(self.p2.x-self.p1.x)

        print("La base del restangulo es {}".format(self.base))
        return(self.base)
        
    def altura(self):
        self.altura=abs(self.p2.y-self.p1.y)
        print("La altura del restangulo es {}".format(self.altura))
        return(self.altura)

    def area(self):

        print("El area del restangulo es {}".format(self.base*self.altura))

        
        
 
A=Punto(2,3)
B=Punto(5,5)        
# C=Punto(-3,1)
# D=Punto(0,0)

# print(A,B,C,D)

# A.cuadrante()
# B.cuadrante()
# C.cuadrante()
# D.cuadrante()

# A.vector(B)
# B.vector(A)

# A.distancia(D)
# B.distancia(D)
# C.distancia(D)


R=Rectangulo(A,B)
R.base()
R.altura()
R.area()

