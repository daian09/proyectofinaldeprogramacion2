import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

def resource_path(relative_path):
    """Devuelve la ruta correcta tanto para .py como para .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# función para visualizar gráficas
def Visualizar():
    New_Reg = tk.Toplevel()
    New_Reg.title("Gráficas")
    New_Reg.geometry("500x200")
    New_Reg.resizable(False, False)

    def volver():
        New_Reg.destroy()

    # Cargar base de datos Excel  (⚠ CORREGIDO)
    try:
        ruta = resource_path("datos/base_datos_salud_procesada.xlsx")
        df = pd.read_excel(ruta)
    except Exception as e:
        tk.Label(New_Reg, text=f"Error al cargar datos:\n{e}", fg="red").pack()
        return

    # ============================
    #   FUNCIONES DE LAS GRÁFICAS
    # ============================

    def grafica_1():
        """Promedio de gasto capital por año"""
        datos = df.groupby("Year")["Capital"].mean()

        plt.figure()
        plt.plot(datos.index, datos.values, marker="o")
        plt.title("Promedio de gasto capital por año")
        plt.xlabel("Año")
        plt.ylabel("Capital promedio")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def grafica_2():
        """Conteo por clase de gasto"""
        datos = df["Expenditure_Class"].value_counts()

        plt.figure()
        plt.bar(datos.index, datos.values)
        plt.title("Cantidad por clase de gasto")
        plt.xlabel("Clase de gasto")
        plt.ylabel("Frecuencia")
        plt.grid(axis="y")
        plt.tight_layout()
        plt.show()

    def grafica_3():
        """Top 10 países con mayor gasto de bolsillo"""
        datos = df.groupby("Country")["Out_of_Pocket_%"].mean().nlargest(10).sort_values()

        plt.figure(figsize=(8, 6))
        plt.barh(datos.index, datos.values)

        # Etiquetas
        for i, valor in enumerate(datos.values):
            plt.text(valor + 0.3, i, f"{valor:.1f}%", va="center")

        plt.title("Top 10 países con mayor gasto de bolsillo (%)")
        plt.xlabel("% Gasto de bolsillo")
        plt.grid(axis="x", linestyle="--", alpha=0.6)
        plt.xlim(0, datos.max() * 1.2)
        plt.tight_layout()
        plt.show()

    # interfaz de selección
    text1 = tk.Label(New_Reg, text="Seleccione una estadística para visualizar")
    text1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    btn1 = tk.Button(New_Reg, text="Promedio de gasto capital por año", width=30, height=3, command=grafica_1)
    btn2 = tk.Button(New_Reg, text="Cantidad por clase de gasto", width=30, height=3, command=grafica_2)
    btn3 = tk.Button(New_Reg, text="Top 10 países con mayor gasto de bolsillo", width=30, height=3, command=grafica_3)
    botonSalir = tk.Button(New_Reg, text="Volver al menú principal", width=30, height=3, command=volver)

    btn1.grid(row=1, column=0, padx=10, pady=10)
    btn2.grid(row=1, column=1, padx=10, pady=10)
    btn3.grid(row=2, column=0, padx=10, pady=10)
    botonSalir.grid(row=2, column=1, padx=10, pady=10)
