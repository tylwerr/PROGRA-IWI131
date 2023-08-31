def avistamientos_por_región(nombre_archivo):
    archivo = open(nombre_archivo,'r',encoding='utf8') # lo del "encoding" (lo vi de piazza) es para que me abriera el archivo (tuve problemas con que no abría o tenía carácteres extraños)
    archivos_creados = 0
    diccionario_region = {}     # diccionario para ordenar datos por región

    for linea in archivo:
        lista_datos = linea.strip().split(';')
        
        if 'año-mes' not in lista_datos:    # con esto descarto la primera línea
            año_mes = lista_datos[0]
            region = lista_datos[1]
            casos_confirmados = lista_datos[3]
            casos_totales = lista_datos[2]

            # agregamos los datos de las regiones, excluímos las que no tengan registros
            if region not in diccionario_region and casos_totales != '0':
                diccionario_region[region] = [[año_mes,casos_confirmados,casos_totales]]
            elif region in diccionario_region and casos_totales != '0':
                diccionario_region[region].append([año_mes,casos_confirmados,casos_totales])
    
    # recorremos el diccionario creando los archivos
    for region2 in diccionario_region:
        nombre_archivo_nuevo = region2 + '.txt'
        porcentajes_datos = []    # estas dos listas son para ordenar y tener los 3 mayores

        # creamos el archivo
        archivo_nuevo = open(nombre_archivo_nuevo,'w')

        for listas in diccionario_region[region2]:

            # extraigo la información del diccionario
            año_mes = listas[0].split('-')
            año = año_mes[0]
            mes = año_mes[1]
            casos_confirmados = int(listas[1])
            casos_totales = int(listas[2])

            # calculo del porcentaje
            porcentaje = round(((casos_confirmados/casos_totales)*100),2)
            casos_totales = str(casos_totales)
            porcentajes_datos.append((porcentaje,año,mes,casos_totales))

        porcentajes_datos.sort()    # ordenamos y luego sacamos los 3 primeros para dejarlos en el archivo nuevo 
        porcentajes_datos.reverse()

        i = 0
        while i < len(porcentajes_datos):
            if i <= 2:
                texto = 'En el mes '+porcentajes_datos[i][2]+' de '+porcentajes_datos[i][1]+' hubo '+str(porcentajes_datos[i][0])+'% de avistamientos confirmados de un total de '+porcentajes_datos[i][3]+'\n'
                archivo_nuevo.write(texto)
            i += 1

        archivo_nuevo.close()
        archivos_creados += 1

    archivo.close()
    return archivos_creados


# casos de prueba
#print(avistamientos_por_región('ovnis_chico.csv'))
#print(avistamientos_por_región('ovnis_mediano.csv'))
print(avistamientos_por_región('ovnis_grande.csv'))