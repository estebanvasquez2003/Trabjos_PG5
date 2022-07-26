# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:00:38 2022

@author: Familiar
"""

from math import sqrt
def A(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
def fibonacci(start, end):
    n = 0
    c = A(n)
    while c <= end:
        if start <= c:
            print(c)
        n += 1
        c = A(n)
fibonacci(1,100)