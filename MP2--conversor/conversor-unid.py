# aqui esta todo el conversor como tal que importa las funciones y el diccionario de unidades
 
from unidades import unidades
from funciones import *

run = True
print("\n|-----------------------|")
print("|----CONVERTIDOR  DE UNIDADES-----|")
print("|-----------------------|")

while run:
    print("\n")
    menu(unidades)
    print("\nPRESIONA E PARA SALIR")
    eleccion_conver = input("\nescoge una opcion: ")

    if eleccion_conver.lower() == "m":
        unity = convertidor()
        result = metro_cm(unidad)
        print_result(result)
        
    elif eleccion_conver.lower() == "km/h":
        unidad =convertidor()
        result = KilometroHora_MetroSegun(unidad)
        print_result(result)    

    elif eleccion_conver.lower() == "kg":
        unidad = convertidor()
        result = kilogramo_gramo(unidad)
        print_result(result)

    elif eleccion_conver.lower() == "l":
        unidad = convertidor()
        result = liter_ml(unidad)
        print_result(result)

    elif eleccion_conver.lower() == "h":
        unidad = convertidor()
        result = hora_min(unidad)
        print_result(result)

    elif eleccion_conver.lower() == "c":
        unidad = convertidor()
        result = celsios_farenheit(unidad)
        print_result(result)

    elif eleccion_conver.lower() == "e":
        print("\n|-----------------------|")
        print("|---vuelve luego-----|")
        print("|-----------------------|")
        
        run = False
    else:
        print("\ningrese una opcion valida.")