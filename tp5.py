import tkinter as tk

def accionOpcion1():
    limpiarVentana()

    etiqueta=tk.Label(text=f"opcion 1")
    etiqueta.pack(pady=10)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

    
def accionOpcion2():
    limpiarVentana()
        
    etiqueta2=tk.Label(text=f"opcion 2")
    etiqueta2.pack(pady=10)
    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def accionOpcion3():
    limpiarVentana()
    
    etiqueta3=tk.Label(text=f"opcion 3")
    etiqueta3.pack(pady=10)
    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def accionOpcion4():
    limpiarVentana()
    
    etiqueta4=tk.Label(text=f"opcion 4")
    etiqueta4.pack(pady=10)
    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def limpiarVentana():  
   
    for widget in ventana.winfo_children():  
        
        widget.destroy()

def mostrarMenu():
    limpiarVentana()
    boton1 = tk.Button(ventana, text="Opcion 1", command=accionOpcion1)
    boton1.pack(pady=5)
    
    boton2 = tk.Button(ventana, text="Opcion 2", command=accionOpcion2)
    boton2.pack(pady=5)
    
    boton3 = tk.Button(ventana, text="Opcion 3", command=accionOpcion3)
    boton3.pack(pady=5)
    
    boton4 = tk.Button(ventana, text="Opcion 4", command=accionOpcion4)
    boton4.pack(pady=5)

def main ():
    global ventana
    
    ventana = tk.Tk()
    ventana.title ("Opciones")
    ventana.geometry("600x600")
    ventana = tk.Label(ventana, text="hola", font=("Comic Sans MS", 30))
    ventana.pack()
    
    boton1 = tk.Button(ventana, text="Opcion 1", command=accionOpcion1)
    boton1.pack(pady=5)
    
    boton2 = tk.Button(ventana, text="Opcion 2", command=accionOpcion2)
    boton2.pack(pady=5)
    
    boton3 = tk.Button(ventana, text="Opcion 3", command=accionOpcion3)
    boton3.pack(pady=5)
    
    boton4 = tk.Button(ventana, text="Opcion 4", command=accionOpcion4)
    boton4.pack(pady=5)
    
    ventana.mainloop()
if __name__ == "__main__":
    main()
    
