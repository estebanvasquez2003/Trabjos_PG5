# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:16:26 2022

@author: Familiar
"""

import random
while True:
    fi=int(input("Ingrese las filas que desee: "))
    if fi<4 or fi>10:
        print("ERROR, Ingrese un numero -4 y +10")
    else:
        break
while True:
    co=int(input("Ingrese las columnas que desee: "))
    if co<4 or co>10:
        print("ERROR, Ingrese un numero -4 y +10")
    else:
        break
    
matriz = [[int() for i in range(co)] for j in range(fi)]

def n():
    for f in range(fi):
        for c in range(co):
            valores=random.randint(0,5)
            matriz[f][c]=valores
        
n()

for i in range(fi):
    print("|", end=" ")
    for j in range(co):
        print(matriz[i][j],"|",end=" ")
    print("\n")

def s(fila):
    sumafi=0
    for s in range(co):
        valorf=matriz[fila-1][s]
        sumafi+=valorf
    print("la suma de filas",fila,"es: ",sumafi)
    
def su(columna):
    sumaco=0
    for b in range(fi):
        valorc=matriz[b][columna-1]
        sumaco+=valorc
    print("la suma de columnas",columna,"es: ",sumaco)
    print("\n")

for k in range(fi):   
    s(k+1)
    su(k+1)

def pro():
    sumatotal=0
    for p in range(fi):
        for q in range(co):
            suma=matriz[p][q]
            sumatotal+=suma
    print("El promedio de la matriz es:",sumatotal/(fi*co))
pro()