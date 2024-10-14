#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
Peso = float (input('¿Cual es tu peso en Kg?'))
Altura = float (input('¿Cual es tu altura en m')) ### El decimal se pone con punto
Altura = Altura ** 2
IMC = Peso / Altura
### He usado un comando que se llama "Round" para redondear ya que no he encontrado como hacerlo en los apuntes 
IMC = round(IMC,2) ### Ponemos round ("La variable" una coma y el numero de decimales que queremos)
print (IMC)