# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 21:02:57 2022

@author: USUARIO
"""


def isYearLeap(year):
    años=0
    meses=0
    dias=0
    error=False
    if años >4000 or años <0:
        print("El dato del año es incorrecto")
        error=True
    if meses >12 or meses <0:
        print("El dato del mes es incorrecto")
        error=True
    if dias >31 or dias <0:
        print("El dato del dia es incorrecto")
    if error==False:
        print("Puede continuar")
        añosbisiestos=int(input("Ingrese los años bisiestos que desea agregar:  "))
    if añosbisiestos<0:
        print("El valor de los años bisiestos es incorrecto ")
    else:
        print("Puede continuar")
        añosbisiestosextras=(años*365)+(meses*12)+dias
        suma=añosbisiestos+añosbisiestosextras
        A=int(suma/365)
        M=int((suma/12)-(A*12))        
        D=int((suma-(M*12)-(A*365)))
        print(A/M/D)
        