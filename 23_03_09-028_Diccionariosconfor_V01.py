#Jaime Santiago Garci­a
#No. de registro: 20310369
#Practica #28

#---------------------------------------------------------------------------------------------

# Se define un diccionario llamado "teclado1" con tres pares clave-valor
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

# Se utiliza un bucle for para iterar a través de cada clave en el diccionario "teclado1"
# En cada iteración, se imprime la clave seguida del valor correspondiente utilizando concatenación de strings
for x in teclado1:
	print(x, '=', teclado1[x] + '.')
