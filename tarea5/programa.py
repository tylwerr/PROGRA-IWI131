def funcion_aritmetica(nota1, nota2, nota3):
    return round((nota1+nota2+nota3)/3)
def funcion_geometrica(nt1, nt2, nt3):
    return round((nt1*nt2*nt3)**(1/3))
def funcion_mediavuelta(no1, no2, no3):
    return round((no3*(funcion_aritmetica(no1, no2, no3))**2)**(1/3))
def funcion_aprueba(farit, fgeo, fvuel):
    if farit >= 55:
        return 1
    elif fgeo >= 55:
        return 2
    elif fvuel >= 55:
        return 3
    else:
        return 0

pedir_notas = True
while pedir_notas:
    ramo = input("Ingrese el nombre del ramo: ")

    if ramo == "salir":
        pedir_notas = False
        print("Fin del programa - Desarrollado por Kiwi :D!")
    else:
        n1 = int(input("Ingrese la 1era nota: "))
        n2 = int(input("Ingrese la 2era nota: "))
        n3 = int(input("Ingrese la 3era nota: "))

        nf_aritmetica = funcion_aritmetica(n1, n2, n3)
        nf_geometrica = funcion_geometrica(n1, n2, n3)
        nf_vuelta = funcion_mediavuelta(n1, n2, n3)

        print("Su nota final según la Media Aritmética es:", nf_aritmetica)
        print("Su nota final según la Media Geométrica es:", nf_geometrica)
        print("Su nota final según la Media Vuelta es:", nf_vuelta)

        nf_aprobacion = funcion_aprueba(nf_aritmetica, nf_geometrica, nf_vuelta)

        if nf_aprobacion == 0:
            print("Lamentablemente no puedes aprobar con ninguna de las fórmulas :'c")
        elif nf_aprobacion == 1:
            print("Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 2:
            print("Si la NF del ramo se calcula usando la Media Geométrica, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 3:
            print("Si la NF del ramo se calcula usando la Media Vuelta, entonces apruebas", ramo, ":D")