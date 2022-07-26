# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 08:39:33 2022

@author: Alumno
"""

def tabla(n):
    import numpy as np
    print("          L","M"," X"," J"," V"," S","T")
    a=np.random.randint(4,size=(1,6))
    b=np.random.randint(4,size=(1,6))
    c=np.random.randint(4,size=(1,6))
    d=np.random.randint(4,size=(1,6))
    e=np.random.randint(4,size=(1,6))
    e1=np.random.randint(4,size=(1,6))
    g=np.random.randint(4,size=(1,6))
    h=np.random.randint(4,size=(1,6))
    i=np.random.randint(4,size=(1,6))
    j=np.random.randint(4,size=(1,6))
    
    s1=[]
    s2=[]
    s3=[]
    s4=[]
    s5=[]
    s6=[]
    s7=[]
    s8=[]
    s9=[]
    s10=[]
    
    
    for f1 in a:
        s1.append(sum(f1))
        
    for f2 in b:
        s2.append(sum(f2))
        
    for f3 in c:
        s3.append(sum(f3))
        
    for f4 in d:
        s4.append(sum(f4))
        
    for f5 in e:
        s5.append(sum(f5))
        
    for f6 in e1:
        s6.append(sum(f6))
        
    for f7 in g:
        s7.append(sum(f7))
        
    for f8 in h:
        s8.append(sum(f8))
        
    for f9 in i:
        s9.append(sum(f9))
        
    for f10 in j:
        s10.append(sum(f10))
    
    print("Chevrolet",a,s1)
    print("Mazda","   ",b,s2)
    print("Nissan","  ",c,s3)
    print("Toyota","  ",d,s4)
    print("Hyundai"," ",e,s5)
    print("Kia","     ",e1,s6)
    print("Renault"," ",g,s7)
    print("Graet W"," ",h,s8)
    print("Jac","     ",i,s9)
    print("Chery","   ",j,s10)   
   
tabla(1)