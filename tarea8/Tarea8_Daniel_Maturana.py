def obtener_valor_característica(características, buscada):
   #recorrimos la lista de tuplas
   for tupla in range(len(características)):
      #dentro de las tuplas buscamos la palabra
      if características[tupla][0] == buscada:
         return características[tupla][1]
   if buscada not in características:
      return 0

def puntaje_amigo(amigo, características):
   puntaje = 0
   for palabra in amigo[1]: #se llama la función para determianr el puntaje de la palabra
      palabra = palabra.lower()
      puntaje += obtener_valor_característica(características,palabra)
   return puntaje

#casos
características = [
('kawaii',10), ('leal',20), ('acusete',-10), ('avaro',-15), ('respetuoso',20),
('otaku',25),('lolero',25),('furro',-50),('vtuver',25),('mechero',-30)
]

amigos = [('Sneki',('leal','kawaii','vtuver')),
          ('Otaku-taku',('otaku','avaro','lolero','leal')),
          ('Maiga',('paciente','otaku','leal')),
          ('Mojojojo',('mechero','kawaii','Furro','lolero')),
          ('Seiya',('leal','acusete')),
          ('Vegeta',('otaku','avaro')),
          ('Kalila',('lolero','kawaii')),
          ('Grogu',('avaro','kawaii','lolero','otaku')),
          ('Freezer',('acusete','furro','otaku','lolero'))
]

#programa
print('Equipo seleccionado:')
i = 0
loleros = []
while i < len(amigos):
   #recorro la lista de tuplas "amigos" y desempaqueto esas tres variables
   amigo = amigos[i]
   nombre = amigos[i][0] + ','
   descripción = amigos[i][1]
   if 'lolero' in descripción: #si es lolero llamo a la función para calcular sus puntajes
      puntaje_real = puntaje_amigo(amigo,características)
      tupla_loleros = (puntaje_real,nombre) #creo una tupla solo para loleros, con el puntaje como primer elemento
      loleros.append(tupla_loleros) #agrego las tuplas anteriores a una lista que luego se le aplica un sort,
                                    #así obtengo quién es el mayor de los puntajes
   i += 1
loleros.sort()

#teniendo las tuplas con su puntaje primero y en una lista,
#recorro la lista, pero solo obtengo el último que sería el mayor puntaje
for i2 in range(len(loleros)):
   puntaje_final = loleros[i2][0]
   nombre_final = loleros[i2][1]
#las siguientes variables obtengo al segundo amigo con el puntaje más alto
puntaje_anterior = loleros[i2-1][0]
nombre_anterior = loleros[i2-1][1]
print(nombre_final,puntaje_final,"puntos")
print(nombre_anterior,puntaje_anterior,"puntos")