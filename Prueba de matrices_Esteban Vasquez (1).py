# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:29:36 2022

@author: Familiar
"""
def m_10(a):
    import numpy as np
    a=np.random.randint(100,size=(10,10))
    print(a)

    suma_filas=[]
    for f in a:
        suma_filas.append(sum(f)) 
    print("Suma de las filas:",suma_filas)
    suma_columnas=[]
    for j in range(len(a[0])):
        s=0
        for i in range(len(a)):
            s+=a[i][j]
        suma_columnas.append(s)
    print("Suma de las columnas:",suma_columnas)
m_10(10)
        


    
