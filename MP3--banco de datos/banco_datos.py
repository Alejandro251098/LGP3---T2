class BaseDatos:
    def __init__(datos):
        datos.registros = {}

    def agregar_datos(datos, id_registro, data):
        datos.registros[id_registro] = data

    def actualizar_datos(datos, id_registro, dato_nuevo):
        if id_registro in datos.registros:
            datos.registros[id_registro] = dato_nuevo
            print("Registro actualizado correctamente.")
        else:
            print("No se encontró el registro con ese ID.")

    def eliminar_datos(datos, id_registro):
        if id_registro in datos.registros:
            del datos.registros[id_registro]
            print("Registro eliminado correctamente.")
        else:
            print("No se encontró el registro con ese ID.")

    def buscar_datos(datos, id_registro):
        if id_registro in datos.registros:
            print(f"Registro encontrado para el ID {id_registro}: {datos.registros[id_registro]}")
        else:
            print("No se encontró ningún registro para ese ID.")

    def print_registros(datos):
        if not datos.registros:
            print("La base de datos está vacía.")
        else:
            print("Registros en la base de datos:")
            for id_registro, data in datos.registros.items():
                print(f"ID: {id_registro}, Datos: {data}")

def main():
    base_datos = BaseDatos()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar registro")
        print("2. Actualizar registro")
        print("3. Eliminar registro")
        print("4. Buscar registro")
        print("5. Mostrar todos los registros")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            id_registro = input("Ingrese el ID del nuevo registro: ")
            data = input("Ingrese los datos del nuevo registro: ")
            base_datos.agregar_datos(id_registro, data)
            print("Registro agregado correctamente.")
        elif choice == "2":
            id_registro = input("Ingrese el ID del registro a actualizar: ")
            dato_nuevo = input("Ingrese los nuevos datos para el registro: ")
            base_datos.actualizar_datos(id_registro, dato_nuevo)
        elif choice == "3":
            id_registro = input("Ingrese el ID del registro a eliminar: ")
            base_datos.eliminar_datos(id_registro)
        elif choice == "4":
            id_registro = input("Ingrese el ID del registro a buscar: ")
            base_datos.buscar_datos(id_registro)
        elif choice == "5":
            base_datos.print_registros()
        elif choice == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
