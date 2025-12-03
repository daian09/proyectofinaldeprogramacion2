import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

# Importar módulos de las otras ventanas
import AddRegistro
import Consultar
import Graficas
import Filtrar
# Función para rutas compatibles con PyInstaller

def resource_path(relative_path):
    """Devuelve la ruta correcta tanto para .py como para .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Funciones de los botones
def Boton1():
    AddRegistro.Add_Registro()

def Boton2():
    Consultar.Consultar_Registro()

def Boton3():
    Filtrar.Filtrar_Registros()

def Boton4():
    Graficas.Visualizar()


# Ventana principal
root = tk.Tk()
root.title("Analisis de gastos en salud")
root.geometry("500x400")
root.resizable(False, False)

try:
    ruta_imagen = resource_path("imagenes/salud-financiera.png")

    img_original = Image.open(ruta_imagen)
    img_redimensionada = img_original.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_redimensionada)

    imagen = tk.Label(root, image=img_tk)
    imagen.image = img_tk
    imagen.pack(padx=5, pady=5)

except Exception as e:
    tk.Label(root, text=f"No se encontró la imagen: {e}").pack()


# Marco botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=20)

btn1 = tk.Button(frame_botones, text="Añadir Registro", width=20, height=3, command=Boton1)
btn2 = tk.Button(frame_botones, text="Consultar registro", width=20, height=3, command=Boton2)
btn3 = tk.Button(frame_botones, text="Filtrar datos por categorías", width=20, height=3, command=Boton3)
btn4 = tk.Button(frame_botones, text="Visualización de estadísticas", width=20, height=3, command=Boton4)

btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3.grid(row=1, column=0, padx=10, pady=10)
btn4.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
