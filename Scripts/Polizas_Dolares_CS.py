import pandas as pd
import os
import logging
from typing import Dict
from Scripts.import_data import leer_archivos
from Scripts.validar_trm import validar_diferencias
from Scripts.generar_plantilla import generar_plantilla

def ejecucion():

    # Obtener la ruta absoluta del directorio actual
    ruta_raiz = os.path.abspath(os.getcwd())
    print(ruta_raiz)
    # Ruta de la carpeta 01.Input
    archivo_detalle = os.path.join(ruta_raiz, "01.Input\Detalle\Detalle.xlsx")
    archivo_cabecera = os.path.join(ruta_raiz, "01.Input\Cabecera\Cabecera.xlsx")
    archivo_claves = os.path.join(ruta_raiz, "01.Input\Claves.xlsx")
    # Ruta de la carpeta 02.Output
    ruta_output = os.path.join(ruta_raiz, "02.Output")

    # Diccionario para los tipos de la data
    dict_detalle = {"Referencia":"str",
                    "NIT":"str",
                    "Lib.mayor":"str",
                    "Importe":"str",
                    "Div.":"str",
                    "CeBe":"str",
                    "Fe.valor":"str",
                    "VP":"str",
                    "Asignación":"str",
                    "Texto":"str",
                    "Clave ref.1":"str",
                    "Clave ref.2":"str",
                    "Clave referencia 3":"str",
                    "Fec.Expedi":"str",
                    "F.FinVigen":"str"}

    dict_cabecera = {"Referencia":"str",
                    "Tipo cambio":"str",
                    "Texto cab.documento":"str",
                    "Anul.con":"str"}

    dict_claves = {"Lib.mayor":"str",
                "Clave NC":"str",
                "Clave Producción":"str"}

    df_importado, df_cabecera, df_claves = leer_archivos(archivo_detalle,archivo_cabecera,archivo_claves,dict_detalle,dict_cabecera,dict_claves)

    df_validado = validar_diferencias(df_importado,df_cabecera,df_claves)

    df_plantilla_final = generar_plantilla(df_validado)

    df_plantilla_final.to_excel(f"{ruta_output}\Plantilla_Ajustes_TRM.xlsx", index=False)