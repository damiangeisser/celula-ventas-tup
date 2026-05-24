from pathlib import Path

import pandas as pd


# Este script utiliza pandas para trabajar con datos tabulares de ventas.
# Pandas se usa para:
# - cargar el archivo CSV desde la carpeta /datos;
# - representar los datos como un DataFrame;
# - revisar columnas, tipos de datos y valores faltantes;
# - imputar valores faltantes cuando es posible;
# - calcular indicadores comerciales mediante operaciones de agrupamiento.

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
    Calcula cantidad y porcentaje de valores nulos por columna.
    """
    total_registros = len(ventas)

    reporte_nulos = pd.DataFrame({
        "columna": ventas.columns,
        "cantidad_nulos": ventas.isnull().sum().values,
        "porcentaje_nulos": (ventas.isnull().sum().values / total_registros) * 100,
    })

    return reporte_nulos


def imputar_datos(ventas: pd.DataFrame) -> pd.DataFrame:
    """
    Imputa valores faltantes para permitir el análisis.

    Criterios aplicados:
    - producto: se completa con "Sin identificar" si falta el nombre.
    - cantidad: se completa con la mediana de cantidad vendida.
    - precio_unitario: se completa con la mediana del precio del mismo producto.
      Si no existe referencia para ese producto, se usa la mediana general.
    """
    ventas_limpias = ventas.copy()

    ventas_limpias["producto"] = ventas_limpias["producto"].fillna("Sin identificar")

    mediana_cantidad = ventas_limpias["cantidad"].median()
    ventas_limpias["cantidad"] = ventas_limpias["cantidad"].fillna(mediana_cantidad)

    mediana_precio_general = ventas_limpias["precio_unitario"].median()

    ventas_limpias["precio_unitario"] = (
        ventas_limpias
        .groupby("producto")["precio_unitario"]
        .transform(lambda serie: serie.fillna(serie.median()))
    )

    ventas_limpias["precio_unitario"] = ventas_limpias["precio_unitario"].fillna(
        mediana_precio_general
    )

    ventas_limpias["total_venta"] = (
        ventas_limpias["cantidad"] * ventas_limpias["precio_unitario"]
    )

    return ventas_limpias


def calcular_indicadores(ventas: pd.DataFrame) -> dict:
    """
    Calcula indicadores comerciales básicos a partir del dataset limpio.
    """
    ventas_totales = ventas["total_venta"].sum()

    unidades_por_producto = (
        ventas.groupby("producto", as_index=False)["cantidad"]
        .sum()
        .sort_values("cantidad", ascending=False)
    )

    producto_mas_vendido = unidades_por_producto.iloc[0]

    ventas_por_mes = (
        ventas.assign(mes=ventas["fecha"].dt.to_period("M").astype(str))
        .groupby("mes", as_index=False)["total_venta"]
        .sum()
        .sort_values("mes")
    )

    return {
        "ventas_totales": ventas_totales,
        "producto_mas_vendido": producto_mas_vendido,
        "ventas_por_mes": ventas_por_mes,
        "unidades_por_producto": unidades_por_producto,
    }


def main():
    """
    Punto de entrada del análisis de ventas.
    """
    print("Iniciando análisis de ventas...")
    print(f"Archivo de datos: {ARCHIVO_DATOS}")

    ventas = cargar_datos(ARCHIVO_DATOS)
    reporte_nulos = explorar_datos(ventas)
    ventas_limpias = imputar_datos(ventas)
    indicadores = calcular_indicadores(ventas_limpias)

    print("\nPrimeras filas del dataset original:")
    print(ventas.head())

    print("\nReporte de valores nulos:")
    print(reporte_nulos)

    print("\nPrimeras filas del dataset limpio:")
    print(ventas_limpias.head())

    print("\nVentas totales:")
    print(indicadores["ventas_totales"])

    print("\nProducto más vendido:")
    print(indicadores["producto_mas_vendido"])

    print("\nVentas por mes:")
    print(indicadores["ventas_por_mes"])

    print("\nUnidades por producto:")
    print(indicadores["unidades_por_producto"])


if __name__ == "__main__":
    main()
