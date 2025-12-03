import tkinter as tk
from tkinter import ttk

def Filtrar_Registros():
    New_Reg = tk.Toplevel()
    New_Reg.title("Filtros")
    New_Reg.geometry("500x400")

    def volver():
        New_Reg.destroy()

    # Título
    titulo = tk.Label(New_Reg, text="Seleccione los filtros necesarios")
    titulo.pack(padx=5, pady=5)

    # Marco de filtros
    frame_filtros = tk.Frame(New_Reg)
    frame_filtros.pack(pady=20)

    # Marco de botones
    frame_botones = tk.Frame(New_Reg)
    frame_botones.pack(pady=20)

    # Variables de Checkbuttons
    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    var4 = tk.BooleanVar()

    # Checkbuttons
    checkbox1 = ttk.Checkbutton(frame_filtros, variable=var1)
    checkbox2 = ttk.Checkbutton(frame_filtros, variable=var2)
    checkbox3 = ttk.Checkbutton(frame_filtros, variable=var3)
    checkbox4 = ttk.Checkbutton(frame_filtros, variable=var4)

    # Opciones para el combobox
    opciones = ["Alto", "Medio", "Bajo"]
    Lista_Opciones = ttk.Combobox(frame_filtros, values=opciones, state='readonly')

    # Textos
    text1 = tk.Label(frame_filtros, text="Registros con capital mayor al promedio")
    text2 = tk.Label(frame_filtros, text="Registros de una clase de gasto específica")
    text3 = tk.Label(frame_filtros, text="Registro con capital menor a:")
    text4 = tk.Label(frame_filtros, text="Filtrar por año")

    # Botones
    btn1 = tk.Button(frame_botones, text="Guardar Registro", width=20, height=3)
    btn2 = tk.Button(frame_botones, text="Volver al menú\n principal", width=20, height=3, command=volver)

    # Grid de los filtros
    text1.grid(row=0, column=1, padx=10, pady=10)
    checkbox1.grid(row=0, column=0, padx=10, pady=10)

    text2.grid(row=1, column=1, padx=10, pady=10)
    checkbox2.grid(row=1, column=0, padx=10, pady=10)
    Lista_Opciones.grid(row=2, column=1, padx=10, pady=10)

    text3.grid(row=3, column=1, padx=10, pady=10)
    checkbox3.grid(row=3, column=0, padx=10, pady=10)

    text4.grid(row=4, column=1, padx=10, pady=10)
    checkbox4.grid(row=4, column=0, padx=10, pady=10)

    # Grid botones
    btn1.grid(row=0, column=0, padx=10, pady=10)
    btn2.grid(row=0, column=1, padx=10, pady=10)
