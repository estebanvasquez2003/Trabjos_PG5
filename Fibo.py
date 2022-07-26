# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 08:28:45 2022

@author: Familiar
"""

def fib(n):
    a,b=0,1
    while a<=n:
        print(a,end=" ")
        """c=a+b
        a=b
        b=c"""
        a,b=b,a+b
fib(8)
    
  
    