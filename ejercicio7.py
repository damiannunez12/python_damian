import subprocess
import tkinter as tk

def abrir_calculadora():
    # Ejecuta el comando para abrir la calculadora de Windows
    subprocess.Popen("calc.exe")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Abrir Calculadora")
ventana.geometry("300x150")

# Crear y ubiscar el botón
boton = tk.Button(
    ventana, 
    text="Abrir Calculadora", 
    command=abrir_calculadora, 
    font=("Arial", 12),
    padx=10, 
    pady=5
)
boton.pack(expand=True)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()