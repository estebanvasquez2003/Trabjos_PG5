# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 22:02:14 2022

@author: Familiar
"""
n=int(input("Ingrese un valor mayor o igual a 4 y menor o igual a 30: "))

def validar(n):
    while n<4 or n>30:
        n=int(input("Error,ingrese un valor nuevamente: "))
validar(n)

def llenar(n):
    import numpy as np
    a=np.random.randint(10,size=(1,n))
    print(a)
    return a
llenar(n)
  
def primo(a):
    x=1
    c=0
    while x <= a:
        if n % x==0:
            c=c+ 1
        x = x + 1
    if c==2:
        print(a)
primo(n)



    
        
        