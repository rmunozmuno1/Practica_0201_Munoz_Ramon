#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
Numero_de_muñecas= float (input('¿Cual es el número de muñecas?'))
Numero_de_payasos= float (input('¿Cual es el número de payasos?'))
Peso_total_de_las_muñecas= Numero_de_muñecas * 75      ### Peso de las muñecas
Peso_total_de_los_payasos= Numero_de_payasos * 112     ### Peso de los payasos
Peso_del_Paquete= Peso_total_de_los_payasos + Peso_total_de_las_muñecas
print (Peso_del_Paquete)