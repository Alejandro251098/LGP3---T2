import tkinter as tk 


def convertir():
    valor = float(valor_entrada.get())
    unidad_origen = grupo_unidades_origen.get()
    unidad_destino = grupo_unidades_destino.get()
    
    if unidad_origen == "metros" and unidad_destino == "kilometros":
        resultado = valor / 1000
    
    elif unidad_origen =="centimetros" and unidad_destino == "metros":
        resultado = valor * 100
        
    elif unidad_origen == "gramos" and unidad_destino == "kilogramo":
        resultado = valor / 1000
        
    elif unidad_origen == "celsius" and unidad_destino == "farenheit":
        resultado = valor *9/2 + 32
        
    else:
         resultado = valor 
         
    
    label_resultado.config(text ="resultado:"
                                 +  str(resultado))
    
    ventana = tk.Tk()
    ventana.title("CONVERSOR DE UNIDADES")
    
    valor_entrada = tk.entry(ventana)
    valor_entrada.pack()
    
    
    unidades_origen = ["metros", "kilometros","centimetros","gramos", "kilogramos","celsius", "farenheit"]
    grupo_unidades_origen = tk.StringVar(ventana)
    grupo_unidades_origen.set(unidades_origen[0])
    
    
    menu_unidades_origen = tk.OptionMenu(ventana,grupo_unidades_origen,*unidades_origen)
    menu_unidades_origen.pak()
    
    
    unidades_destino = ["metros", "kilometros","centimetros","gramos", "kilogramos","celsius", "farenheit"]
    grupo_unidades_destino = tk.StringVar(ventana)
    grupo_unidades_destino.set(unidades_destino[1])   
    
    menu_unidades_destino = tk.OptionMenu(ventana,grupo_unidades_destino,*unidades_destino)
    menu_unidades_destino.pak()             
    
    boton_convertir = tk.label(ventana, text = "convertir" , command= convertir)
    boton_convertir.pack()
    
    label_resultado = tk.labrl(ventana, text ="resultado:",)
    label_resultado.pack()
    
    ventana.mainloop() 