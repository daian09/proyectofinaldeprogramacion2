import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
import sys

def resource_path(relative_path):
    """Devuelve la ruta correcta tanto para .py como para .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ------------------------------------------------------------
# VENTANA PARA AÑADIR REGISTRO
# ------------------------------------------------------------
def Add_Registro():
    New_Reg = tk.Toplevel()
    New_Reg.title("Añadir Registro")
    New_Reg.geometry("500x500")
    New_Reg.resizable(False, False)

    # --------------------------------------------------------
    # FUNCIÓN PARA GUARDAR EL REGISTRO
    # --------------------------------------------------------
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

        # Validación
        for campo, valor in campos.items():
            if valor == "":
                messagebox.showwarning("Campos incompletos", f"El campo '{campo}' está vacío.")
                return

        if not messagebox.askyesno("Confirmar", "¿Está seguro de guardar este registro?"):
            return

        # ----------------------------------------------------
        # RUTA REAL PARA GUARDAR EL EXCEL
        # ----------------------------------------------------
        # Cuando está en .exe, debemos guardar el excel en la carpeta del usuario,
        # NO dentro del .MEIPASS (carpeta temporal).
        ruta_excel = os.path.join(os.path.abspath("."), "base_datos_salud_procesada.xlsx")

        try:
            # Cargar archivo si existe
            if os.path.exists(ruta_excel):
                df = pd.read_excel(ruta_excel)
                df = pd.concat([df, pd.DataFrame([campos])], ignore_index=True)
            else:
                df = pd.DataFrame([campos])

            # Guardar archivo
            df.to_excel(ruta_excel, index=False)

            messagebox.showinfo("Éxito", "Registro guardado exitosamente.")
            New_Reg.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el registro.\n{e}")


    # --------------------------------------------------------
    # FUNCIÓN PARA VOLVER
    # --------------------------------------------------------
    def volver():
        if messagebox.askyesno("Volver", "¿Desea volver sin guardar?"):
            New_Reg.destroy()

    # --------------------------------------------------------
    # CAMPOS DE ENTRADA
    # --------------------------------------------------------
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

    entradas = []
    for i, texto in enumerate(labels):
        tk.Label(New_Reg, text=texto, font=("Arial", 11)).grid(row=i, column=0, padx=20, pady=7, sticky="w")
        entry = tk.Entry(New_Reg, width=35)
        entry.grid(row=i, column=1, padx=20, pady=7)
        entradas.append(entry)

    info1, info2, info3, info4, info5, info6, info7, info8, info9 = entradas

    # --------------------------------------------------------
    # BOTONES
    # --------------------------------------------------------
    frame_botones = tk.Frame(New_Reg)
    frame_botones.grid(row=10, column=0, columnspan=2, pady=20)

    tk.Button(frame_botones, text="Guardar registro", width=20, height=2, command=guardar_registro).grid(row=0, column=0, padx=20)
    tk.Button(frame_botones, text="Volver sin guardar", width=20, height=2, command=volver).grid(row=0, column=1, padx=20)

