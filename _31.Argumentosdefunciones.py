def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

#Linea 4 son 4 argumentos
#Linea 5 son 3 argumentos
#Linea 6 son 1 argumentos
#Linea 7 son 2 argumentos
#____________________________________________________________________________________________

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('blanco', 'rojo')

#________________________________________________________________________________________________

def sumas(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

sumas(10, 7, 89, 29, 12, 11)