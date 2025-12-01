import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Visualizar():
    New_Reg = tk.Toplevel()
    New_Reg.title("Graficas")
    New_Reg.geometry("600x600")
    New_Reg.resizable(False, False)

    def volver():
        New_Reg.destroy()

    # === Crear un frame para el gráfico (antes de usarlo) ===
    frame_grafica = tk.Frame(New_Reg)
    frame_grafica.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)