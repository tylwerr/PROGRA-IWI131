#input de las variables, usuario introduce lo que comió Grogu
neNu = float(input('Nevarro Numies consumidas (unidades):'))
spaSo = float(input('Space Soup consumida (en[ml]):'))
carne = float(input('Carne de Rana consumida (en[g]):'))

#desarrollo de las Nevarro Numies
neNu = (neNu * 11) #las nevarro consumidas se multiplican por 11(g)
grasasNe = (neNu * 1.90) / 11 #lo anterior se multiplica según cada (g)y se divide en 11
carboNe = (neNu* 6.00) / 11
proteNe = (neNu * 0.80) / 11
calo = (grasasNe * 9) #según los valores anteriores, se multiplican por sus calorías
calo += (carboNe * 4)
calo += (proteNe * 4)
#se acumulan las calorías obtenidas

#desarrollo de la SpaceSoup
grasasSpa = (spaSo * 10.0) / 285 #los ml consumidos se multiplican según cada (g)y se dividien en 285
carboSpa = (spaSo * 12.0) / 285
proteSpa = (spaSo * 11.0) / 285
calo += (grasasSpa * 9) #según los valores anteriores, se multiplican por sus calorías
calo += (carboSpa * 4)
calo += (proteSpa * 4)
#se acumulan las calorías obtenidas

#desarrollo de la Carne de Rana
grasasRa = (carne * 0.30) / 100 #la carne consumida se multiplica según cada (g) y se dividen en 100
carboRa = (carne * 0.00) / 100
proteRa = (carne * 16.0) / 100
calo += (grasasRa * 9) #según los valores obtenidos, se multiplican por sus calorías
calo += (carboRa * 4)
calo += (proteRa * 4)
#se acumulan las calorías obtenidas

#desarrollo suma total de los tres alimentos
grasasTotal = round(grasasNe + grasasSpa + grasasRa, 2) #se suman todas las grasas obtenidas de los 3 alimentos, redondea a 2 dígitos
carbohidratosTotal = round(carboNe + carboSpa + carboRa, 2) #se suman todos los carbohidratos obtenidos de los 3 alimentos, redondea a 2 dígitos
proteínasTotal = round(proteNe + proteSpa + proteRa, 2) #se suman todas las proteínas obtenidas de los 3 alimentos, redondea a 2 dígitos
calo = round(calo) #se acumularon las calorías de cada alimento, redondea al entero más cercano

#print de los resultados; muestra grasas, carbohidratos, proteínas y calorías consumidas
print('Grogu ha consumido:')
print(grasasTotal,'[g] de grasas')
print(carbohidratosTotal,'[g] de carbohidratos')
print(proteínasTotal,'[g] de proteínas')
print('Dando un total de:')
print(calo,'[calorías]')

'''
Casos de prueba
Caso 1
Entrada: 2400 nevarro  1 ml de space soup  809 g de carne rana

Salida:
grasa: 4562.46[g]
carbo: 14400.04[g]
prote: 2049.48[g]
calorías: 106860

Caso 2
Entrada: 40 nevarro  10 ml de space soup  0 g de carne rana

Salida:
grasa: 76.35[g]
carbo: 240.42[g]
prote: 32.39[g]
calorías: 1778

Caso 3
Entrada: 0 nevarro  0 ml de sapce soup  50 g de carne rana

Salida:
grasa: 0.15 [g]
carbo: 0 [g]
prote: 8 [g]
calorías: 33
'''
