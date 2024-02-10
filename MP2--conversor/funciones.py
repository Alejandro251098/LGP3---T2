# en este archivo solo estan guardadas la funciones q le daran funcion al conversor de unidades

def menu(unidades):
    i = 1
    for opcion, cantidad in unidades.items():
        print(f"{i}. {cantidad} | Opc: {opcion}")
        i += 1
    return unidades 


def convertidor():
    print("\n|-----------------------|")
    while True:
        try:
            unidad = float(input("\ningrese la cantidad: "))
            return unidad
        except ValueError:
            print("\ningrese un valor valido.")


def print_result(resultado):
    print(f"\nResultado:\n{resultado}")
    print("\n|-----------------------|\n")


def metro_cm(cantidad):
    resultado = cantidad * 100
    return f"{cantidad}m es igual a: {resultado}cm"


def KilometroHora_MetroSegun(cantidad):
    resultado = cantidad / 3.6
    return f"{cantidad}km/h es igual a:{resultado}m/s"



def kilogramo_gramo(cantidad):
    resultado = cantidad * 1000
    return f"{cantidad}kg es igual a: {resultado}g"


def liter_ml(cantidad):
    resultado = cantidad * 1000
    return f"{cantidad}L es igual a: {resultado}mL"


def hora_min(cantidad):
    resultado = cantidad * 60
    return f"{cantidad}h es igual a: {resultado}min"


def celsios_farenheit(cantidad):
    resultado = cantidad * (9/5) + 32
    return f"{cantidad}°C es igual a: {resultado}°F"