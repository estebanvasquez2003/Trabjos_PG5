# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:05:29 2022

@author: Familiar
"""

from math import sqrt
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
r=(b*b)-4*a*c
if a==0:
    print("")
    print("División para 0")
else:
    if r<0:
        print("")
        print("Raíz negativa")
    else:
        raiz=sqrt(r)
        x1=(-b + raiz)/(2*a)
        if r !=0:
            x2=(-b - raiz)/(2*a)
            print("")
            print("Dos soluciones:")
            print("x1=",x1)
            print("x2=",x2)
        else:
            print("")
            print("Única solución:")
            print("x=",x1)
            
            
            
            
            
            
            
            
    