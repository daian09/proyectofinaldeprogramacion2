import tkinter as tk
from tkinter import ttk

def Filtrar_Registros():
    New_Reg = tk.Toplevel()
    New_Reg.title("Filtros")
    New_Reg.geometry("500x400")

    def volver():
        New_Reg.destroy()

    titulo = tk.Label(New_Reg, text="Seleccione los filtros necesarios")
    titulo.pack(padx=5, pady=5)

    # Marco para los botones
    frame_filtros = tk.Frame(New_Reg)
    frame_filtros.pack(pady=20)

    # Marco para los botones
    frame_botones = tk.Frame(New_Reg)
    frame_botones.pack(pady=20)

    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    var4 = tk.BooleanVar()
    checkbox1 = ttk.Checkbutton(frame_filtros, variable=var1, onvalue=1, offvalue=0)
    checkbox2 = ttk.Checkbutton(frame_filtros, variable=var2, onvalue=1, offvalue=0)
    checkbox3= ttk.Checkbutton(frame_filtros, variable=var3, onvalue=1, offvalue=0)
    checkbox4 = ttk.Checkbutton(frame_filtros, variable=var4, onvalue=1, offvalue=0)

    opciones = ["Alto", "Medio", "Bajo"]
    Lista_Opciones = ttk.Combobox(frame_filtros, values=opciones, state='readonly')

    text1 = tk.Label(frame_filtros, text="Registros con capital mayor al promedio")
    text2 = tk.Label(frame_filtros, text="Registros de una clase de gasto especifica")
    text3 = tk.Label(frame_filtros, text="Registro con capital menor a:")
    text4 = tk.Label(frame_filtros, text="Filtrar por año")

    btn1 = tk.Button(frame_botones, text="Guardar Registro", width=20, height=3)
    btn2 = tk.Button(frame_botones, text="Volver al menu\n principal", width=20, height=3, command=volver)

    text1.grid(row=0, column=1, padx=10, pady=10)
    checkbox1.grid(row=0, column=0, padx=10, pady=10)

    text2.grid(row=1, column=1, padx=10, pady=10)
    checkbox2.grid(row=1, column=0, padx=10, pady=10)
    Lista_Opciones.grid(row=2, column=1, padx=10, pady=10)

    text3.grid(row=3, column=1, padx=10, pady=10)
    checkbox3.grid(row=3, column=0, padx=10, pady=10)

    text4.grid(row=4, column=1, padx=10, pady=10)
    checkbox4.grid(row=4, column=0, padx=10, pady=10)

    btn1.grid(row=0, column=0, padx=10, pady=10)
    btn2.grid(row=0, column=1, padx=10, pady=10)