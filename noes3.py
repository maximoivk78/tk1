import tkinter as tk

def accionOpcion1 ():
    titulo = tk.Label(ventana, text="hola")
    titulo.pack(pady=10)

def accionOpcion2 ():
    titulo = tk.Label(ventana, text="adios")
    titulo.pack(pady=10)
    
def main():
    global ventana 
    ventana = tk.Tk()
    ventana.title("hola")
    ventana.geometry ("700x700")
    ventana.configure (bg="skyblue")
    
    etiqueta = tk.Label(ventana, text="nubes", font=("Comic Sans MS", 64))
    etiqueta.pack()
    
    boton1=tk.Button(ventana, text="opcion 1", command=accionOpcion1)
    boton1.pack(pady=5)
                    
    boton2=tk.Button(ventana, text="opcion 2", command=accionOpcion2)
    boton2.pack(pady=5)
                    
    ventana.mainloop()
 
if __name__=="__main__":
    main() 
