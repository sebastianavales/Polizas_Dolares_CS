import pandas as pd
import os
import logging
from typing import Dict
from Scripts.import_data import leer_archivos
from Scripts.validar_trm import validar_diferencias
from Scripts.generar_plantilla import generar_plantilla

def ejecucion_general():

    # Obtener la ruta absoluta del directorio actual
    ruta_raiz = os.path.abspath(os.getcwd())

    # Ruta de la carpeta 01.Input
    archivo_detalle = os.path.join(ruta_raiz, "01.Input\Detalle\Detalle.xlsx")
    archivo_cabecera = os.path.join(ruta_raiz, "01.Input\Cabecera\Cabecera.xlsx")
    archivo_parametros = os.path.join(ruta_raiz, "01.Input\Parametros.xlsx")
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

    dict_parametros = {"Lib.mayor":"str",
                       "Clave NC":"str",
                       "Clave Producción":"str",
                       "Calc. Impuestos ":"str",
                       "Calc. Impuestos ":"str",
                       "Número de identificación fiscal 1":"str",
                       "Tipo de número de identificación fiscal":"str",
                       "Centro de coste":"str"}

    df_importado, df_cabecera, df_parametros = leer_archivos(archivo_detalle,archivo_cabecera,archivo_parametros,dict_detalle,dict_cabecera,dict_parametros)

    df_validado = validar_diferencias(df_importado,df_cabecera,df_parametros)

    df_plantilla_final = generar_plantilla(df_validado)

    df_plantilla_final.to_excel(f"{ruta_output}\Plantilla_Ajustes_TRM.xlsx", index=False)

def ejecucion_especifico(referencia: str):

    referencia_iva = referencia + "I"

    # Obtener la ruta absoluta del directorio actual
    ruta_raiz = os.path.abspath(os.getcwd())

    # Ruta de la carpeta 01.Input
    archivo_detalle = os.path.join(ruta_raiz, "01.Input\Detalle\Detalle.xlsx")
    archivo_cabecera = os.path.join(ruta_raiz, "01.Input\Cabecera\Cabecera.xlsx")
    archivo_parametros = os.path.join(ruta_raiz, "01.Input\Parametros.xlsx")
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

    dict_parametros = {"Lib.mayor":"str",
                       "Clave NC":"str",
                       "Clave Producción":"str",
                       "Calc. Impuestos ":"str",
                       "Calc. Impuestos ":"str",
                       "Número de identificación fiscal 1":"str",
                       "Tipo de número de identificación fiscal":"str",
                       "Centro de coste":"str"}

    df_importado, df_cabecera, df_parametros = leer_archivos(archivo_detalle,archivo_cabecera,archivo_parametros,dict_detalle,dict_cabecera,dict_parametros)

    df_validado = validar_diferencias(df_importado,df_cabecera,df_parametros)

    df_validado = df_validado.loc[(df_validado['Referencia'] == referencia) | (df_validado['Referencia'] == referencia_iva)]

    df_plantilla_final = generar_plantilla(df_validado)

    df_plantilla_final.to_excel(f"{ruta_output}\Plantilla_Ajustes_TRM_{referencia}.xlsx", index=False)