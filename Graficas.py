import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys


#función para rutas compatibles con PyInstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Cuando está empaquetado
    except:
        base_path = os.path.abspath(".")  # Modo normal
    return os.path.join(base_path, relative_path)


#función para visualizar gráficas

def Visualizar():
    New_Reg = tk.Toplevel()
    New_Reg.title("Gráficas")
    New_Reg.geometry("600x200")

    def volver():
        New_Reg.destroy()


    # Cargar base de datos Excel
    try:
        ruta = resource_path("base_datos_salud_procesada.xlsx")
        df = pd.read_excel(ruta)
    except Exception as e:
        tk.Label(New_Reg, text=f"Error al cargar datos: {e}", fg="red").pack()
        return

    # funciones de las gráficas

    def grafica_1():
        """Gasto capital promedio por año"""
        datos = df.groupby("Year")["Capital"].mean()

        plt.figure()
        plt.plot(datos.index, datos.values)
        plt.title("Promedio de gasto capital por año")
        plt.xlabel("Año")
        plt.ylabel("Capital promedio")
        plt.tight_layout()
        plt.show()

    def grafica_2():
        """Conteo por clase de gasto"""
        datos = df["Expenditure_Class"].value_counts()

        plt.figure()
        plt.bar(datos.index, datos.values)
        plt.title("Cantidad por clase de gasto")
        plt.xlabel("Clase")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.show()

    def grafica_3():
        """Gasto de bolsillo promedio por país"""
        datos = df.groupby("Country")["Out_of_Pocket_%"].mean().nlargest(10)

        plt.figure()
        plt.barh(datos.index, datos.values)
        plt.title("Top 10 países con mayor gasto de bolsillo")
        plt.xlabel("% Gasto bolsillo")
        plt.tight_layout()
        plt.show()

    # interfaz de selección de gráficas
    text1 = tk.Label(New_Reg, text="Seleccione una estadística para visualizar")
    text1.grid(row=0, column=1, padx=10, pady=10)

    btn1 = tk.Button(New_Reg, text="Gráfica 1", width=20, height=3, command=grafica_1)
    btn2 = tk.Button(New_Reg, text="Gráfica 2", width=20, height=3, command=grafica_2)
    btn3 = tk.Button(New_Reg, text="Gráfica 3", width=20, height=3, command=grafica_3)

    botonSalir = tk.Button(New_Reg, text="Volver al menú\n principal", width=20, height=3, command=volver)

    btn1.grid(row=1, column=0, padx=10, pady=10)
    btn2.grid(row=1, column=1, padx=10, pady=10)
    btn3.grid(row=1, column=2, padx=10, pady=10)
    botonSalir.grid(row=2, column=1, padx=10, pady=10)
