import tkinter as tk

def saludar():
    
    nombre = entry.get()

    
    etiqueta2=tk.Label(text=f"¡Hola, {nombre}, te saluda Máximo!")
    etiqueta2.pack()

def main():
    global ventana, entry, etiqueta  

   
    ventana = tk.Tk()
    ventana.title("hola")
    ventana.geometry("700x700")
    ventana.configure(bg="skyblue")

    
    etiqueta = tk.Label(ventana, text="ingresa tu nombre", font=("Comic Sans MS", 32))
    etiqueta.pack()

   
    entry = tk.Entry(ventana)
    entry.pack(pady=10)

   
    boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
    boton_saludar.pack(pady=10)

    
    ventana.mainloop()

if __name__ == "__main__":
    main()
