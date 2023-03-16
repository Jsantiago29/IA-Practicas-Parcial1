#Jaime Santiago Garci­a
#No. de registro: 20310369
#Practica #21

#---------------------------------------------------------------------------------------------

# Se solicita al usuario que ingrese su edad y se convierte en un entero usando la función int()
edad = int(input('¿Cuál es tu edad?\n'))

# Se utiliza una estructura condicional if-elif-else para evaluar la edad ingresada
if edad <= 0:
	# Si la edad es menor o igual a cero, se imprime este mensaje
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	# Si la edad está entre 1 y 18, se imprime este mensaje
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	# Si la edad está entre 18 y 45, se imprime este mensaje
    print('Tienes una edad entre 18 y 45')
elif edad >= 18 and edad <= 100:
	# Si la edad está entre 18 y 100, se imprime este mensaje
	print('Eres mayor de edad.')
elif edad >= 100 and edad <= 120:
	# Si la edad está entre 100 y 120, se imprime este mensaje
    print('Tienes entre 100 y 120')
else:
	# Si la edad no se encuentra en ninguno de los rangos anteriores, se imprime este mensaje
	print('Edad no válida.')
