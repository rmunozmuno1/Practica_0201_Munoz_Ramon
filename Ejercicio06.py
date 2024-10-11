#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:
n= int(input('Introduzca un numero positivo'))
#Ponemos un IF para dar poner el caso de un numero que no sea positivo 
if n > 0:
    suma = n * (n + 1) // 2
    print (f"La suma de 1 hasta el numero introducido da {suma}")
#Ponemos el caso de que no haya puesto un numero positivo
else:
    print ("El numero introducido no es un numero postivo")