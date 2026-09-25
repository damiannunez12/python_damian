import subprocess
import sys
import tkinter as tk
from tkinter import messagebox


def apagar_sistema():
    """Función para apagar el dispositivo según el sistema operativo."""
    try:
        if sys.platform.startswith("win"):  # Windows
            # /s apaga el equipo, /t 0 lo hace de forma inmediata (sin demora)
            subprocess.Popen(["shutdown", "/s", "/t", "0"])
        elif sys.platform.startswith("darwin"):  # macOS
            subprocess.Popen(["sudo", "shutdown", "-h", "now"])
        else:  # Linux
            subprocess.Popen(["systemctl", "poweroff"])
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se pudo apagar el dispositivo: {e}"
        )


def procesar_texto():
    """Función que toma el texto del Entry y procede a apagar."""
    texto_ingresado = campo.get()
    if texto_ingresado:
        print(f"Texto escrito antes de apagar: {texto_ingresado}")

    # Mensaje de confirmación antes de apagar (opcional pero recomendado)
    if messagebox.askyesno(
        "Confirmar", "¿Estás seguro de que deseas apagar el equipo?"
    ):
        apagar_sistema()


# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("SNPP - Apagado")
ventana.geometry("320x150")
ventana.resizable(False, False)

# Etiqueta informativa
etiqueta = tk.Label(ventana, text="Escribe algo y apaga el equipo:")
etiqueta.pack(pady=5)

# Campo de texto (Entry)
campo = tk.Entry(ventana, width=25)
campo.pack(pady=5)

# Botón con la función de apagado
boton = tk.Button(
    ventana,
    text="Aceptar y Apagar Dispositivo",
    command=procesar_texto,
    bg="#F44336",  # Color rojo para indicar acción destructiva/apagado
    fg="white",
)
boton.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
