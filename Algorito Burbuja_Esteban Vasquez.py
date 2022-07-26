# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 23:48:09 2022

@author: Familiar
"""

import numpy as np
while True:
    while True:
        tamaño=int(input("Ingrese la dimension: "))
        numeros=int(input("Ingrese los numeros que desea: "))
        break
    vector = np.array(np.random.randint(50,100,tamaño))
    print(vector)
    num=len(vector)
    i=0
    while i<num:
        j=i
        while j<num:
            if vector[i]<vector[j]:
                aux=vector[i]
                vector[i]=vector[j]
                vector[j]=aux
            j=j+1
        i=i+1
    ope = int(input('Que operación matematica desea hacer: 1.Suma, 2.Resta, 3.Multiplicación, 4.Division\n Digite 0.para salir del programa'))
    res = 0
    suma=0
    multiplicacion=0
    division=0
    if ope == 0:
      print('Gracias .')
      break
    elif ope == 1:
      for i in vector:
        suma+= vector
      print('La suma del vector: ',suma)
    elif ope == 2:
      for i in vector:
        res -= vector
      print('La resta del vector: ',res)
    elif ope == 3:
      for i in vector:
        multiplicacion *= vector
      print('La multiplicación del vector: ', multiplicacion)
    elif ope == 4:
      for i in vector:
        division /=  vector
      print('La division del vector: ',division)
print("Lista ordenada: ")
print(vector)