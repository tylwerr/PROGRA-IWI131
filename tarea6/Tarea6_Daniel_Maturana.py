#Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<
#<3*corazon$:-D*cara feliz$>.<*incomodo$
textoOriginal = input('Ingrese texto: ')
significado = input('Ingrese significado: ')

#aumento: variable para avanzar y rebanar lo correspondiente
aumento = 0
i = 0
#recorremos el string significado
while i < len(significado):
    if significado[i] == '*':
        #tenemos el emoji
        emoji = significado[aumento:i]
        aumento = i + 1

    elif significado[i] == '$':
        #tenemos la palabra que representa al emoji
        palabraEmoji = significado[aumento:i]
        palabraEmoji = palabraEmoji.upper()
        aumento = i + 1

        #recorre textoOriginal
        contador = 0
        nuevoTexto = ''
        while contador < len(textoOriginal):
            #si se encuentran los emojis en el textoOriginal, se reemplazan
            if emoji in textoOriginal:
                if textoOriginal[contador:contador+len(emoji)] == emoji:
                    #se cambia el emoji por el significado
                    nuevoTexto += palabraEmoji
                    contador += len(emoji)

                else:
                    #agrega letras del textoOriginal
                    nuevoTexto += textoOriginal[contador]
                    contador += 1

        textoOriginal = nuevoTexto
            
    i += 1

print('Texto traducido: ',nuevoTexto)