# galeria random que se usara para randomizar las preguntas que estan ingresadas en lo siguiente diccionario
import random

# variable preguntas con el diccionarios que contienes las preguntas y respuestas 
preguntas = {
    "Ciencia": [
        {"pregunta": "¿Cuál es la capital de colombia?", "respuesta": "bogota"},
        {"pregunta": "¿Cuál es el símbolo químico del agua?", "respuesta": "H2O"},
        {"pregunta": "¿Quién descubrió la ley de la gravedad?", "respuesta": "Isaac Newton"}
    ],
    "tecnologia": [
        {"pregunta": "nombre un hardware de salida visual de un computador", "respuesta": "monitor"},
        {"pregunta": "¿cual es el hardware encargado de unir los componentes un mismo puntos y que se comuniquen entre si?", "respuesta": "tarjeta madre"},
        {"pregunta": "¿cual es el software mas importante en un computador ?", "respuesta": "sistema operativo"}
    ],
    "programacion": [
        {"pregunta": "porque a un lenguaje de programacion se le llama de alto nivel", "respuesta": "porque su escritura es mas cercana al lenguaje humano"},
        {"pregunta": "¿HTML y CSS son lenguajes de programacion?", "respuesta": "no, son lenguajes de estructura"},
        {"pregunta": "¿cual es el lenguaje de programacion mas usado para crear aplicaciones y desarrollo web?", "respuesta": "python"}
    ]
}
funcion que permite seleccionar la categoria  de las pregruntas ingresando a las preguntas que estan en la variable preguntas
def seleccionar_categoria():
    print("Selecciona una categoría:")
    for i, categoria in enumerate(preguntas.keys(), start=1):
        print(f"{i}. {categoria}")
    opcion = int(input("Ingrese el número de la categoría: "))
    categorias = list(preguntas.keys())
    if 1 <= opcion <= len(categorias):
        return categorias[opcion - 1]
    else:
        print("Categoría inválida.")
        return None
# funcion para jugar  que segun la catoria selleciona una pregunta random  y nos pide ingrear la respuesta correcta
# segun la respuesta ingresada nos devolvera una respuesa
def jugar():
    categoria = seleccionar_categoria()
    if categoria:
        pregunta = random.choice(preguntas[categoria])
        print(f"\nPregunta: {pregunta['pregunta']}")
        respuesta_usuario = input("Respuesta: ")
        if respuesta_usuario.lower() == pregunta["respuesta"].lower():
            print("¡Respuesta correcta!")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: {pregunta['respuesta']}")

# funcion main que genera un menu para interactuar con el juego y las demas funciones , sellecionando la categoria y permitir jugar 
def main():
    print("¡Bienvenido al juego de preguntas y respuestas!")
    while True:
        print("\n--- Menú ---")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
