import random

# Listas de personajes, lugares y eventos
personajes = ["Juan", "María", "Pedro", "Ana", "Luisa"]
lugares = ["una ciudad", "un pueblo", "un castillo", "un bosque", "una isla"]
eventos = ["encontró un tesoro", "salvó al mundo", "se perdió en el bosque", "construyó una máquina del tiempo", "conquistó un reino"]

def generar_historia():
    personaje = random.eleccion(personajes)
    lugar = random.eleccion(lugares)
    evento = random.eleccion(eventos)

    return f"{personaje} estaba en {lugar} cuando {evento}."

def main():
    print("Generador de historias aleatorias")
    print("¿Qué tipo de historia deseas crear?")
    print("1. Historia de aventuras")
    print("2. Historia romántica")
    print("3. Historia de misterio")
    print("4. Salir")

    eleccion = input("Seleccione una opción: ")

    while eleccion != "4":
        if eleccion == "1":
            print("Historia de aventuras:")
            print(generar_historia())
        elif eleccion == "2":
            print("Historia romántica:")
            print(generar_historia())
        elif eleccion == "3":
            print("Historia de misterio:")
            print(generar_historia())
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        eleccion = input("\nSeleccione otra opción o 4 para salir: ")

    print("Saliendo del programa...")

if __name__ == "__main__":
    main()
