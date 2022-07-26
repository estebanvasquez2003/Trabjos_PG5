
# -*- coding: utf-8 -*-
"""
Un distribuidor de material eléctrico vende alambre en rollos de 500, 300 y 75 metros. Realizar un
programa que ingrese la longitud total de alambre en metros que requiere el usuario, y que
imprima el número de rollos de alambre de 500, 300 y 75 metros correspondientes y el número de
metros de alambre faltante.
"""
a = int(input("Cantidad de metros: "))
if a > 0:
    b = int(a/500)
    c = int(a%500)
    d = int(c/300)
    e = int(a%300)
    f = int(e/75)
    g = int(e%75)
    print(f"{b} rollos de 500 metros, {d} rollos de 300 metros, {f} rollos de 75 metros y {g} metros faltantes")
else:
    print("Ingrese un numero positivo mayor a cero")
    
    