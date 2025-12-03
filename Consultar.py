import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd


def resource_path(relative_path):
    """Devuelve la ruta correcta tanto para .py como para .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Ventana de consulta
def Consultar_Registro():
    New_Reg = tk.Toplevel()
    New_Reg.title("Consultar registro")
    New_Reg.geometry("500x600")
    New_Reg.resizable(False, False)

    # Cargar base de datos Excel
    try:
        ruta_excel = resource_path("datos/base_datos_salud_procesada.xlsx")
        df = pd.read_excel(ruta_excel)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la base de datos.\n{e}")
        return

    # Cargar imagen
    try:
        ruta_imagen = resource_path("imagenes/busqueda-de-lupa.png")
        img_original = Image.open(ruta_imagen)
        img_redimensionada = img_original.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img_redimensionada)

        imagen = tk.Label(New_Reg, image=img_tk)
        imagen.image = img_tk
        imagen.pack(pady=5)

    except Exception as e:
        tk.Label(New_Reg, text=f"No se encontró la imagen: {e}").pack(pady=5)

    # Etiqueta
    tk.Label(New_Reg, text="Escriba País o ISO:", font=("Arial", 11)).pack(pady=5)

    entry_busqueda = tk.Entry(New_Reg, width=40)
    entry_busqueda.pack(pady=5)

    lista = tk.Listbox(New_Reg, width=50, height=10)
    lista.pack(pady=10)

    info = tk.Label(New_Reg, text="", justify="left", anchor="w", font=("Arial", 10))
    info.pack(pady=10)

    # Buscar mientras escribe
    def actualizar_lista(event=None):
        lista.delete(0, tk.END)
        texto = entry_busqueda.get().strip()

        if texto == "":
            return

        resultados = df[
            (df["Country"].str.contains(texto, case=False, na=False)) |
            (df["ISO_Code"].str.contains(texto, case=False, na=False))
        ]

        for _, row in resultados.iterrows():
            lista.insert(tk.END, f"{row['Country']} ({row['ISO_Code']}) - Año {row['Year']}")

    entry_busqueda.bind("<KeyRelease>", actualizar_lista)

    # Mostrar detalles
    def mostrar_detalle(event=None):
        seleccion = lista.curselection()
        if not seleccion:
            return

        texto = lista.get(seleccion[0])
        iso = texto.split("(")[1].split(")")[0]

        registro = df[df["ISO_Code"] == iso].iloc[0]

        texto_info = (
            f"País: {registro['Country']}\n"
            f"ISO: {registro['ISO_Code']}\n"
            f"Año: {registro['Year']}\n"
            f"Reformas: {registro['Health_Reforms']}\n"
            f"Clase de gasto: {registro['Expenditure_Class']}\n"
            f"Gasto capital: {registro['Capital']}\n"
            f"% PIB Salud: {registro['Health_Expenditure_GDP_%']}\n"
            f"Gasto bolsillo: {registro['Out_of_Pocket_%']}\n"
            f"Expectativa de vida: {registro['Objective_Life_Expectancy']}\n"
        )

        info.config(text=texto_info)

    lista.bind("<<ListboxSelect>>", mostrar_detalle)

    # Botón volver
    tk.Button(
        New_Reg,
        text="Volver al menú principal",
        width=30,
        command=New_Reg.destroy
    ).pack(pady=15)
