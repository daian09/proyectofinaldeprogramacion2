import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import sys
import os

def resource_path(relative_path):
    """Devuelve la ruta correcta tanto para .py como para .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ==============================
# RUTA CORRECTA DEL DATASET
# ==============================
# Como el archivo está dentro de la carpeta "datos" y esa carpeta
# fue agregada con --add-data "datos;datos"
# entonces la ruta interna ES: datos/base_datos_salud_procesada.xlsx
RUTA_EXCEL = resource_path("datos/base_datos_salud_procesada.xlsx")


def Filtrar_Registros(master=None):
    if master is None:
        master = tk.Tk()
        master.withdraw()

    # ==============================
    #      VENTANA DE FILTROS
    # ==============================
    New_Reg = tk.Toplevel(master)
    New_Reg.title("Filtros")
    New_Reg.geometry("520x480")

    # Cargar Excel una vez
    try:
        df_base = pd.read_excel(RUTA_EXCEL)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el Excel:\n{RUTA_EXCEL}\n\n{e}")
        return

    # ==============================
    #       FUNCIÓN FILTRAR
    # ==============================
    def aplicar_filtros():
        df = df_base.copy()

        # Filtro 1: Capital mayor al promedio
        if var1.get():
            df = df[df["Capital"] > df["Capital"].mean()]

        # Filtro 2: Clase específica
        if var2.get():
            valor = Lista_Opciones.get().strip()
            if valor != "":
                df = df[df["Expenditure_Class"] == valor]

        # Filtro 3: Capital menor a X
        if var3.get():
            try:
                x_valor = float(entry_capital.get())
                df = df[df["Capital"] < x_valor]
            except:
                messagebox.showerror("Error", "Debe ingresar un número válido en 'Capital menor a'")
                return

        # Filtro 4: Año específico
        if var4.get():
            try:
                año = int(entry_año.get().strip())
                df = df[df["Year"] == año]
            except:
                messagebox.showerror("Error", "Debe ingresar un año válido (solo números)")
                return

        mostrar_resultados(df)

    # ==============================
    #   VENTANA DE RESULTADOS
    # ==============================
    def mostrar_resultados(df):
        ventana = tk.Toplevel(New_Reg)
        ventana.title("Resultados del filtro")
        ventana.geometry("1000x600")

        tabla = ttk.Treeview(ventana, columns=list(df.columns), show="headings")
        tabla.pack(fill="both", expand=True)

        # Encabezados
        for col in df.columns:
            tabla.heading(col, text=col)
            tabla.column(col, width=140)

        # Datos
        for _, fila in df.iterrows():
            tabla.insert("", "end", values=list(fila))

    # ==============================
    #         INTERFAZ
    # ==============================
    titulo = tk.Label(New_Reg, text="Seleccione los filtros que desea aplicar", font=("Arial", 12))
    titulo.pack(padx=5, pady=10)

    frame_filtros = tk.Frame(New_Reg)
    frame_filtros.pack(pady=10)

    frame_botones = tk.Frame(New_Reg)
    frame_botones.pack(pady=20)

    # Variables
    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    var4 = tk.BooleanVar()

    # Checkbox y etiquetas
    checkbox1 = ttk.Checkbutton(frame_filtros, variable=var1)
    text1 = tk.Label(frame_filtros, text="Capital mayor al promedio")

    checkbox2 = ttk.Checkbutton(frame_filtros, variable=var2)
    text2 = tk.Label(frame_filtros, text="Clase de gasto específica")
    Lista_Opciones = ttk.Combobox(frame_filtros, values=["Alto", "Medio", "Bajo"], state="readonly")

    checkbox3 = ttk.Checkbutton(frame_filtros, variable=var3)
    text3 = tk.Label(frame_filtros, text="Capital menor a:")
    entry_capital = tk.Entry(frame_filtros, width=12)

    checkbox4 = ttk.Checkbutton(frame_filtros, variable=var4)
    text4 = tk.Label(frame_filtros, text="Filtrar por año (escriba)")
    entry_año = tk.Entry(frame_filtros, width=12)

    # Grid
    checkbox1.grid(row=0, column=0, padx=10, pady=8)
    text1.grid(row=0, column=1, padx=10, pady=8)

    checkbox2.grid(row=1, column=0, padx=10, pady=8)
    text2.grid(row=1, column=1, padx=10, pady=8)
    Lista_Opciones.grid(row=2, column=1, padx=10, pady=5)

    checkbox3.grid(row=3, column=0, padx=10, pady=8)
    text3.grid(row=3, column=1, padx=10, pady=8)
    entry_capital.grid(row=4, column=1, padx=10, pady=5)

    checkbox4.grid(row=5, column=0, padx=10, pady=8)
    text4.grid(row=5, column=1, padx=10, pady=8)
    entry_año.grid(row=6, column=1, padx=10, pady=5)

    # Botones
    btn1 = tk.Button(frame_botones, text="Aplicar filtros", width=20, height=2, command=aplicar_filtros)
    btn2 = tk.Button(frame_botones, text="Volver", width=20, height=2, command=New_Reg.destroy)

    btn1.grid(row=0, column=0, padx=10)
    btn2.grid(row=0, column=1, padx=10)
