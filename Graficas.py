import tkinter as tk

def Visualizar():
    New_Reg = tk.Toplevel()
    New_Reg.title("Graficas")
    New_Reg.geometry("600x200")

    def volver():
        New_Reg.destroy()

    text1 = tk.Label(New_Reg, text="Seleccione una estadistica para visualizar")

    btn1 = tk.Button(New_Reg, text="Grafica 1", width=20, height=3)
    btn2 = tk.Button(New_Reg, text="Grafica 2", width=20, height=3)
    btn3 = tk.Button(New_Reg, text="Grafica 3", width=20, height=3)
    botonSalir = tk.Button(New_Reg, text="Volver al menu\n principal", width=20, height=3, command=volver)

    text1.grid(row=0, column=1, padx=10, pady=10)

    btn1.grid(row=1, column=0, padx=10, pady=10)
    btn2.grid(row=1, column=1, padx=10, pady=10)
    btn3.grid(row=1, column=2, padx=10, pady=10)
    botonSalir.grid(row=2, column=1, padx=10, pady=10)