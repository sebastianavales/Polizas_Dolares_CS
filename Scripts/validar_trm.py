import pandas as pd

def validar_diferencias(df_importado: pd.DataFrame, df_cabecera: pd.DataFrame, df_parametros: pd.DataFrame) -> pd.DataFrame:

    # Cruce de df_importado con df_cabecera
    df_importado = df_importado.merge(df_cabecera, on='Referencia', how='inner')
    # Cruce de df_importado con df_parametros
    df_importado = df_importado.merge(df_parametros, on='Lib.mayor', how='left')

    # Descartar referencias que ya hayan sido corregidas
    df_importado = df_importado.loc[df_importado['Texto cab.documento'] != 'ACTUALIZA TRM']

    # Transformaciones previas a la validación
    df_importado['Referencia_temp'] = df_importado['Referencia'].apply(lambda x: x[:-1] if x.endswith('I') else x)
    df_importado['Tipo cambio'] = df_importado['Tipo cambio'].apply(lambda x: round(float(f"{x.replace(' ', '').replace('.', '').replace(',', '')[:-5]}.{x.replace(' ', '').replace('.', '').replace(',', '')[-5:]}"), 2))

    # Validar referencias que tienen producción e IVA calculado con diferente TRM
    trm_unicas = df_importado.groupby('Referencia_temp').agg(TRM_Unicas=('Tipo cambio', 'nunique')).reset_index()

    # Filtrar solo registros de IVA para asignar la tasa correcta
    trm_iva = df_importado.loc[df_importado['Referencia'].str.endswith('I')].drop_duplicates(subset=['Referencia'])[['Referencia_temp','Tipo cambio']]
    trm_iva = trm_iva.rename(columns={'Tipo cambio': 'Tasa_Correcta'})
    
    # Identificar fecha valor para asignarla a las referencias faltantes
    fecha_val = df_importado.loc[~df_importado['Fe.valor'].isnull()].drop_duplicates(subset=['Referencia_temp'])[['Referencia_temp','Fe.valor']]
    fecha_val = fecha_val.rename(columns={'Fe.valor': 'Fecha_Valor'})

    # Identificar fecha expedición para asignarla a las referencias faltantes
    fecha_exp = df_importado.loc[~df_importado['Fec.Expedi'].isnull()].drop_duplicates(subset=['Referencia_temp'])[['Referencia_temp','Fec.Expedi']]
    fecha_exp = fecha_exp.rename(columns={'Fec.Expedi': 'Fecha_Expedicion'})

    # Identificar fecha fin vigencia para asignarla a las referencias faltantes
    fecha_fin = df_importado.loc[~df_importado['F.FinVigen'].isnull()].drop_duplicates(subset=['Referencia_temp'])[['Referencia_temp','F.FinVigen']]
    fecha_fin = fecha_fin.rename(columns={'F.FinVigen': 'Fecha_Fin_Vigencia'})

    # Cruce de df_importado con trm_unicas para llevar la columna TRM_Unicas a la BD principal
    df_importado = df_importado.merge(trm_unicas, on='Referencia_temp', how='left')

    # Cruce de df_importado con trm_iva para asignar la tasa correcta
    df_importado = df_importado.merge(trm_iva, on='Referencia_temp', how='left')

    # Cruce de df_importado con fecha_val para asignar la tasa correcta
    df_importado = df_importado.merge(fecha_val, on='Referencia_temp', how='left')

    # Cruce de df_importado con fecha_exp para asignar la tasa correcta
    df_importado = df_importado.merge(fecha_exp, on='Referencia_temp', how='left')

    # Cruce de df_importado con fecha_fin para asignar la tasa correcta
    df_importado = df_importado.merge(fecha_fin, on='Referencia_temp', how='left')

    # Corregir columna Tasa_Correcta cuando la referencia no tenga IVA
    df_importado['Tasa_Correcta'] = df_importado.apply(lambda x: x['Tipo cambio'] if pd.isna(x['Tasa_Correcta']) else x['Tasa_Correcta'], axis=1)

    # Filtrar aquellas referencias que tienen TRM diferentes
    df_validado = df_importado.loc[df_importado['TRM_Unicas'] != 1]
    df_validado = df_validado.sort_values(by=['Referencia', 'Lib.mayor'])

    return df_validado