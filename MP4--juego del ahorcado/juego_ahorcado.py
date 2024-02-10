# se importa la libreria random
import random

# inicia el juego usando random para escoger una palabra aleatoria de una lista dada
# y segun la cantidad de letras imprime las casillas ,ademas en esta funcion se guardaran las letras erroneas en una lista 
def inicializar_juego(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    letras_erroneas = []
    return tablero, palabra, letras_erroneas

# nos muestra el tablero segun la longitud de la palabra q debemos adivinar , ademas imprime en una lista de letras erroneas las letras q se dan y 
# no corresponden a las letras  de la palabra que debemos adivinar
def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if letras_erroneas:
        print('Letras erróneas:', ', '.join(letras_erroneas))
        print()

#fucion que permite abrir un input para pedir la letra q queramos ingresar , la compare con la lista de letras erroneas  y con las letras de la palabra 
# para adivinar , si la letra esta en algunas de las lista nos devolvera un mensaje correspondiente
def pedir_letra(tablero, letras_erroneas):
    letra = input('Introduce una letra (a-z): ').lower()
    while letra in letras_erroneas or letra in tablero:
        if letra in letras_erroneas:
            print('Letra repetida, prueba con otra.')
        elif letra in tablero:
            print('Esa letra ya ha sido adivinada.')
        letra = input('Introduce una letra (a-z): ').lower()
    return letra

# funcion que verifica si  las letras ingresadas corresponden a la palabra que debemos adivinar si es asi  nos devolvera un mensaje de felicitacion
# y si no con devuleve un ensaje de falla
def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('¡Genial! Has acertado una letra.')
        for i, letra_palabra in enumerate(palabra):
            if letra_palabra == letra:
                tablero[i] = letra
    else:
        print('¡Oh! Has fallado.')
        letras_erroneas.append(letra)
        
# comprueba la palabra y genera un table del tamaño de la palabra que debemos adivinar  sin mostrar la palabra solo guiones bajos 
def comprobar_palabra(tablero, palabra):
    return '_' not in tablero

# funcion para jugar donde se llama las demas funciones que escogen la palabra genran el tablero y cuentas la cantidad de intentos hasta llegar a 7
# si nos pasamos de 7 palabras erroneas  nos saldra un mensaje que hemos perdido pero si logramos aidvinar nos imprime un mensaje de felicitacion
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

# lista que contiene las palabras que el juego usara aleatoreamente
diccionario = ['casa', 'perro', 'gato', 'arbol', 'casa','programacion', 'python']
jugar_al_ahorcado(diccionario)