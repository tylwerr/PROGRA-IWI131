##########################################
#                                        #
#  Programe sus funciones aquí           #
#                                        #
##########################################

def disparo(tablero, barcos, fila, columna):
    i = 0
    flag = True
    while i < len(barcos) and flag:
        #Extracción de los datos de los barcos mediante ciclo
        largo_barco = barcos[i][0]
        orientacion_barco = barcos[i][1]
        fila_barco = barcos[i][2]
        columna_barco = barcos[i][3]

        #Comprobar la orientación para luego comprobar que es la fila o columna del barco y cambiar a 'O'
        if orientacion_barco == 1:
            fila_barco_final = list(range(fila_barco,fila_barco+largo_barco))
            if (fila in fila_barco_final) and (columna == columna_barco):
                tablero[fila][columna] = 'O'
                flag = False

        elif orientacion_barco == 2:
            columna_barco_final = list(range(columna_barco,columna_barco+largo_barco))
            if (fila == fila_barco) and (columna in columna_barco_final):
                tablero[fila][columna] = 'O'
                flag = False

        i += 1
    #Si no es la ubicación del barco, entonces es agua
    if flag:
        tablero[fila][columna] = ' '


def destruidos(tablero, barcos):
    i2 = 0
    flag2 = True
    contador = 0
    while i2 < len(barcos) and flag2:
        #Extracción de datos de los barcos mediante ciclo
        largo_barco2 = barcos[i2][0]
        orientacion_barco2 = barcos[i2][1]
        fila_barco2 = barcos[i2][2]
        columna_barco2 = barcos[i2][3]
        tamaño = largo_barco2-1 #variable que uso para ir comprobando que la fila o columna esté toda en 'O'

        itera = 0
        while itera < largo_barco2:
            #Comprobar la orientación para luego determinar si la fila o columna esté toda en 'O'
            #Luego se usa un ciclo for para cambiar todas las 'O' del barco por 'X'
            if orientacion_barco2 == 1:
                fila_barco_final2 = list(range(fila_barco2,fila_barco2+largo_barco2))
                if tablero[fila_barco2][columna_barco2] == 'O':
                    if tablero[(fila_barco2+tamaño)//2][columna_barco2] == 'O' and tablero[fila_barco2+tamaño][columna_barco2] == 'O':
                        contador +=1
                        for e in fila_barco_final2:
                            tablero[e][columna_barco2] = 'X'
                            flag2 = False

            elif orientacion_barco2 == 2:
                columna_barco_final2 = list(range(columna_barco2,columna_barco2+largo_barco2))
                if tablero[fila_barco2][(columna_barco2+tamaño)//2] == 'O':
                    if tablero[fila_barco2][columna_barco2+itera] == 'O' and tablero[fila_barco2][columna_barco2+tamaño] == 'O':
                        contador +=1
                        for e in columna_barco_final2:
                            tablero[fila_barco2][e] = 'X'
                            flag2 = False
            itera += 1
        i2 += 1
    
    #si no es el barco, suma 0
    if flag2:
        contador += 0
        return contador
    return contador


# OPCIONAL:
# Cambie el valor de esta variable a 1 si desea ver
# la ubicación de los barcos antes de comenzar.
# Esto puede ser útil para probar sus funciones.
mostrar_solucion = 1



##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")
