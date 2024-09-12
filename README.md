# Polizas_Dolares_CS

## Estructura del Proyecto 📦

    ├── 01.Input                                <- Carpeta de ingreso de recursos iniciales y parametros para ejecución.
    |    ├── Cabecera                           <- Carpeta de almacenamiento del archivo cabecera.
    |    |      └── Cabecera.xlsx               <- Archivo que contiene la cabecera en formato xlsx.
    |    ├── Detalle                            <- Carpeta de almacenamiento del archivo detalle.
    |    |      └── Detalle.xlsx                <- Archivo que contiene el detalle en formato xlsx.
    |    └── Parametros.xlsx                    <- Archivo de parametros esenciales para la ejecución en formato xlsx.
    ├── 02.Output                               <- Carpeta de salida de las plantillas generadas.
    ├── 03.Notebooks                            <- Carpeta que contiene los notebooks usados durante el desarrollo.
    |    └── Polizas_Dolares_CS.ipynb           <- Notebook de desarrollo y pruebas del programa. 
    ├── Scripts                                 <- Carpeta con módulos.
    │    ├── __init__.py                        <- Inicializador del módulo.
    │    ├── generar_plantilla.py               <- Funciones de generación de plantilla.
    │    ├── gui.py                             <- Funciones de interfaz del proyecto.
    │    ├── import_data.py                     <- Funciones de importacion de recursos.
    │    ├── Polizas_Dolares_CS.py              <- Funciones de ejecución del programa.
    |    ├── requirements.txt                   <- Archivo que contiene las librerias necesarias de Python.
    │    └── validar_trm.py                     <- Funciones de validación de TRM.
    ├── .gitignore                              <- Ignorar archivos que no son código.
    ├── app.log                                 <- Log de ejecución del desarrollo.
    ├── main.py                                 <- Ejecutable del proyecto.
    └── README.md                               <- La guía del proyecto.