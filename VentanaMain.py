import tkinter as tk
from PIL import Image, ImageTk  # Para manejar imágenes
import os 
import sys 
# Importar los módulos de las otras ventanas

import AddRegistro
import Consultar
import Graficas
import Filtrar

# función para rutas compatibles con PyInstaller
def resource_path(relative_path):
    """Obtiene ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS  # Cuando está dentro del ejecutable
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    New_Reg.resizable(False, False)


#funciones de los botones
def Boton1():
    AddRegistro.Add_Registro()

def Boton2():
    Consultar.Consultar_Registro()
    
def Boton3():
    Filtrar.Filtrar_Registros()

def Boton4():
    Graficas.Visualizar()


# ventana principal
root = tk.Tk()
root.title("Analisis de gastos en salud")
root.geometry("500x400")

try:
    # ruta correcta para PyInstaller
    ruta_imagen = resource_path("salud-financiera.png")

    # cargar y redimensionar imagen
    img_original = Image.open(ruta_imagen)
    img_redimensionada = img_original.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_redimensionada)

    # mostrar la imagen
    imagen = tk.Label(root, image=img_tk)
    imagen.image = img_tk  # evitar que sea borrada por el GC
    imagen.pack(padx=5, pady=5)

except Exception as e:
    error_label = tk.Label(root, text=f"No se encontró la imagen: {e}")
    error_label.pack(padx=5, pady=5)

# Marco de botones
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

frame_botones.grid_columnconfigure(0, weight=1)
frame_botones.grid_columnconfigure(1, weight=1)

# EJECUTAR APLICACIÓN

root.mainloop()
