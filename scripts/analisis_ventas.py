from pathlib import Path

import pandas as pd


# Este script utiliza pandas para trabajar con datos tabulares de ventas.
# Pandas se usa para:
# - cargar el archivo CSV desde la carpeta /datos;
# - representar los datos como un DataFrame;
# - revisar columnas, tipos de datos y valores faltantes;
# - preparar el dataset para cálculos comerciales posteriores.

BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_DIR = BASE_DIR / "datos"
RESULTADOS_DIR = BASE_DIR / "resultados"

ARCHIVO_DATOS = DATOS_DIR / "ventas.csv"

COLUMNAS_REQUERIDAS = [
    "fecha",
    "producto",
    "cantidad",
    "precio_unitario",
]


def cargar_datos(ruta_archivo: Path) -> pd.DataFrame:
    """
    Carga el archivo CSV de ventas como DataFrame de pandas.

    El DataFrame permite aplicar validaciones y transformaciones sobre columnas,
    como convertir fechas, revisar valores nulos y preparar los datos para el
    análisis comercial.
    """
    if not ruta_archivo.exists():
        raise FileNotFoundError(f"No se encontró el archivo de datos: {ruta_archivo}")

    ventas = pd.read_csv(ruta_archivo)

    columnas_faltantes = [
        columna for columna in COLUMNAS_REQUERIDAS
        if columna not in ventas.columns
    ]

    if columnas_faltantes:
        raise ValueError(
            "El dataset no contiene las columnas requeridas: "
            f"{columnas_faltantes}"
        )

    ventas["fecha"] = pd.to_datetime(ventas["fecha"], errors="coerce")

    return ventas


def explorar_datos(ventas: pd.DataFrame) -> pd.DataFrame:
    """
    Revisa la presencia de valores nulos por columna.

    Para cada columna se calcula:
    - cantidad de valores nulos;
    - porcentaje de nulos sobre el total de registros.

    Esta exploración permite decidir si corresponde imputar datos faltantes
    o documentar limitaciones del dataset.
    """
    total_registros = len(ventas)

    reporte_nulos = pd.DataFrame({
        "columna": ventas.columns,
        "cantidad_nulos": ventas.isnull().sum().values,
        "porcentaje_nulos": (ventas.isnull().sum().values / total_registros) * 100,
    })

    return reporte_nulos


def main():
    """
    Punto de entrada del análisis de ventas.
    """
    print("Iniciando análisis de ventas...")
    print(f"Archivo de datos: {ARCHIVO_DATOS}")

    ventas = cargar_datos(ARCHIVO_DATOS)
    reporte_nulos = explorar_datos(ventas)

    print("\nPrimeras filas del dataset:")
    print(ventas.head())

    print("\nColumnas disponibles:")
    print(list(ventas.columns))

    print("\nTipos de datos:")
    print(ventas.dtypes)

    print("\nReporte de valores nulos:")
    print(reporte_nulos)


if __name__ == "__main__":
    main()
