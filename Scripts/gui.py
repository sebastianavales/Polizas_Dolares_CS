import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
import logging
import Scripts.Polizas_Dolares_CS as PDCS

# Hardcode - Parametros
color_fondo =  "#DFEAFF"
color_azul_vivo = "#2D6DF6"
color_azul_sura = "#0033A0"
blanco = "#FFFFFF"

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.wm_minsize(600, 250)
        self.title("GUI by GI-TI")
        self.configure(bg=color_fondo) 
        self.v = tk.IntVar()
        self.v.set(1)

        self.create_widgets()

    def create_widgets(self):

        #####################################################################################################
        #Titulo
        #####################################################################################################
        self.title_frame = tk.Frame(self, bg=color_fondo)
        self.title_frame.pack(fill="x", pady=10)
        self.title_label = tk.Label(self.title_frame, text="Ajuste TRM Generales por Cliente Servidor", bg=color_fondo, font=("Arial", 20, "bold"), fg=color_azul_vivo)
        self.title_label.pack(expand=True)
        
        #####################################################################################################
        # Opciones
        #####################################################################################################
        
        self.opciones_frame = tk.Frame(self, bg=color_fondo)
        self.opciones_frame.pack(fill="x", pady=10)
        self.opcion1 = tk.Radiobutton(self.opciones_frame, text="General", padx = 20, pady = 5, variable=self.v, value=1, bg=color_fondo, font=("Arial", 15, "bold"), fg=color_azul_sura, activebackground=color_fondo)
        self.opcion1.pack(anchor=tk.W)
        self.opcion2 = tk.Radiobutton(self.opciones_frame, text="Especifico",  padx = 20, pady = 5, variable=self.v, value=2, bg=color_fondo, font=("Arial", 15, "bold"), fg=color_azul_sura, activebackground=color_fondo)
        self.opcion2.pack(anchor=tk.W)

        #####################################################################################################
        # Separador
        #####################################################################################################
        self.separador_frame = tk.Frame(self, bg=color_fondo)
        self.separador_frame.pack(fill="x", pady=10)
        self.separador = ttk.Separator(self.separador_frame)
        self.separador.pack(fill="x", padx=20)  # Ajusta el padding para espaciar los bordes
        
        #####################################################################################################
        # Frame para el ingreso
        #####################################################################################################
        self.main_frame = tk.Frame(self, bg=color_fondo)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=2)
        self.main_frame.columnconfigure(3, weight=1)
        self.main_frame.columnconfigure(4, weight=1)
        self.main_frame.columnconfigure(5, weight=2)
        self.main_frame.pack(fill="x", padx="20")

        # Columna 1 - Labels
        tk.Label(self.main_frame, text="Referencia sin 'I':", font=("Arial",14), bg=color_fondo, fg=color_azul_sura)\
            .grid(row=0, column=0, padx=5, pady=5, sticky="e")
       
        # Columna 2 - Entrys
        self.entry_numero_recibo = tk.Entry(self.main_frame)
        self.entry_numero_recibo.configure(state='normal', font=14)
        self.entry_numero_recibo.grid(row=0, column=1, ipadx=20, pady=5, sticky="we")

        self.select_button = tk.Button(self.main_frame, text="Generar Plantilla", command=self.generar_plantilla, bg="#FFFFFF", fg=color_azul_sura)
        self.select_button.grid(row=0, column=5, sticky= "e", padx=2)

        # Footer
        #####################################################################################################
        self.footer = tk.Label(self, text="Ajuste TRM Generales por cliente servidor", bg=color_fondo, font=("Arial", 10))        
        self.footer.pack(side=tk.BOTTOM, pady=10)
        #####################################################################################################
        
    def generar_plantilla(self):

        if self.v.get() == 1:
            # Llama a la función correspondiente a 'opcion1'
            print('Se seleccionó la opción "General"')
            PDCS.ejecucion_general()
            messagebox.showinfo("Correcto", "Se generó la plantilla correctamente.") 
            print('Se generó la plantilla correctamente.')

        elif self.v.get() == 2:
            # Llama a la función correspondiente a 'opcion2'
            print('Se seleccionó la opción "Específico"')
            PDCS.ejecucion_especifico(str(self.entry_numero_recibo.get()))
            messagebox.showinfo("Correcto", f"Se generó la plantilla para la referencia {self.entry_numero_recibo.get()} correctamente.") 
            print(f'Se generó la plantilla para la referencia {self.entry_numero_recibo.get()} correctamente.')           