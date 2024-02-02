class Cinema:
    def __init__(datos, filas, asientos_x_fila):
        datos.filas = filas
        datos.asientos_x_fila = asientos_x_fila
        datos.planos_asientos = [['O' for _ in range(asientos_x_fila)] for _ in range(filas)]
        datos.asientos_disponibles = filas * asientos_x_fila

    def mostrar_asientos(datos):
        print("Plano de asientos:")
        for row in datos.planos_asientos:
            print(' '.join(row))
        print(f"Asientos disponibles: {datos.asientos_disponibles}")

    def reservar_asiento(datos, row, seat):
        if 1 <= row <= datos.filas and 1 <= seat <= datos.asientos_x_fila:
            if datos.planos_asientos[row - 1][seat - 1] == 'O':
                datos.planos_asientos[row - 1][seat - 1] = 'X'
                datos.asientos_disponibles -= 1
                print(f"Asiento {row}-{seat} reservado correctamente.")
            else:
                print("Lo siento, este asiento ya está ocupado.")
        else:
            print("Número de fila o asiento inválido.")

def main():
    filas = int(input("Ingrese el número de filas en el cine: "))
    asientos_x_fila = int(input("Ingrese el número de asientos por fila en el cine: "))

    cinema = Cinema(filas, asientos_x_fila)

    while True:
        print("\n--- Menú ---")
        print("1. Mostrar plano de asientos")
        print("2. Reservar asiento")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            cinema.mostrar_asientos()
        elif choice == "2":
            row = int(input("Ingrese el número de fila del asiento que desea reservar: "))
            seat = int(input("Ingrese el número de asiento que desea reservar: "))
            cinema.reservar_asiento(row, seat)
        elif choice == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
