# clase gaastos en la se empaquetaras los datos de cateroria y monto
class Gastos:
    def __init__(self, categoria, monto):
        self.categoria = categoria
        self.monto = monto
        
# clase RegistroGastos que tendra contenidad las funciones para agregar y generar informes de los gastos y su categoria 
class RegistroGastos:
    def __init__(self):
        self.gastos = []

# agrega los gastos  ingresados a una lista
    def agregar_gasto(self, gasto):
        self.gastos.append(gasto)


    def calcular_total_por_categoria(self):
        total_por_categoria = {}
        for gasto in self.gastos:
            if gasto.categoria in total_por_categoria:
                total_por_categoria[gasto.categoria] += gasto.monto
            else:
                total_por_categoria[gasto.categoria] = gasto.monto
        return total_por_categoria

    def generar_informe(self):
        print("Informe de gastos:")
        total_por_categoria = self.calcular_total_por_categoria()
        for categoria, total in total_por_categoria.items():
            print(f"{categoria}: ${total}")

        
    def verificar_presupuesto(self, categoria):
        if categoria in self.presupuestos:
            return self.presupuestos[categoria] - self.calcular_total_por_categoria(categoria)
        else :
            return  None      

# funcion main donde se llama la clase de registro de gatos para desempaquetar los datos anteriores 
def main():
    registro = RegistroGastos()

# bucle while para la sellecion del menu segun lo que se desea q las funciones impriman  o ingresar un dato de gastos 
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar gasto")
        print("2. Generar informe de gastos")
        print("3. verificar presupuesto")
        print("4. Salir")

        choice = input("Seleccione una opción: ")

# condicionales para la seleccion de la opcion deseada y en cada condicional se llama la funcion especifica
        if choice == "1":
            categoria = input("Ingrese la categoría del gasto: ")
            monto = float(input("Ingrese el monto del gasto: "))
            gasto = gasto(categoria, monto)
            registro.agregar_gasto(gasto)
            print("Gasto agregado correctamente.")
        elif choice == "2":
            registro.generar_informe()
        elif choice == "3":
            categoria = input("Ingrese la categoría para establecer el presupuesto: ")
            presupuesto = float(input("Ingrese el presupuesto para esa categoría: "))
            registro.establecer_presupuesto(categoria, presupuesto)
            print("Presupuesto establecido correctamente.")
        elif choice == "4":
            categoria.verificar_presupuesto(categoria)
            print(f"{presupuesto}")
                  
            
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
