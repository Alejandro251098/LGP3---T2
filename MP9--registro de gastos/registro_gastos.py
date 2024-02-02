class Gastos:
    def __init__(self, categoria, monto):
        self.categoria = categoria
        self.monto = monto

class RegistroGastos:
    def __init__(self):
        self.gastos = []

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

    def establecer_presupuesto(self, categoria, monto):
        self.presupuestos =  {categoria : monto}
        
    def verificar_presupuesto(self, categoria):
        if categoria in self.presupuestos:
            return self.presupuestos[categoria] - self.calcular_total_por_categoria(categoria)
        else :
            return  None      

def main():
    registro = RegistroGastos()

    while True:
        print("\n--- Menú ---")
        print("1. Ingresar gasto")
        print("2. Generar informe de gastos")
        print("3. Establecer presupuesto")
        print("4. verificar presupuesto")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

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
