import pandas as pd
import numpy as np
from datetime import datetime

def generar_plantilla(df_validado: pd.DataFrame) -> pd.DataFrame:

    # Definición de parámatros estandar
    fecha_hoy = datetime.now()
    fecha_documento = fecha_hoy.strftime("%d%m%Y")
    clase_documento = 'SL'
    sociedad =  1000
    periodo = fecha_hoy.strftime("%m")
    clave_moneda = 'USD'
    txt_cabecera = 'ACTUALIZAR TRM'
    indicador_IVA = 'GA'

    # Generación de plantilla para Notas Crédito
    df_plantilla1 = df_validado
    df_plantilla1 = df_plantilla1.rename(columns={'Tipo cambio': 'Tipo de Cambio'})
    df_plantilla1 = df_plantilla1.rename(columns={'Referencia': 'Número documento de referencia'})
    df_plantilla1 = df_plantilla1.rename(columns={'Lib.mayor': 'Cuenta de mayor de la contabilidad principal'})
    df_plantilla1 = df_plantilla1.rename(columns={'NIT': 'Nit'})
    df_plantilla1['Importe'] = df_plantilla1['Importe'].astype(float).abs()
    df_plantilla1 = df_plantilla1.rename(columns={'Importe': 'Importe en la moneda del documento'})
    df_plantilla1 = df_plantilla1.rename(columns={'Div.': 'División'})
    df_plantilla1['Fecha_Valor'] = pd.to_datetime(df_plantilla1['Fecha_Valor']).dt.strftime("%d%m%Y")
    df_plantilla1 = df_plantilla1.rename(columns={'Fecha_Valor': 'Fecha valor'})
    df_plantilla1 = df_plantilla1.rename(columns={'VP': 'Vía de pago'})
    df_plantilla1 = df_plantilla1.rename(columns={'Asignación': 'Número de asignación'})
    df_plantilla1 = df_plantilla1.rename(columns={'Texto': 'Texto posición'})
    df_plantilla1 = df_plantilla1.rename(columns={'Clave ref.1': 'Clave de referencia de interlocutor comercial'})
    df_plantilla1 = df_plantilla1.rename(columns={'Clave ref.2': 'Clave de referencia de interlocutor comercial 2'})
    df_plantilla1 = df_plantilla1.rename(columns={'Clave referencia 3': 'Clave de referencia para la posición de documento'})
    df_plantilla1 = df_plantilla1.rename(columns={'Fecha_Expedicion': 'Fecha expeENEion'})
    df_plantilla1 = df_plantilla1.rename(columns={'Fecha_Fin_Vigencia': 'Fecha fin vigencia'})
    df_plantilla1['Fecha de Documento'] = fecha_documento
    df_plantilla1['Clase de Documento'] = clase_documento
    df_plantilla1['Sociedad'] = sociedad
    df_plantilla1['Fecha Contabilización'] = fecha_documento
    df_plantilla1['Período'] = periodo
    df_plantilla1['Clave de Moneda'] = clave_moneda
    df_plantilla1['Fe.conversión '] = ""
    df_plantilla1['Texto de Cebecera'] = txt_cabecera
    df_plantilla1['Clave de contabilización para la siguiente posición'] = df_plantilla1['Clave NC']
    df_plantilla1['Número de identificación fiscal 1'] = np.select([df_plantilla1['Número de identificación fiscal 1'] == "X"],
                                                                   [df_plantilla1['Nit']],
                                                                   default="")
    df_plantilla1['Tipo de número de identificación fiscal'] = np.select([df_plantilla1['Tipo de número de identificación fiscal'] == "X"],
                                                                        ["31"],
                                                                        default="")
    df_plantilla1['In. CME'] = ""
    df_plantilla1['Indicador IVA'] = indicador_IVA
    df_plantilla1['InENEador retefuente WT_WITHCD'] = ""
    df_plantilla1['TP retefuente WITHT'] = ""
    df_plantilla1['inENEador reteica WT_WITHCD'] = ""
    df_plantilla1['TP reteica WITHT'] = ""
    df_plantilla1['inENEador reteiva WT_WITHCD'] = ""
    df_plantilla1['TP reteiva WITHT'] = ""
    df_plantilla1['inENEador retetimbre WT_WITHCD'] = ""
    df_plantilla1['Tp retetimbre WITHT'] = ""
    df_plantilla1['Clave de conENEiones de pago'] = ""
    df_plantilla1['Centro de coste'] = np.select([df_plantilla1['Centro de coste'] == "X"],                    
                                                [df_plantilla1['CeBe']],
                                                default="")
    df_plantilla1['Centro de beneficio'] = ""
    df_plantilla1['Días del descuento por pronto pago 1'] = ""
    df_plantilla1['Porcentaje de descuento por pronto pago 1'] = ""
    df_plantilla1['Días del descuento por pronto pago 2'] = ""
    df_plantilla1['Porcentaje de descuento por pronto pago 2'] = ""
    df_plantilla1['Plazo para conENEión de pago neto'] = ""
    df_plantilla1['Fecha base para cálculo del vencimiento'] = df_plantilla1['Fecha valor']
    df_plantilla1['ConENEión de pago fija'] = ""
    df_plantilla1['Base de descuento'] = ""
    df_plantilla1['Bloqueo pago'] = ""
    df_plantilla1['% DPP'] = ""
    df_plantilla1['Importe DPP'] = ""
    df_plantilla1['Número de orden'] = ""
    df_plantilla1['Tipo de banco interlocutor'] = ""
    df_plantilla1['Poliza líder'] = ""
    df_plantilla1['Cert.lider'] = ""
    df_plantilla1['Nombre'] = ""
    df_plantilla1['Orden'] = df_plantilla1['Número documento de referencia'].apply(lambda x: x[:-1] + "AB" if x.endswith('I') else x + "AA")
    df_plantilla1['Tipo'] = "NC"

    # Generación de plantilla para Corrección
    df_plantilla2 = df_validado
    df_plantilla2 = df_plantilla2.rename(columns={'Tasa_Correcta': 'Tipo de Cambio'})
    df_plantilla2 = df_plantilla2.rename(columns={'Referencia': 'Número documento de referencia'})
    df_plantilla2 = df_plantilla2.rename(columns={'Lib.mayor': 'Cuenta de mayor de la contabilidad principal'})
    df_plantilla2 = df_plantilla2.rename(columns={'NIT': 'Nit'})
    df_plantilla2['Importe'] = df_plantilla2['Importe'].astype(float).abs()
    df_plantilla2 = df_plantilla2.rename(columns={'Importe': 'Importe en la moneda del documento'})
    df_plantilla2 = df_plantilla2.rename(columns={'Div.': 'División'})
    df_plantilla2['Fecha_Valor'] = pd.to_datetime(df_plantilla2['Fecha_Valor']).dt.strftime("%d%m%Y")
    df_plantilla2 = df_plantilla2.rename(columns={'Fecha_Valor': 'Fecha valor'})
    df_plantilla2 = df_plantilla2.rename(columns={'VP': 'Vía de pago'})
    df_plantilla2 = df_plantilla2.rename(columns={'Asignación': 'Número de asignación'})
    df_plantilla2 = df_plantilla2.rename(columns={'Texto': 'Texto posición'})
    df_plantilla2 = df_plantilla2.rename(columns={'Clave ref.1': 'Clave de referencia de interlocutor comercial'})
    df_plantilla2 = df_plantilla2.rename(columns={'Clave ref.2': 'Clave de referencia de interlocutor comercial 2'})
    df_plantilla2 = df_plantilla2.rename(columns={'Clave referencia 3': 'Clave de referencia para la posición de documento'})
    df_plantilla2 = df_plantilla2.rename(columns={'Fecha_Expedicion': 'Fecha expeENEion'})
    df_plantilla2 = df_plantilla2.rename(columns={'Fecha_Fin_Vigencia': 'Fecha fin vigencia'})
    df_plantilla2['Fecha de Documento'] = fecha_documento
    df_plantilla2['Clase de Documento'] = clase_documento
    df_plantilla2['Sociedad'] = sociedad
    df_plantilla2['Fecha Contabilización'] = fecha_documento
    df_plantilla2['Período'] = periodo
    df_plantilla2['Clave de Moneda'] = clave_moneda
    df_plantilla2['Fe.conversión '] = ""
    df_plantilla2['Texto de Cebecera'] = txt_cabecera
    df_plantilla2['Clave de contabilización para la siguiente posición'] = df_plantilla2['Clave Producción']
    df_plantilla2['Número de identificación fiscal 1'] = np.select([df_plantilla2['Número de identificación fiscal 1'] == "X"],
                                                                   [df_plantilla2['Nit']],
                                                                   default="")
    df_plantilla2['Tipo de número de identificación fiscal'] = np.select([df_plantilla2['Tipo de número de identificación fiscal'] == "X"],
                                                                        ["31"],
                                                                        default="")
    df_plantilla2['In. CME'] = ""
    df_plantilla2['Indicador IVA'] = indicador_IVA
    df_plantilla2['InENEador retefuente WT_WITHCD'] = ""
    df_plantilla2['TP retefuente WITHT'] = ""
    df_plantilla2['inENEador reteica WT_WITHCD'] = ""
    df_plantilla2['TP reteica WITHT'] = ""
    df_plantilla2['inENEador reteiva WT_WITHCD'] = ""
    df_plantilla2['TP reteiva WITHT'] = ""
    df_plantilla2['inENEador retetimbre WT_WITHCD'] = ""
    df_plantilla2['Tp retetimbre WITHT'] = ""
    df_plantilla2['Clave de conENEiones de pago'] = ""
    df_plantilla2['Centro de coste'] = np.select([df_plantilla2['Centro de coste'] == "X"],                    
                                                [df_plantilla2['CeBe']],
                                                default="")
    df_plantilla2['Centro de beneficio'] = ""
    df_plantilla2['Días del descuento por pronto pago 1'] = ""
    df_plantilla2['Porcentaje de descuento por pronto pago 1'] = ""
    df_plantilla2['Días del descuento por pronto pago 2'] = ""
    df_plantilla2['Porcentaje de descuento por pronto pago 2'] = ""
    df_plantilla2['Plazo para conENEión de pago neto'] = ""
    df_plantilla2['Fecha base para cálculo del vencimiento'] = df_plantilla2['Fecha valor']
    df_plantilla2['ConENEión de pago fija'] = ""
    df_plantilla2['Base de descuento'] = ""
    df_plantilla2['Bloqueo pago'] = ""
    df_plantilla2['% DPP'] = ""
    df_plantilla2['Importe DPP'] = ""
    df_plantilla2['Número de orden'] = ""
    df_plantilla2['Tipo de banco interlocutor'] = ""
    df_plantilla2['Poliza líder'] = ""
    df_plantilla2['Cert.lider'] = ""
    df_plantilla2['Nombre'] = ""
    df_plantilla2['Orden'] = df_plantilla2['Número documento de referencia'].apply(lambda x: x[:-1] + "BB" if x.endswith('I') else x + "BA")
    df_plantilla2['Tipo'] = "Producción"

    # Lista de la estructura final de la plantilla
    estructura_final =[
                    "Fecha de Documento",
                    "Clase de Documento",
                    "Sociedad",
                    "Fecha Contabilización",
                    "Período",
                    "Clave de Moneda",
                    "Tipo de Cambio",
                    "Fe.conversión ",
                    "Número documento de referencia",
                    "Texto de Cebecera",
                    "Calc. Impuestos ",
                    "Clave de contabilización para la siguiente posición",
                    "Número de identificación fiscal 1",
                    "Tipo de número de identificación fiscal",
                    "In. CME",
                    "Cuenta de mayor de la contabilidad principal",
                    "Importe en la moneda del documento",
                    "Indicador IVA",
                    "InENEador retefuente WT_WITHCD",
                    "TP retefuente WITHT",
                    "inENEador reteica WT_WITHCD",
                    "TP reteica WITHT",
                    "inENEador reteiva WT_WITHCD",
                    "TP reteiva WITHT",
                    "inENEador retetimbre WT_WITHCD",
                    "Tp retetimbre WITHT",
                    "División",
                    "Clave de conENEiones de pago",
                    "Centro de coste",
                    "Centro de beneficio",
                    "Días del descuento por pronto pago 1",
                    "Porcentaje de descuento por pronto pago 1",
                    "Días del descuento por pronto pago 2",
                    "Porcentaje de descuento por pronto pago 2",
                    "Plazo para conENEión de pago neto",
                    "Fecha valor",
                    "Fecha base para cálculo del vencimiento",
                    "ConENEión de pago fija",
                    "Base de descuento",
                    "Vía de pago",
                    "Bloqueo pago",
                    "% DPP",
                    "Importe DPP",
                    "Número de asignación",
                    "Texto posición",
                    "Número de orden",
                    "Clave de referencia de interlocutor comercial",
                    "Clave de referencia de interlocutor comercial 2",
                    "Clave de referencia para la posición de documento",
                    "Tipo de banco interlocutor",
                    "Fecha expeENEion",
                    "Fecha fin vigencia",
                    "Poliza líder",
                    "Cert.lider",
                    "Nit",
                    "Nombre",
                    "Orden",
                    "Tipo"]

    # Aplicar estructura final a ambas plantillas
    df_plantilla1 = df_plantilla1[estructura_final]
    df_plantilla2 = df_plantilla2[estructura_final]

    # Concatenar ambas plantillas y ordenar
    df_plantilla_final = pd.concat([df_plantilla1, df_plantilla2], axis=0, ignore_index=True)
    df_plantilla_final = df_plantilla_final.sort_values(by=['Orden','Clave de contabilización para la siguiente posición'])
    df_plantilla_final = df_plantilla_final.drop(columns=['Orden'])

    # Generar Agrupador de Documentos
    agrupador_temp = df_plantilla_final[['Número documento de referencia', 'Tipo']].drop_duplicates(subset=['Número documento de referencia', 'Tipo'])
    agrupador_temp['Agrupdor de Documentos'] = range(1, len(agrupador_temp) + 1)
    df_plantilla_final = df_plantilla_final.merge(agrupador_temp, on=['Número documento de referencia', 'Tipo'])
    df_plantilla_final = df_plantilla_final.drop(columns=['Tipo'])
    col_agrup = df_plantilla_final.pop('Agrupdor de Documentos')
    df_plantilla_final.insert(0, 'Agrupdor de Documentos', col_agrup)
        
    return df_plantilla_final