import datetime
tareas =[]
def inicio (tarea ,descripcion, fecha_limite , prioridad):
    tarea.descripcion = descripcion
    tarea.fecha_limite = fecha_limite
    tarea.prioridad   = prioridad

def orden(tarea):
    return f"{tarea.descripcion} - {tarea.fecha_limite.strftime('%d/%m/%Y')} - {tarea.prioridad}"
    



 

def agregar_tarea(prioridad,descripcion,fecha_limite):
    if not isinstance(fecha_limite, datetime.date):
        return ValueError("debe escribir una fecha limite en orden y/m/d")
    if not isinstance(prioridad, int) or prioridad < 1 or prioridad > 3:
        return ValueError("la prioridad debe ser un numero entre 1 y 3")
    tarea = tarea(descripcion,fecha_limite,prioridad) 
    tareas.append(tarea)
    print("tarea agregada con exito")
   
    
    
def eliminar_tarea(tarea):
    
    if tarea < len(tareas):
        tareas.pop(tarea)
        print("tarea eliminada con exito")
    
    else :
        print("la tarea no existe ")
               
def EliminarPorFecha(tarea, fecha_limite):
    if not isinstance(fecha_limite, datetime.date):
            return ValueError("La fecha limite debe tener formator y/m/d")
    for tarea in tareas:
            if tarea.fecha_limite == fecha_limite:
                tareas.remove(tarea)
                break
        
    else:
        print("No se encontró ninguna tarea con la fecha limite especificada")
           
        
def buscar_tarea(tarea):
    for tarea in tareas: 
     if tarea ==  tarea :
       print(f"tarea que busca es :{tarea}")
            
    else :
        print("esta tarea no existe")
        
            
def mostrar_tareas():
    
               
    for   tarea in enumerate(tareas):
       print(f"  {tarea}")
           
    else :
        print("no hay tareas en la lista")
        

def main():
    
    opcion = 0
    
    if    opcion != 6 :
        print( " ---lista de tareas---")        
        print("1- agregar tarea")
        print("2- eliminar tarea")
        print("3- eliminar por fecha")
        print("4- buscar tarea")
        print("5- mostrar lista de tareas")
        print("6- salir ") 
             
    
    opcion = int(input("seleccione una opcion "))
    
    
    if opcion == 1:
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_limite = datetime.date(int(input("Ingrese el año de la fecha limite: ")),
                                          int(input("Ingrese el mes de la fecha limite: ")),
                                          int(input("Ingrese el día de la fecha limite: ")))
        prioridad = int(input("Ingrese la prioridad de la tarea (1: baja, 2: media, 3: alta): "))
        agregar_tarea(descripcion,fecha_limite,prioridad)
    elif opcion == 2:
        eliminar_tarea(tareas)
    elif opcion == 3 :
        fecha_limite = datetime.date(int(input("Ingrese el año de la fecha limite: ")),
                                          int(input("Ingrese el mes de la fecha limite: ")),
                                          int(input("Ingrese el día de la fecha limite: ")))
        
        EliminarPorFecha(fecha_limite)
    elif opcion == 4 :
        print("que tarea desea buscar")
        buscar_tarea(tareas)
    elif opcion == 5:
        mostrar_tareas()
    elif opcion == 6 :
        print("hasta luego")
        
                      
    else :
        print("opcion no valida")

    return main()
                         
if __name__ == "__main__":
    main()