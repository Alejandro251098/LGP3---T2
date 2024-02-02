def convertir_moneda(monto, tasa_cambio):
    return monto * tasa_cambio

def main():
    print("¡Bienvenido al conversor de monedas!")

    
    moneda_origen = input("Ingrese la moneda de origen: ")
    monto_origen = float(input("Ingrese el monto a convertir: "))

    
    moneda_destino = input("Ingrese la moneda de destino: ")

    
    respuesta = input("¿Desea utilizar una tasa de cambio personalizada? (s/n): ")
    if respuesta.lower() == "s":
        tasa_personalizada = float(input("Ingrese la tasa de cambio personalizada: "))
        resultado = convertir_moneda(monto_origen, tasa_personalizada)
        print(f"{monto_origen} {moneda_origen} equivale a {resultado} {moneda_destino} (utilizando la tasa personalizada).")
    else:
        
        print("Usando tasas de cambio actuales...")

        
        tasas_cambio = {"USD-EUR": 0.85, "EUR-COP": 4226.77, "USD-MXN": 17.06}

        
        clave = f"{moneda_origen.upper()}-{moneda_destino.upper()}"
        if clave in tasas_cambio:
            tasa_cambio = tasas_cambio[clave]
            resultado = convertir_moneda(monto_origen, tasa_cambio)
            print(f"{monto_origen} {moneda_origen} equivale a {resultado} {moneda_destino}.")
        else:
            print("Lo siento, no es posible realizar esta conversión. Las tasas de cambio no están disponibles.")

if __name__ == "__main__":
    main()
