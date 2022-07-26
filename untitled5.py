# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:41:45 2022

@author: Familiar
"""

acl=int(input("Ingrese el numero de ACL: "))
if acl >=1 and acl<=99:
 print("Es un ACL de tipo estandar")
elif acl>=100 and acl<=199:
 print("Es un ACL extendida")
elif acl>=1300 and acl<=1999:
 print ("Es un ACL de tipo estandar en rango expandido")
elif acl>=2000 and acl<=2699:
    print ("Es un ACL de tipo Extendida en rango expandido")
else:
 print("El numero ingresado no es de un ACL")
 
 