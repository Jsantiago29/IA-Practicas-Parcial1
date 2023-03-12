colorseleccionado = input('Elige un color porfavor: ')
tupla_de_colores = ('rojo', 'azul', 'verde', 'morado')

if colorseleccionado in tupla_de_colores[0]:
    print('El color rojo si  esta en la tupla')
elif colorseleccionado in tupla_de_colores[1]:
    print('El color azul si esta en la tupla')
elif colorseleccionado in tupla_de_colores[2]:
    print('El color verde si esta en la tupla')
elif colorseleccionado in tupla_de_colores[3]:
    print('El color morado si esta en la tupla')
else:
    print('Lo siento el color no está en nuestra tupla')
