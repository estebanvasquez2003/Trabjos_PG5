# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 07:32:25 2022

@author: Alumno
"""
suma=0
promedio=0
for n in range(1,16):
   print("")
   print("La tabla del N°:",n)
   print("")
   par=0
   impar=0
   for i in range(1,16):
       res=i*n
       suma+=res
       promedio=suma//15
       print(i,"x",n,"=",res)
       if res%2==0:
           par=par+1
       else:
           impar=impar+1
   print("La suma de los numeros es",suma)
   print("El promedio de los numeros es:",promedio)
   print("Hay",par,"numeros pares")
   print("Hay",impar,"numeros impares")
   print("")
   