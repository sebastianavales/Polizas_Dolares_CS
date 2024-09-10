import pandas as pd
import os
import logging
from typing import Dict
from Scripts import import_data
from Scripts import validar_trm

# Obtener la ruta absoluta del directorio actual
ruta_raiz = os.path.abspath(os.getcwd())
# Ruta de la carpeta 01.Input
archivo_detalle = os.path.join(ruta_raiz, "01.Input\Detalle.xlsx")
archivo_cabecera = os.path.join(ruta_raiz, "01.Input\Cabecera.xlsx")
# Ruta de la carpeta 02.Output
ruta_output = os.path.join(ruta_raiz, "02.Output")

# Diccionario para los tipos de la data
dict_detalle = {"Referencia":"str",
                          "Asignación":"str",
                          "Soc.":"str",
                          "Acreedor":"str",
                          "Clave ref.1":"str",
                          "Clave ref.2":"str",
                          "Cuenta":"str",
                          "Clave referencia 3":"str",
                          "Período":"str",
                          "Período":"str",
                          "Cl.coste":"str",
                          "CeBe":"str",
                          "CeBe int.":"str",
                          "Div.":"str",
                          "NIT":"str",
                          "Deudor":"str",
                          "Lib.mayor":"str",
                          "Cta.mayor":"str",
                          "VP":"str",
                          "Fec.Expedi":"str",
                          "Fecha doc.":"str",
                          "Fe.contab.":"str",
                          "ML2":"str",
                          "Importe":"str",
                          "ImpteML2":"str",
                          "Importe en ML3":"str",
                          "Tp.camb.ef.":"str",
                          "MonPa":"str",
                          "Compens.":"str",
                          "Fe.valor":"str",
                          "Fecha pago":"str",
                          "Registrado":"str"}

dict_cabecera = {"Referencia":"str",
                 "Texto cab.documento":"str",
                 "Anul.con":"str",
                 "Tipo cambio":"str"}
      
df_importado, df_cabecera = import_data.leer_archivos(archivo_detalle,archivo_cabecera,dict_detalle,dict_cabecera)

df_validado = validar_trm.validar_diferencias(df_importado, df_cabecera)

df_validado.to_excel('Prueba_Funciones.xlsx', index=False)
