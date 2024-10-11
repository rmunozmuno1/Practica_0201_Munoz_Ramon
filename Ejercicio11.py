#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. 
Pan_Pasado= int(input('¿Cuanto pan pasado se vendido?'))
a = float(Pan_Pasado)
b = (3.49)
c = (60)
Dinero_Total = ((a * b * c) / 100)
round (Dinero_Total, 2)
print (f"Una barra de pan normal cuesta {b}")
print (f"La compra total por haber comprado barras que estan pasadas es de {Dinero_Total}")