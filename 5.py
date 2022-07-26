# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 22:47:19 2022

@author: Familiar
"""

from math import factorial
def SerieIlimitada(n,Ilimitado):
    suma=n
    for a in range(0,Ilimitado):
        valores=pow(n,a)/factorial(n)
        suma+=valores
        print("Iteracion: ",n,"\nValores: ",valores,"\nsuma: ",suma)
print("Serie Ilimitada")
n=int(input("Escriba el valor de n: "))
while True:
    Ilimitado=int(input("Escriba un numero entero positivo: "))
    if Ilimitado > 0:
        break
SerieIlimitada(n,Ilimitado)



