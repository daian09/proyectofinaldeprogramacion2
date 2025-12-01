import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os


def Filtrar_Registros():
    New_Reg = tk.Toplevel()
    New_Reg.title("Filtros")
    New_Reg.geometry("650x500")
    New_Reg.resizable(False, False)

    # cargar base de datos
    try:
        ruta = os.path.join(os.path.dirname(__file__), "base_datos_salud_procesada.xlsx")
        df = pd.read_excel(ruta)
    except:
        messagebox.showerror("Error", "No se pudo cargar el archivo base_datos_salud_procesada.xlsx")
        New_Reg.destroy()
        return

    # función para aplicar los filtros seleccionados
    def aplicar_filtros():
        filtros_aplicados = df.copy()

        # 1. Capital mayor al promedio
        if var1.get():
            promedio = df["Capital"].mean()
            filtros_aplicados = filtros_aplicados[filtros_aplicados["Capital"] > promedio]

        # 2. Clase de gasto
        if var2.get():
            clase = Lista_Opciones.get()
            if clase == "":
                messagebox.showerror("Error", "Debe seleccionar una clase de gasto.")
                return
            filtros_aplicados = filtros_aplicados[filtros_aplicados["Expenditure_Class"] == clase]

        # 3. Capital menor a
        if var3.get():
            try:
                menor_a = float(entry_menor.get())
                filtros_aplicados = filtros_aplicados[filtros_aplicados["Capital"] < menor_a]
            except:
                messagebox.showerror("Error", "Ingrese un valor numérico para el filtro de capital menor.")
                return

        # 4. Año exacto
        if var4.get():
            try:
                year = int(entry_year.get())
                filtros_aplicados = filtros_aplicados[filtros_aplicados["Year"] == year]
            except:
                messagebox.showerror("Error", "Ingrese un año válido.")
                return

        mostrar_resultados(filtros_aplicados)

    # función para mostrar resultados en una nueva ventana
    def mostrar_resultados(resultados):
        if resultados.empty:
            messagebox.showinfo("Sin resultados", "No se encontraron registros con esos filtros.")
            return

        ventana_resultados = tk.Toplevel()
        ventana_resultados.title("Resultados de filtros")
        ventana_resultados.geometry("900x400")

        columnas = list(resultados.columns)
        tabla = ttk.Treeview(ventana_resultados, columns=columnas, show="headings")

        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=120)

        for _, row in resultados.iterrows():
            tabla.insert("", tk.END, values=list(row))

        tabla.pack(fill="both", expand=True)

    # interfaz de filtros
    titulo = tk.Label(New_Reg, text="Seleccione los filtros necesarios", font=("Arial", 12))
    titulo.pack(padx=5, pady=5)

    frame_filtros = tk.Frame(New_Reg)
    frame_filtros.pack(pady=10)

    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    var4 = tk.BooleanVar()

    # Checkbox 1: Capital > promedio
    checkbox1 = ttk.Checkbutton(frame_filtros, variable=var1)
    text1 = tk.Label(frame_filtros, text="Registros con capital mayor al promedio")
    checkbox1.grid(row=0, column=0, padx=10, pady=10)
    text1.grid(row=0, column=1, padx=10, pady=10)

    # Checkbox 2: Clase de gasto
    checkbox2 = ttk.Checkbutton(frame_filtros, variable=var2)
    text2 = tk.Label(frame_filtros, text="Registros por clase de gasto")
    opciones = ["Alto", "Medio", "Bajo"]
    Lista_Opciones = ttk.Combobox(frame_filtros, values=opciones, state="readonly")

    checkbox2.grid(row=1, column=0, padx=10, pady=10)
    text2.grid(row=1, column=1, padx=10, pady=10)
    Lista_Opciones.grid(row=2, column=1, padx=10, pady=10)

    # Checkbox 3: Capital menor a X
    checkbox3 = ttk.Checkbutton(frame_filtros, variable=var3)
    text3 = tk.Label(frame_filtros, text="Capital menor a:")
    entry_menor = tk.Entry(frame_filtros, width=15)

    checkbox3.grid(row=3, column=0, padx=10, pady=10)
    text3.grid(row=3, column=1, padx=10, pady=10)
    entry_menor.grid(row=3, column=2, padx=10, pady=10)

    # Checkbox 4: Año exacto
    checkbox4 = ttk.Checkbutton(frame_filtros, variable=var4)
    text4 = tk.Label(frame_filtros, text="Filtrar por año:")
    entry_year = tk.Entry(frame_filtros, width=15)

    checkbox4.grid(row=4, column=0, padx=10, pady=10)
    text4.grid(row=4, column=1, padx=10, pady=10)
    entry_year.grid(row=4, column=2, padx=10, pady=10)

    # Botones inferiores
    frame_botones = tk.Frame(New_Reg)
    frame_botones.pack(pady=10)

    btn_aplicar = tk.Button(frame_botones, text="Aplicar filtros", width=20, height=2, command=aplicar_filtros)
    btn_volver = tk.Button(frame_botones, text="Volver", width=20, height=2, command=New_Reg.destroy)

    btn_aplicar.grid(row=0, column=0, padx=20)
    btn_volver.grid(row=0, column=1, padx=20)
