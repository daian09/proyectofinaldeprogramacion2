import os
import tkinter as tk
from PIL import Image, ImageTk

def Consultar_Registro():
    New_Reg = tk.Toplevel()
    New_Reg.title("Consultar registro")
    New_Reg.geometry("350x250")

    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ruta_imagen = os.path.join(BASE_DIR, "busqueda-de-lupa.png")
        # Imagen de la ventana principal
        img_original = Image.open(ruta_imagen)
        img_redimensionada = img_original.resize((100, 100)) # Nuevo tamaño de la imagen
        img_tk = ImageTk.PhotoImage(img_redimensionada)

        # Crear una etiqueta para mostrar la imagen
        imagen = tk.Label(New_Reg, image=img_tk)
        # Guardar referencia a la imagen
        imagen.image = img_tk
        # Empaquetar la etiqueta para que sea visible
        imagen.pack(padx=5, pady=5)

    except FileNotFoundError:
        error_label = tk.Label(New_Reg, text="No se encontró la imagen")
        error_label.pack(padx=5, pady=5)
    
    # Marco para los botones
    frame_botones = tk.Frame(New_Reg)
    frame_botones.pack(pady=20)

    def volver():
        New_Reg.destroy()

    btn1 = tk.Button(frame_botones, text="Buscar registro", width=20, height=3)
    btn2 = tk.Button(frame_botones, text="Volver al menu\n principal", width=20, height=3, command=volver)

    btn1.grid(row=0, column=0, padx=10, pady=10)
    btn2.grid(row=0, column=1, padx=10, pady=10)