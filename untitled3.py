# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:38:16 2022

@author: Familiar
"""

fosforos=int(input("Ingrese la cantidad de fosforos producidos: "))
c=(fosforos/40)
p=((c*12)/12)
cs=(fosforos%c)
ps=(fosforos%p)
print("La cantidad de cajas es:",c, ",La cantidad de paquetes producidos es: ",p, "La cantidad de cajas sobrantes es: ",cs, "La cantidad de paquetes sobrantes es: ",ps)

