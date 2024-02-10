# se importa la libreria random para usarlo en la funcion que generara los datos para la infirmacion que se pida 
import random

# funcion creada para dar informacion metereologica de diferentes ciudades dando datos random de temperatura ,humedad y estado del tiempo 
def generar_informacion_meteorologica():
    temperatura = random.randint(-10, 40)  
    humedad = random.randint(0, 100)  
    estado_del_tiempo = random.choice(["Despejado", "Nublado", "Lluvioso", "Tormentoso", "Neblinoso"])

    return temperatura, humedad, estado_del_tiempo

# funcion para mostrar los diferentes datos para las ciudades  mostrando el nombre de la ciudad y sus datos sobre el clima
def mostrar_informacion_meteorologica(ciudad, temperatura, humedad, estado_del_tiempo):
    print(f"Información meteorológica para {ciudad}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Humedad: {humedad}%")
    print(f"Estado del tiempo: {estado_del_tiempo}")

# input para ingresar el nombre de la ciudad que queramos saber sus datos meterologicos y los imprima en consola
def main():
    ciudad = input("Ingrese el nombre de la ciudad: ")

    
    temperatura, humedad, estado_del_tiempo = generar_informacion_meteorologica()


    mostrar_informacion_meteorologica(ciudad, temperatura, humedad, estado_del_tiempo)

if __name__ == "__main__":
    main()
