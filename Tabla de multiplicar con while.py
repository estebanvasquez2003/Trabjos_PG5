# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 04:58:46 2022

@author: Familiar
"""

j=1
i=1
suma = 0
promedio = 0
par = 0
impar = 0

n=int(input("Ingrese la cantidad de tablas que deseas tener: "))
while n<=1 or n>99:
    print("Por favor, ingrese un número mayor que 1 y menor que 100")
    n=int(input("Ingrese un valor válido: "))
a=int(input("Ingrese la cantidad de números que desea multiplicar en cada tabla: "))
while a<=1 or a>99:
    print("Por favor, ingrese un número mayor que 1 y menor que 100")
    a=int(input("Ingrese un valor válido "))

while i <= n:
  print("La tabla del N°:",i)
  while j <= a:
    resm = i*j
    suma += resm
    print(i,"x",j,"=",resm)
    j += 1
    if resm % 2 == 0:
      par += 1
    else:
      impar += 1
    promedio = suma/a
  i+=1
  j=1
  print("La suma de los numeros es",suma)
  print("El promedio de los numeros es:",promedio)
  print("Hay",par,"numeros pares")
  print("Hay",impar,"numeros impares")
  suma = 0
  par = 0
  impar = 0