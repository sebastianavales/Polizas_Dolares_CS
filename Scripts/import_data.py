import pandas as pd
import logging
from typing import Dict

def leer_archivos(detalle: str, cabecera: str, claves: str, dict_detalle: Dict[str, str], dict_cabecera: Dict[str, str], dict_claves: Dict[str, str]) -> pd.DataFrame:
    
    # Importar archivo que contiene el detalle
    try:
        df_importado = pd.read_excel(detalle, names=list(dict_detalle.keys()), dtype=dict_detalle)
        logging.info(f"Se importó el detalle.")
    except PermissionError:
        logging.error(f"Error: El archivo detalle está abierto, por favor cerrarlo.")
        return pd.DataFrame()
    except FileNotFoundError as e:
        logging.error('Error: El archivo detalle no fue encontrado en la ruta especificada.')
        return pd.DataFrame()
    except NameError as e:
        logging.error('Error: No se encontró la ruta especificada.')
        return pd.DataFrame()
    except KeyError:
        logging.error("Error: El archivo detalle no contiene la estructura esperada.")
        return pd.DataFrame()
    
    # Importar archivo que contiene la cabecera
    try:
        df_cabecera = pd.read_excel(cabecera, names=list(dict_cabecera.keys()), dtype=dict_cabecera)
        logging.info(f"Se importó la cabecera.")
    except PermissionError:
        logging.error(f"Error: El archivo cabecera está abierto, por favor cerrarlo.")
        return pd.DataFrame()
    except FileNotFoundError as e:
        logging.error('Error: El archivo cabecera no fue encontrado en la ruta especificada.')
        return pd.DataFrame()
    except NameError as e:
        logging.error('Error: No se encontró la ruta especificada.')
        return pd.DataFrame()
    except KeyError:
        logging.error("Error: El archivo cabecera no contiene la estructura esperada.")
        return pd.DataFrame()
    
    # Importar archivo que contiene las claves de contabilización
    try:
        df_claves = pd.read_excel(claves, names=list(dict_claves.keys()), dtype=dict_claves)
        logging.info(f"Se importó archivo claves contabilización.")
    except PermissionError:
        logging.error(f"Error: El archivo claves contabilización está abierto, por favor cerrarlo.")
        return pd.DataFrame()
    except FileNotFoundError as e:
        logging.error('Error: El archivo claves contabilización no fue encontrado en la ruta especificada.')
        return pd.DataFrame()
    except NameError as e:
        logging.error('Error: No se encontró la ruta especificada.')
        return pd.DataFrame()
    except KeyError:
        logging.error("Error: El archivo claves contabilización no contiene la estructura esperada.")
        return pd.DataFrame()

    return df_importado, df_cabecera, df_claves