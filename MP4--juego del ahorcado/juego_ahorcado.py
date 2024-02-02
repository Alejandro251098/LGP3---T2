import random

def inicializar_juego(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    letras_erroneas = []
    return tablero, palabra, letras_erroneas

def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if letras_erroneas:
        print('Letras erróneas:', ', '.join(letras_erroneas))
        print()

def pedir_letra(tablero, letras_erroneas):
    letra = input('Introduce una letra (a-z): ').lower()
    while letra in letras_erroneas or letra in tablero:
        if letra in letras_erroneas:
            print('Letra repetida, prueba con otra.')
        elif letra in tablero:
            print('Esa letra ya ha sido adivinada.')
        letra = input('Introduce una letra (a-z): ').lower()
    return letra

def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('¡Genial! Has acertado una letra.')
        for i, letra_palabra in enumerate(palabra):
            if letra_palabra == letra:
                tablero[i] = letra
    else:
        print('¡Oh! Has fallado.')
        letras_erroneas.append(letra)

def comprobar_palabra(tablero, palabra):
    return '_' not in tablero

def jugar_al_ahorcado(diccionario):
    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)
    while len(letras_erroneas) < 7:
        mostrar_tablero(tablero, letras_erroneas)
        letra = pedir_letra(tablero, letras_erroneas)
        procesar_letra(letra, palabra, tablero, letras_erroneas)
        if comprobar_palabra(tablero, palabra):
            print('¡Enhorabuena, lo has logrado!')
            break
    else:
        print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
        mostrar_tablero(tablero, letras_erroneas)

diccionario = ['casa', 'perro', 'gato', 'arbol', 'casa']
jugar_al_ahorcado(diccionario)