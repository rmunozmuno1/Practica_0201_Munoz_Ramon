#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = int(input('Intorduce un numero entero'))
m = int(input('Introduce otro numero entero'))
#Calculamos
cociente= n//m
resto = n % m
print ("{n} entre {m} da un cociente {cociente} y un resto {resto}")