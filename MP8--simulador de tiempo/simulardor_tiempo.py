import random

def generar_informacion_meteorologica():
    temperatura = random.randint(-10, 40)  
    humedad = random.randint(0, 100)  
    estado_del_tiempo = random.choice(["Despejado", "Nublado", "Lluvioso", "Tormentoso", "Neblinoso"])

    return temperatura, humedad, estado_del_tiempo

def mostrar_informacion_meteorologica(ciudad, temperatura, humedad, estado_del_tiempo):
    print(f"Información meteorológica para {ciudad}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Humedad: {humedad}%")
    print(f"Estado del tiempo: {estado_del_tiempo}")

def main():
    ciudad = input("Ingrese el nombre de la ciudad: ")

    
    temperatura, humedad, estado_del_tiempo = generar_informacion_meteorologica()


    mostrar_informacion_meteorologica(ciudad, temperatura, humedad, estado_del_tiempo)

if __name__ == "__main__":
    main()
