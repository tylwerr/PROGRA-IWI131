#Se solicitan los inputs, si el rango es correcto, el programa sigue, si no, lo cierra con un error(se encuentran al final)
valor = int(input('Valor propiedad en UF (1500-13000): '))
if (valor > 1499) and (valor < 12999):
    pie = int(input('Ingrese % del Pie (20%-40%): '))

    if (pie >= 20) and (pie <= 45):
        plazo = int(input('Ingrese Plazo (20, 25, 30): '))

        if (plazo == 20 or plazo == 25 or plazo == 30):
            tipo = int(input('Tipo de vivienda Casa(1) o Departamento(2): '))

            if (tipo == 1 or tipo == 2):
                estado = int(input('Estado vivienda Nueva(1) o Usada(2): '))

                if (estado == 1 or estado == 2):
                    
                    #transformación pie % a decimal
                    pie = pie/100

                    #cálculo del valor UF y variable seguros
                    valor = valor-(valor*pie)
                    seguros = 0.5
                    if (tipo == 1 and estado == 1):
                        seguros += 0.8
                    elif (tipo == 2 and estado == 1):
                        seguros += 0.8 + 0.3
                    elif (tipo == 2 and estado == 2):
                        seguros += 0.3

                    #plazos y porcentaje a cobrar de interés
                    #20 años Nueva
                    if (plazo == 20) and (estado == 1):
                        if (tipo == 1):
                            porcentaje = 25
                        elif (tipo == 2):
                            porcentaje = 28
                    #20 años Usada
                    elif (plazo == 20) and (estado == 2):
                        if (tipo == 1):
                            porcentaje = 22
                        elif (tipo == 2):
                            porcentaje = 26
                    #25 años Nueva
                    elif (plazo == 25) and (estado == 1):
                        if (tipo == 1):
                            porcentaje = 30
                        elif (tipo == 2):
                            porcentaje = 33
                    #25 años Usada
                    elif (plazo == 25) and (estado == 2):
                        if (tipo == 1):
                            porcentaje = 27
                        elif (tipo == 2):
                            porcentaje = 32
                    #30 años Nueva
                    elif (plazo == 30) and (estado == 1):
                        if (tipo == 1):
                            porcentaje = 35
                        elif (tipo == 2):
                            porcentaje = 41
                    #30 años Usada
                    elif (plazo == 30) and (estado == 2):
                        if (tipo == 1):
                            porcentaje = 31
                        elif (tipo == 2):
                            porcentaje = 37

                    #cálculos de interés, total y dividendo mensual
                    interes = valor*(porcentaje/100)
                    seguros = seguros*12*plazo
                    total = round(valor + interes + seguros,2)
                    dividendo = round(total/(12*plazo),2)
                    print('Total del crédito a pagar',total,'UF')
                    print('Dividendo mensual de',dividendo,'UF')

                else:
                    print('Estado vivienda inválido')
            else:
                print('Tipo vivienda inválido')
        else:
            print('Plazo inválido')
    else:
        print('Error: Pie fuera de rango')
else:
    print('Error: Valor fuera de rango')