import tkinter as tk

def accionOpcion1():
    etiqueta=tk.Label(text=f"opcion 1")
    etiqueta.pack(pady=10)
def accionOpcion2():
    etiqueta2=tk.Label(text=f"opcion 2")
    etiqueta2.pack(pady=10)
def accionOpcion3():
    etiqueta3=tk.Label(text=f"opcion 3")
    etiqueta3.pack(pady=10)
def accionOpcion4():
    etiqueta4=tk.Label(text=f"opcion 4")
    etiqueta4.pack(pady=10)
def main ():
    global ventana
    
    ventana = tk.Tk()
    ventana.title ("Opciones")
    ventana.geometry("300x200")

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
    
