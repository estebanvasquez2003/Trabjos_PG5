# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:22:33 2022

@author: Familiar
"""

import math
def isPrime(num):
 for n in range(3,int(math.sqrt(num))+1,2):
  if num%n==0:
   return False
 return True
def listPrime(l):
 print(2)
 for i in range(3,l+1,2):
  if isPrime(i):
   print(i)
listPrime(100)


