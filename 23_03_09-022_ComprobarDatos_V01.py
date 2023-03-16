#Jaime Santiago Garci­a
#No. de registro: 20310369
#Practica #22

#---------------------------------------------------------------------------------------------

# Se solicita al usuario que ingrese un color y se almacena en la variable colorseleccionado
colorseleccionado = input('Elige un color porfavor: ')

# Se define una tupla de colores
tupla_de_colores = ('rojo', 'azul', 'verde', 'morado')

# Se utiliza una estructura condicional if-elif-else para verificar si el color seleccionado está en la tupla de colores
if colorseleccionado in tupla_de_colores[0]:
    # Si el color seleccionado es 'rojo', se imprime este mensaje
    print('El color rojo si está en la tupla')
elif colorseleccionado in tupla_de_colores[1]:
    # Si el color seleccionado es 'azul', se imprime este mensaje
    print('El color azul si está en la tupla')
elif colorseleccionado in tupla_de_colores[2]:
    # Si el color seleccionado es 'verde', se imprime este mensaje
    print('El color verde si está en la tupla')
elif colorseleccionado in tupla_de_colores[3]:
    # Si el color seleccionado es 'morado', se imprime este mensaje
    print('El color morado si está en la tupla')
else:
    # Si el color seleccionado no se encuentra en la tupla de colores, se imprime este mensaje
    print('Lo siento el color no está en nuestra tupla')
