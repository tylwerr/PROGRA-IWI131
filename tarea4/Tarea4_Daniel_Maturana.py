from math import sqrt

#Solicita datos de entrada (nombre tienda y coordenadas)
tienda = str(input('Nombre sucursal 1: '))
coordenadaX = int(input('Coordenada x: '))
coordenadaY = int(input('Coordenada y: '))
tienda2 = str(input('Nombre sucursal 2: '))
coordenadaX2 = int(input('Coordenada x: '))
coordenadaY2 = int(input('Coordenada y: '))
tienda3 = str(input('Nombre sucursal 3: '))
coordenadaX3 = int(input('Coordenada x: '))
coordenadaY3 = int(input('Coordenada y: '))
print('')

#Ciclos (primero pedidos - segundo platos y sus precios)
otro = True
sumaPlata = 0
pedidoTienda = 0
pedidoTienda2 = 0
pedidoTienda3 = 0
while otro:
    plato = 0
    plata = 0
    while plato != -1:
        plato = int(input('Ingrese número del plato: '))
        if plato == 1:
            carne = 4000
            plata += carne
            sumaPlata += carne
        elif plato == 2:
            veget = 3000
            plata += veget
            sumaPlata += veget
        elif plato == 3:
            vegan = 3500
            plata += vegan
            sumaPlata += vegan
    print('Total del pedido $',plata)

    #distancia más cercana
    coordenadaCx = int(input('Ingrese coordenada x cliente: '))
    coordenadaCy = int(input('Ingrese coordenada y cliente: '))
    d1 = sqrt((coordenadaCx - coordenadaX)**2 + (coordenadaCy - coordenadaY)**2)
    d2 = sqrt((coordenadaCx - coordenadaX2)**2 + (coordenadaCy - coordenadaY2)**2)
    d3 = sqrt((coordenadaCx - coordenadaX3)**2 + (coordenadaCy - coordenadaY3)**2)
    if d1 < d2 and d1 < d3:
        print('Pedido será entregado por',tienda)
        pedidoTienda += 1
    elif d2 < d1 and d2 < d3:
        print('Pedido será entregado por',tienda2)
        pedidoTienda2 += 1
    elif d3 < d1 and d3 < d2:
        print('Pedido será entregado por',tienda3)
        pedidoTienda3 += 1
    
    #Pregunta por otro pedido
    otro = str(input('¿Desea registrar otro pedido?: '))
    print('')
    if otro == 'si':
        otro = True
    else:
        otro = False
        #Estadísticas finales
        print('#### Estadísticas Finales ####')
        print('Monto total recaudado $',sumaPlata)
        print(tienda,'entregó',pedidoTienda,'pedidos')
        print(tienda2,'entregó',pedidoTienda2,'pedidos')
        print(tienda3,'entregó',pedidoTienda3,'pedidos')