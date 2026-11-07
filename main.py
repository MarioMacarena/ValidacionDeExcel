from tabulate import tabulate
from pathlib import Path
import pandas as pd
from validators import (
    validar_beneficiario,
    validar_clabe,
    validar_importe
)

ARCHIVO_ENTRADA = Path("DatosEntrada.xlsx")
ARCHIVO_SALIDA = Path("resultado.xlsx")

# Comprobamos que el archivo exista antes de intentar leerlo
if not ARCHIVO_ENTRADA.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo: {ARCHIVO_ENTRADA}"
    )

# Leemos el archivo Excel
df = pd.read_excel(ARCHIVO_ENTRADA)

# Comprobamos que existan las columnas necesarias para validar
columnas_requeridas = [
    "Beneficiario",
    "CLABE",
    "Importe"
]

columnas_faltantes = [
    columna for columna in columnas_requeridas
    if columna not in df.columns
]

if columnas_faltantes:
    raise ValueError(
        f"Faltan columnas en el archivo: {columnas_faltantes}"
    )

# Listas para guardar los resultados
estados = []
motivos_errores = []

for indice, fila in df.iterrows():
    # Validamos cada campo
    error_beneficiario = validar_beneficiario(
        fila["Beneficiario"]
    )

    error_clabe = validar_clabe(
        fila["CLABE"]
    )

    error_importe = validar_importe(
        fila["Importe"]
    )

    # Reunimos los errores encontrados
    errores = [
        error for error in [
            error_beneficiario,
            error_clabe,
            error_importe
        ]
        if error is not None
    ]

    # Determinamos el estado del registro
    if errores:
        estados.append("inválido")
        motivos_errores.append("; ".join(errores))
    else:
        estados.append("válido")
        motivos_errores.append("")

# Creamos una copia para no modificar el excel original
df_resultado = df.copy()

# Agregamos las columnas de validación a la copia
df_resultado["estado"] = estados
df_resultado["motivo_error"] = motivos_errores

# Guardamos el resultado en un nuevo archivo
df_resultado.to_excel(ARCHIVO_SALIDA, index=False)

# Resumen de los resultados
print("\nProcesamiento completado correctamente.")
print(f"Total de registros: {len(df_resultado)}")
print(f"Registros válidos: {(df_resultado['estado'] == 'válido').sum()}")
print(f"Registros inválidos: {(df_resultado['estado'] == 'inválido').sum()}")
print(f"Archivo generado: {ARCHIVO_SALIDA}")

# Mostramos los resultados procesados
print("\nResultados:")

print(
    tabulate(
        df_resultado,
        headers="keys",
        tablefmt="grid",
        showindex=False
    )
)
