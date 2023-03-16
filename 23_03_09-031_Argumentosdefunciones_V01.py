#Jaime Santiago Garci­a
#No. de registro: 20310369
#Practica #31

#-----------------------------------------------------------------------------------------

# Definición de la función "colores" que toma un número variable de argumentos utilizando el operador "*args"
def colores(*args):
	pass

# Llamadas a la función "colores" con diferentes argumentos
colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

# La primera llamada a la función "colores" tiene 4 argumentos
# La segunda llamada a la función "colores" tiene 3 argumentos
# La tercera llamada a la función "colores" tiene 1 argumento
# La cuarta llamada a la función "colores" tiene 2 argumentos

#____________________________________________________________________________________________

# Definición de la función "colores" que toma un número variable de argumentos utilizando el operador "*args"
def colores(*args):
	# Se imprime un mensaje que utiliza los argumentos en posiciones específicas
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

# Llamada a la función "colores" con dos argumentos
colores('blanco', 'rojo')

#________________________________________________________________________________________________

# Definición de la función "sumas" que toma un número variable de argumentos utilizando el operador "*args"
def sumas(*args):
	# Se suman los cinco primeros argumentos y se almacena el resultado en la variable "resultado"
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	# Se imprime el resultado de la suma
	print('El resultado de sumar estos cinco números es:', resultado)

# Llamada a la función "sumas" con seis argumentos
sumas(10, 7, 89, 29, 12, 11)
