# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:42:37 2022

@author: USUARIO
"""

import random
def Listrandom(num):
    list=[0]*num
    for a in range(num):
        list[a]=random.random()
        return list
print("Ingrese la cantidad de numeros aleatorios que quiere obtener: ")
num=int(input())
aleatory=Listrandom(num)
print(aleatory)