#Jaime Santiago Garci­a
#No. de registro: 20310369
#Practica #29

#-----------------------------------------------------------------------------------------

# Se definen dos diccionarios, teclado1 y teclado2, que representan dos teclados diferentes
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

# Se elimina el diccionario "teclado1" utilizando la función "del"
del teclado1

# Se eliminan dos claves del diccionario "teclado2" utilizando la palabra clave "del"
del teclado2['Categoría']
del teclado2['Precio']

# Se imprime el valor asociado con la clave "Modelo" del diccionario "teclado2" utilizando la función "print()"
print(teclado2['Modelo'])
