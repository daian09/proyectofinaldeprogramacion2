import tkinter as tk

def Add_Registro():
    New_Reg = tk.Toplevel()
    New_Reg.title("Añadir Registro")
    New_Reg.geometry("350x300")

    def volver():
        New_Reg.destroy()

    text1 = tk.Label(New_Reg, text="Region o ciudad")
    text2 = tk.Label(New_Reg, text="Capital")
    text3 = tk.Label(New_Reg, text="Clase de gasto")
    text4 = tk.Label(New_Reg, text="Nivel de  inversion\n(Alto/Medio/Bajo)")

    info1 = tk.Entry(New_Reg)
    info2 = tk.Entry(New_Reg)
    info3 = tk.Entry(New_Reg)
    info4 = tk.Entry(New_Reg)

    btn1 = tk.Button(New_Reg, text="Guardar Registro", width=20, height=3)
    btn2 = tk.Button(New_Reg, text="Volver al menu\n principal sin guardar", width=20, height=3, command=volver)

    text1.grid(row=0, column=0, padx=10, pady=10)
    text2.grid(row=1, column=0, padx=10, pady=10)
    text3.grid(row=2, column=0, padx=10, pady=10)
    text4.grid(row=3, column=0, padx=10, pady=10)

    info1.grid(row=0, column=1, padx=10, pady=10)
    info2.grid(row=1, column=1, padx=10, pady=10)
    info3.grid(row=2, column=1, padx=10, pady=10)
    info4.grid(row=3, column=1, padx=10, pady=10)

    btn1.grid(row=5, column=0, padx=10, pady=10)
    btn2.grid(row=5, column=1, padx=10, pady=10)
    