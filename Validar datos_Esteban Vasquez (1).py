# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:20:50 2022

@author: Familiar
"""

def validar(nombre,edad,cedula,email):
    if edad>100:
        print("Error al ingresar el dato")
        return False
    elif cedula>9999999999:
        print("Error al ingresar el dato")
        return False
    si=[".","_","-","@"]
    num=["0","1","2","3","4","5","6","7","8","9"]
    dom=["gmail","ups",",hotmail","outlook","edu"]
    minu=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    mayu=[]
    ext=["com","net","ec","gob"]
    p=""
    for x in minu:
        mayu.append(x.upper())
    if email.find("@"):
        ne=email.split("@")
        us=ne[0]
        res=ne[1]
        con=res.split(".")
        dom=con[0]
        ter=con[1]
    else:
        print("Error")     
    print("Hola",nombre,edad,cedula,email)
    return True
validar("Esteban Vasquez",188,1753858412,"estebanvasquez2020@hotmail.com")