import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import pandas as pd

def Visualizar():
    New_Reg = tk.Toplevel()
    New_Reg.title("Graficas")
    New_Reg.geometry("900x700")
    New_Reg.resizable(False, False)

    def volver():
        New_Reg.destroy()
        
    # cargar base de datos
    try:
        ruta = os.path.join(os.path.dirname(__file__), "base_datos_salud_procesada.xlsx")
        df = pd.read_excel(ruta)
    except:
        messagebox.showerror("Error", "No se pudo cargar el archivo base_datos_salud_procesada.xlsx")
        New_Reg.destroy()
        return

    #TÍTULO
    text1 = tk.Label(New_Reg, text="Seleccione una estadística para visualizar", font=("Arial", 14, "bold"))
    text1.pack(pady=10)

    # FRAME para la gráfica
    frame_grafica = tk.Frame(New_Reg, bd=2, relief="solid")
    frame_grafica.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    # FIGURA embebida en Tkinter
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, frame_grafica)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    #Funciones graficadoras para los botones

    def grafica1():
        """Histograma de CAPITAL (gasto en salud per cápita)"""
        ax.clear()

        ax.hist(
            df["Capital"].dropna(),
            bins=10,
            edgecolor="black"
        )

        ax.set_title("Histograma del gasto en salud per cápita (Capital)")
        ax.set_xlabel("Gasto per cápita")
        ax.set_ylabel("Frecuencia")

        canvas.draw()

    def grafica2():
        """Barras del gasto promedio por país"""
        ax.clear()

    # Promedio por país
        promedio_pais = (
            df.groupby("Country")["Capital"].mean().sort_values()
        )

        ax.bar(
            promedio_pais.index,
            promedio_pais.values
        )

        ax.set_title("Gasto promedio per cápita por país")
        ax.set_xlabel("País")
        ax.set_ylabel("Gasto promedio per cápita")
        ax.tick_params(axis="x", rotation=90)

        canvas.draw()

    def grafica3():
        """Dispersión Capital vs Esperanza de vida"""
        ax.clear()

        ax.scatter(
            df["Capital"],
            df["Objective_Life_Expectancy"]
        )

        ax.set_title("Relación entre gasto en salud y esperanza de vida")
        ax.set_xlabel("Capital (gasto per cápita)")
        ax.set_ylabel("Esperanza de vida")

        canvas.draw()

    # Botones

    frame_botones = tk.Frame(New_Reg)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Histograma (Capital)", width=22, height=2,
              command=grafica1).grid(row=0, column=0, padx=10, pady=10)

    tk.Button(frame_botones, text="Barras por país", width=22, height=2,
              command=grafica2).grid(row=0, column=1, padx=10, pady=10)

    tk.Button(frame_botones, text="Dispersión Capital vs Vida", width=22, height=2,
              command=grafica3).grid(row=0, column=2, padx=10, pady=10)

    tk.Button(New_Reg, text="Cerrar", width=20, height=2,
              command=New_Reg.destroy).pack(pady=10)