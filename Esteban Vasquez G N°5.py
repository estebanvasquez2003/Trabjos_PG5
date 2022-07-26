# -*- coding: utf-8 -*-
"""
Created on Fri May 27 07:43:00 2022

@author: Alumno
"""
n=int(input("Ingrese un valor: "))
v=range(2,n)
c=0
while n<=1:
    print("")
    print("Error, debe ingreser un numero mayor de 1")
    print("")
    n=int(input("Porfavor, ingrese un valor valido:"))
if n==2:
    print("El 2 Es el primer número primo")
else:
    for n in v:
        if n % n==0:
            c+=1
            print("divisor:",n)   
    if c>0:
        ("")
        print("El número no es primo")
    else:
        print("")
        print("El número es primo")
        print("")
        print("Puede continuar")
        
        
    

            
    
    


        


