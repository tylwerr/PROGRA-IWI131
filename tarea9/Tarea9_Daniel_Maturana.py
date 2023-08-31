#diccionario vacunas
vacunas = {
 "Sinovac":["11.111.111-1", "12.345.678-9"],
 "Pfizer": ["8.978.657-3"],
 "CanSino": ["13.789.456-k"]
}

#diccionario dosis (Valor: [edad,fecha1] o [edad,fecha1,fecha2])
dosis = {
 "11.111.111-1":[55,(2021,4,11),(2021,5,10)],
 "12.345.678-9":[47,(2021,6,3)],
 "8.978.657-3":[79,(2021,3,23)],
 "13.789.456-k":[40,(2021,5,18),(2021,6,10)]
}

#diccionario edades (así determinamos la edad con más vacunados)
edades = {}

dia = int(input('Día: '))
mes = int(input('Mes: '))
año = int(input('Año: '))
continuar = True

while continuar:
    rut = input('RUT: ')

    #Si el rut no se encuentra pedimos edad y vacuna a ponerse
    if rut not in dosis:    
        edad = int(input('Edad: '))
        vacuna = input('Tipo de vacuna: ')

        #agregar a la lista dosis la persona vacunada
        dosis[rut] = [edad,(año,mes,dia)]

        #Si la vacuna puesta existe, agregamos al rut a la vacuna correspondiente
        if vacuna in vacunas:
            vacunas[vacuna].append(rut)

        #si no existe, agregamos la nueva vacuna y el rut
        else:
            vacunas[vacuna] = []
            vacunas[vacuna].append(rut)

    #determinamos la vacuna para ponerse la segunda dosis
    else:
        #Si tiene una dosis, se agrega la fecha de la segunda dosis
        if len(dosis[rut]) == 2:
            dosis[rut].append((año,mes,dia))

        #recorremos diccionario vacunas y luego la lista de ruts, así encontramos la vacuna puesta
        for vacuna_llave in vacunas:
            for rut_buscado in vacunas[vacuna_llave]:
                if rut == rut_buscado:
                    print('Segunda dosis. Paciente debe ser inoculado con:',vacuna_llave)


    #Determinar la continuación del ciclo
    respuesta = input('¿Desea continuar? (s/n): ')
    if respuesta == 'n':
        print(' ')
        continuar = False


#agregamos las edades con ambas dosis al diccionario creado
for rut_llave in dosis:
    if len(dosis[rut_llave]) == 3:
        if dosis[rut_llave][0] not in edades:
            edades[dosis[rut_llave][0]] = 0
        edades[dosis[rut_llave][0]] += 1

#creamos una lista para ordenarla al final con tuplas
print('Edades con más personas con esquema de inoculación completo:')
edades_ordenadas = []
for nuevo_mayor in edades:
    tupla_ordenada = (edades[nuevo_mayor],nuevo_mayor)
    edades_ordenadas.append(tupla_ordenada)
edades_ordenadas.sort()

#contador para extraer los tres primeros con más vacunados de segunda dosis
i = 0
while i < len(edades_ordenadas):
    i += 1
print(edades_ordenadas[i-1][1],'años:',edades_ordenadas[i-1][0],'personas')
print(edades_ordenadas[i-2][1],'años:',edades_ordenadas[i-2][0],'personas')
print(edades_ordenadas[i-3][1],'años:',edades_ordenadas[i-3][0],'personas')