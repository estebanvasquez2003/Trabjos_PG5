# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:47:23 2022

@author: Familiar
"""

print("*************************")
print("CONVERSION DE UNIDADES")
print("*************************")
print("Hola usuario, para poder continuar con el programa siga con las siguientes instrucciones")
print("")
print("El siguiente programa tiene la capacidad de convertir unidades de temperatura, longitud y tiempo de acuerdo a la unidad que necesite transformar el usuario")
print("")
print("Para utilizar la función de temperatura, digite 1")
print("Para utilizar la función de longitud, digite 2")
print("Para utilizar la función de tiempo, digite 3")
a=int(input("Digite a continuación su elección: "))

def conversion(a):
    if a==1:
        print("")
        print("*****************************************")
        print("La función temperatura fue seleccionada")
        print("*****************************************")
        print("Para transformar:")
        print("De grados ºC a ºK, digite 1")
        print("De grados ºC a ºF, digite 2")
        print("De grados ºK a ºC, digite 3")
        print("De grados ºK a ºF, digite 4")
        print("De grados ºF a ºC, digite 5")
        print("De grados ºF a ºK, digite 6")
        b=int(input("Ingrese un valor: "))
        
        def temp(b):
            q=float(input("Ingrese la cantidad a transformar: "))
            if b==1:
                res=q+273.15
                print("")
                print(res,"ºK")
                
            if b==2:
                res=(q*9/5)+32
                print("")
                print(res,"ºF")
                
            if b==3:
                while q<0:
                    q=float(input("Error, los ºK no cuentan con números negativos. Inténtelo nuevamente: "))
                res=q-273.15
                print(res,"ºC")
                
            if b==4:
                while q<0:
                    q=float(input("Error, los ºK no cuentan con números negativos. Inténtelo nuevamente: "))
                res=(q-273.15)*9/5 + 32
                print(res,"ºF")
                
            if b==5:
                res=(q-32)*5/9
                print("")
                print(res,"ºC")
                
            if b==6:
                res=(q-32)*5/9 + 273.15
                print("")
                print(res,"ºK")
        temp(b)
    if a==2:
        print("")
        print("*****************************************")
        print("La función longitud fue seleccionada")
        print("*****************************************")
        print("La librería se encuentra dividida en 7 partes, las cuales contienen los respectivos valores para digitar y transformar la unidad deseada.")
        print("")
        print("A continuacion se mostrara las opciones para desplegar a la misma: ")
        print("")
        print("Para transformar unidades de Km, digite 1")
        print("Para transformar unidades de Hm, digite 2")
        print("Para transformar unidades de Dm, digite 3")
        print("Para transformar unidades de m,  digite 4")
        print("Para transformar unidades de dm, digite 5")
        print("Para transformar unidades de cm, digite 6")
        print("Para transformar unidades de mm, digite 7")
        b=int(input("Ingrese un valor: "))
        
        def libre(b):
            if b==1:
                print("******")
                print("DE Km A .....?")
                print("******")
                print("De Km a Hm, digite 1.1")
                print("De Km a Dm, digite 1.2")
                print("De Km a m,  digite 1.3")
                print("De Km a dm, digite 1.4")
                print("De Km a cm, digite 1.5")
                print("De Km a mm, digite 1.6")
            if b==2:
                print("******")
                print("DE Hm A .....?")
                print("******")
                print("De Hm a Km, digite 2.1")
                print("De Hm a Dm, digite 2.2")
                print("De Hm a m,  digite 2.3")
                print("De Hm a dm, digite 2.4")
                print("De Hm a cm, digite 2.5")
                print("De Hm a mm, digite 2.6")
            if b==3:
                print("******")
                print("DE Dm A .....?")
                print("******")
                print("De Dm a Km, digite 3.1")
                print("De Dm a Hm, digite 3.2")
                print("De Dm a m,  digite 3.3")
                print("De Dm a dm, digite 3.4")
                print("De Dm a cm, digite 3.5")
                print("De Dm a mm, digite 3.6")
            if b==4:
                print("******")
                print("DE m A .....?")
                print("******")
                print("De m a Km, digite 4.1")
                print("De m a Hm, digite 4.2")
                print("De m a Dm, digite 4.3")
                print("De m a dm, digite 4.4")
                print("De m a cm, digite 4.5")
                print("De m a mm, digite 4.6")
            if b==5:
                print("******")
                print("DE dm A .....?")
                print("******")
                print("De dm a Km, digite 5.1")
                print("De dm a Hm, digite 5.2")
                print("De dm a Dm, digite 5.3")
                print("De dm a m,  digite 5.4")
                print("De dm a cm, digite 5.5")
                print("De dm a mm, digite 5.6")
            if b==6:
                print("******")
                print("DE cm A .....")
                print("******")
                print("De cm a Km, digite 6.1")
                print("De cm a Hm, digite 6.2")
                print("De cm a Dm, digite 6.3")
                print("De cm a m,  digite 6.4")
                print("De cm a dm, digite 6.5")
                print("De cm a mm, digite 6.6")
            if b==7:
                print("******")
                print("DE mm A .....")
                print("******")
                print("De mm a Km, digite 7.1")
                print("De mm a Hm, digite 7.2")
                print("De mm a Dm, digite 7.3")
                print("De mm a m,  digite 7.4")
                print("De mm a dm, digite 7.5")
                print("De mm a cm, digite 7.6")
                
            h=float(input("Ingrese un valor: "))
            
            def long(h):
                z=float(input("Ingrese la cantidad a transformar: "))
                while z<=0:
                    z=float(input("Error, ingrese un valor válido: "))
                    
                if h==1.1:
                    res=z*10
                    print(res,"Hm")
                if h==1.2:
                    res=z*100
                    print(res,"Dm")
                if h==1.3:
                    res=z*1000
                    print(res,"m")
                if h==1.4:
                    res=z*10000
                    print(res,"dm")
                if h==1.5:
                    res=z*100000
                    print(res,"cm")
                if h==1.6:
                    res=z*1000000
                    print(res,"mm")
                    
                
                if h==2.1:
                     res=z/10
                     print(res,"Km")
                if h==2.2:
                     res=z*10
                     print(res,"Dm")
                if h==2.3:
                     res=z*100
                     print(res,"m")
                if h==2.4:
                     res=z*1000
                     print(res,"dm")
                if h==2.5:
                     res=z*10000
                     print(res,"cm")
                if h==2.6:
                     res=z*100000
                     print(res,"mm")
                     
                     
                if h==3.1:
                     res=z/100
                     print(res,"Km")
                if h==3.2:
                     res=z/10
                     print(res,"Hm")
                if h==3.3:
                     res=z*10
                     print(res,"m")
                if h==3.4:
                     res=z*100
                     print(res,"dm")
                if h==3.5:
                     res=z*1000
                     print(res,"cm")
                if h==3.6:
                     res=z*10000
                     print(res,"mm")
                     
                     
                if h==4.1:
                     res=z/1000
                     print(res,"Km")
                if h==4.2:
                     res=z/100
                     print(res,"Hm")
                if h==4.3:
                     res=z/10
                     print(res,"Dm")
                if h==4.4:
                     res=z*10
                     print(res,"dm")
                if h==4.5:
                     res=z*100
                     print(res,"cm")
                if h==4.6:
                     res=z*1000
                     print(res,"mm")
                     
                     
                if h==5.1:
                     res=z/10000
                     print(res,"Km")
                if h==5.2:
                     res=z/1000
                     print(res,"Hm")
                if h==5.3:
                     res=z/100
                     print(res,"Dm")
                if h==5.4:
                     res=z/10
                     print(res,"m")
                if h==5.5:
                     res=z*10
                     print(res,"cm")
                if h==5.6:
                     res=z*100
                     print(res,"mm")
                     
                
                if h==6.1:
                     res=z/100000
                     print(res,"Km")
                if h==6.2:
                     res=z/10000
                     print(res,"Hm")
                if h==6.3:
                     res=z/1000
                     print(res,"Dm")
                if h==6.4:
                     res=z/100
                     print(res,"m")
                if h==6.5:
                     res=z/10
                     print(res,"dm")
                if h==6.6:
                     res=z*10
                     print(res,"mm")
                     
                
                if h==7.1:
                     res=z/1000000
                     print(res,"Km")
                if h==7.2:
                     res=z/100000
                     print(res,"Hm")
                if h==7.3:
                     res=z/10000
                     print(res,"Dm")
                if h==7.4:
                     res=z/1000
                     print(res,"m")
                if h==7.5:
                     res=z/100
                     print(res,"dm")
                if h==7.6:
                     res=z/10
                     print(res,"cm")
            long(h)
        libre(b)
    if a==3:
        print("")
        print("*****************************************")
        print("La función tiempo fue seleccionada")
        print("*****************************************")
        print("Para transformar:")
        print("De segundos a minutos, digite 1")
        print("De segundos a horas, digite 2")
        print("De minutos a segundos, digite 3")
        print("De minutos a horas, digite 4")
        print("De horas a minutos, digite 5")
        print("De horas a segundos, digite 6")
        b=int(input("Ingrese un valor: "))
        
        def tiemp(b):
            z=float(input("Ingrese la cantidad a transformar: "))
            while z<=0:
                z=float(input("Error, ingrese un valor válido: "))
            if b==1:
                res=z/60
                print(res,"minuto/s")
            if b==2:
                res=z/3600
                print(res,"hora/s")
            if b==3:
                res=z*60
                print(res,"segundo/s")
            if b==4:
                res=z/60
                print(res,"hora/s")
            if b==5:
                res=z*60
                print(res,"minuto/s")
            if b==6:
                res=z*3600
                print(res,"segundo/s")
        tiemp(b)
conversion(a)
                    
           

    