#Jaime Santiago Garci­a
#No. de registro: 20310369
#Practica #24

#---------------------------------------------------------------------------------------------

# Inicialización de la variable x con un valor de 0
x = 0 

# Mientras x sea menor o igual a 30, el bucle se ejecutará
while x <= 30:
	# Se incrementa el valor de x en 1 en cada iteración
	x += 1

	# Se verifica si el valor actual de x es igual a 4, 6 o 10
	if x == 4 or x == 6 or x == 10:
		# Si x es igual a 4, 6 o 10, se imprime un mensaje indicando que se saltó ese valor
		print('Se saltó el valor ', x, ' de x')
		# La instrucción 'continue' hace que se salte el resto del código en esta iteración y se pase a la siguiente
		continue

	# Se verifica si el valor actual de x es igual a 15
	if x == 15:
		# Si x es igual a 15, se imprime un mensaje indicando que se rompió la ejecución del bucle
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		# La instrucción 'break' hace que se salga del bucle inmediatamente
		break
	
	# Si no se cumple ninguna de las condiciones anteriores, se imprime el valor actual de x
	print(x)
