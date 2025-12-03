import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

def Add_Registro():
    New_Reg = tk.Toplevel()
    New_Reg.title("Añadir Registro")
    New_Reg.geometry("500x520")
    New_Reg.resizable(False, False)

    # ------------- Función para guardar el registro -------------
    def guardar_registro():
        campos = {
            "Country": info1.get().strip(),
            "ISO_Code": info2.get().strip(),
            "Year": info3.get().strip(),
            "Health_Reforms": info4.get().strip(),
            "Expenditure_Class": info5.get().strip(),
            "Capital": info6.get().strip(),
            "Health_Expenditure_GDP_%": info7.get().strip(),
            "Out_of_Pocket_%": info8.get().strip(),
            "Objective_Life_Expectancy": info9.get().strip(),
        }

        # Validar que todos los campos estén llenos
        for campo, valor in campos.items():
            if valor == "":
                messagebox.showwarning("Campos incompletos", f"El campo '{campo}' está vacío.")
                return

        # Confirmar antes de guardar
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de guardar este registro?")
        if not confirmar:
            return
        
        # Guardar en excel o base de datos
        try:
            archivo = "base_datos_salud_procesada.xlsx"

            if os.path.exists(archivo):
                df = pd.read_excel(archivo)
                df = df._append(campos, ignore_index=True)
            else:
                df = pd.DataFrame([campos])

            df.to_excel(archivo, index=False)

            messagebox.showinfo("Éxito", "Registro guardado exitosamente.")
            New_Reg.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el registro.\n{e}")

    # ------------- Función para volver sin guardar -------------
    def volver():
        confirmar = messagebox.askyesno("Volver", "¿Desea volver sin guardar?")
        if confirmar:
            New_Reg.destroy()

    # --------- Diseño de textos y cajas de entrada ----------
    labels = [
        "País",
        "Código ISO",
        "Año",
        "Reformas en salud",
        "Clase de gasto",
        "Gasto de capital en salud",
        "% del PIB destinado a salud",
        "Gasto de bolsillo",
        "Expectativa de vida",
    ]

    # Crear entradas
    entradas = []
    for i, texto in enumerate(labels):
        tk.Label(New_Reg, text=texto, font=("Arial", 11)).grid(row=i, column=0, padx=20, pady=7, sticky="w")
        entry = tk.Entry(New_Reg, width=35)
        entry.grid(row=i, column=1, padx=20, pady=7)
        entradas.append(entry)

    # Desempaquetar entradas
    (info1, info2, info3, info4, info5,
     info6, info7, info8, info9) = entradas

    # ---------- Botones ----------
    frame_botones = tk.Frame(New_Reg)
    frame_botones.grid(row=10, column=0, columnspan=2, pady=20)  # espacio de 1 cm

    btn_guardar = tk.Button(frame_botones, text="Guardar registro", width=20, height=2, command=guardar_registro)
    btn_volver = tk.Button(frame_botones, text="Volver sin guardar", width=20, height=2, command=volver)

    btn_guardar.grid(row=0, column=0, padx=20)
    btn_volver.grid(row=0, column=1, padx=20)
