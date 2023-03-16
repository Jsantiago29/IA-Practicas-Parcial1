#Jaime Santiago Garci­a
#No. de registro: 20310369
#Practica #13

#---------------------------------------------------------------------------------------------

# Creamos una lista llamada 'colores' con diez elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Eliminamos el segundo elemento de la lista (el elemento en el índice 1) y lo almacenamos en la variable 'color1'
color1 = colores.pop(1)

# Eliminamos el octavo elemento de la lista (el elemento en el índice 7) y lo almacenamos en la variable 'color2'
color2 = colores.pop(7)

# Creamos una nueva lista llamada 'colores_guardados' y agregamos los elementos eliminados 'color1' y 'color2' a ella
colores_guardados = [color1, color2]

# Imprimimos la lista de 'colores_guardados', que debería contener los elementos 'azul' y 'rosa'
print(colores_guardados)
