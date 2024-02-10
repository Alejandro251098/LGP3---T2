# se crea la clase tareas para generar un blque de funciones 
class tareas:

    # funcion inico que declara como variables los parametros dados  para poder ser llamadas en las funciones
    def __init__(datos, descripcion, fecha_tarea, prioridad):
        datos.descripcion = descripcion
        datos.fecha_tarea = fecha_tarea
        datos.prioridad = prioridad
# clase para generar un blque de funciones q se usaran para la confiduracion de la lista de tareas tareas
class ConfigTareas:
    def __init__(datos):
        datos.tareas = []

    def Agregar_tarea(datos, tarea):
        datos.tareas.append(tarea)

    def editar_tarea(datos, index, nueva_tarea):
        datos.tareas[index] = nueva_tarea

    def eliminar_tarea(datos, index):
        del datos.tareas[index]

    def print_tareas(datos):
        if not datos.tareas:
            print("No hay tareas")
            return
        print("Tareas:")
        for i, tarea in enumerate(datos.tareas):
            print(f"{i+1}. Descripción: {tarea.descripcion}, Fecha de vencimiento: {tarea.fecha_tarea}, Prioridad: {tarea.prioridad}")

# funcion main o principal , donde se llama la clase configtareas para poder usar las funciones en los siguoentes condicionales con 
# las opciones de modificacion para la lista de tareas
def main():
    manager = ConfigTareas()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Editar tarea")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_tarea = input("Ingrese la fecha de vencimiento (dd/mm/aaaa): ")
            prioridad = input("Ingrese la prioridad de la tarea: ")
            tarea = tarea(descripcion, fecha_tarea, prioridad)
            manager.Agregar_tarea(tarea)
            print("Tarea agregada correctamente.")
        elif choice == "2":
            index = int(input("Ingrese el índice de la tarea a editar: ")) - 1
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            nueva_fecha_tarea = input("Ingrese la nueva fecha de vencimiento (dd/mm/aaaa): ")
            nueva_prioridad = input("Ingrese la nueva prioridad de la tarea: ")
            nueva_tarea = tarea(nueva_descripcion, nueva_fecha_tarea, nueva_prioridad)
            manager.editar_tarea(index, nueva_tarea)
            print("Tarea editada correctamente.")
        elif choice == "3":
            index = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
            manager.eliminar_tarea(index)
            print("Tarea eliminada correctamente.")
        elif choice == "4":
            manager.print_tareas()
        elif choice == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
