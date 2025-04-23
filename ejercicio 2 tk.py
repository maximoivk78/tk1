import tkinter as tk

def main ():
    
    ventana = tk.Tk()
    ventana.title("hola")
    ventana.geometry ("700x700")
    ventana.configure (bg="skyblue")
    etiqueta = tk.Label(ventana, text="Ejercicio 2", font=("Comic Sans MS", 64))
    etiqueta.pack()
    etiqueta = tk.Label(ventana, text="maximo", font=("Comic Sans MS", 64))
    etiqueta.pack()
    ventana.mainloop()
 
if __name__=="__main__":
    main () 
