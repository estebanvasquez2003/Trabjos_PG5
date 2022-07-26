# -*- coding: utf-8 -*-
"""
Created on Fri May 20 08:57:18 2022

@author: Alumno
"""

print("---CALCULADORA DE HORAS---")
hora=int(input("Ingrese una hora:"))
minu=int(input("Ingrese los minutos de la hora:"))
seg=int(input("Ingrese los segundos de la hora:"))
s=int(input("Ingrese los segundos a sumar"))
if s<60:
    r=seg+s
    print("Su hora total es:",hora,":",minu,":",r)
else: 
    print("No se puede realizar el calculo")