#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y la ganancia final total.
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. 
Pan_Pasado= int(input('¿Cuanto pan pasado se vendido?'))
a = float(Pan_Pasado)
b = (3.49)
c = (60)
Dinero_Total = ((a * b * c) / 100)
round (Dinero_Total, 2)  ### Por alguna extraña razon no me lo redondea, he buscado soluciones pero no encuentro nada 
print (f"Una barra de pan normal cuesta {b}")
print (f"La compra total por haber comprado barras que estan pasadas es de {Dinero_Total}")