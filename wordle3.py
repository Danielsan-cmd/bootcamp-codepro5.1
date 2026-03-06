def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    cantidad_letras_de_palabra_a_encontrar = 5

    letras_verificadas = []

    for posicion in range(cantidad_letras_de_palabra_a_encontrar):

        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]

        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:
            letras_verificadas.append('[' + palabra_ingresada[posicion] + ']')

        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append('(' + palabra_ingresada[posicion] + ')')

        else:
            letras_verificadas.append(palabra_ingresada[posicion])

    return letras_verificadas

palabra_secreta = 'perro'
intentos = 3

while intentos > 0:

    palabra_del_usuario = input('ADIVINA LA PALABRA!! pista (5 letras): ')

    resultado = obtener_fila_verificada(palabra_secreta, palabra_del_usuario)

    print(resultado)

    if palabra_del_usuario == palabra_secreta:
        print('Que grandeee.. Ganastee!!!')
        break
    elif palabra_del_usuario != palabra_secreta:
        print('Palabra incorrecta.')

    else:
        intentos -= 1
        print('Intentos restantes:', intentos)


if intentos == 0:
    print('Ya no quedan intentos. Intentelo mas tarde.')