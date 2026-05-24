# Celula Ventas TUP

Tecnicatura universitaria en programacion - Universidad Tecnologica Nacional

Organizacion empresarial - Unidad 4 - TP 2

Gestion colaborativa, control de versiones y organizacion empresarial

Alumno: Damian Geisser - 104105
Docente titular: Gabriela Martinez
Docente tutor: Martina Zabala

Mayo 2026

## Caso de estudio

Set de datos de ventas simuladas.

## Objetivo

Demostrar la gestion operativa del equipo desde la administracion de la infraestructura necesaria hasta la presentacion de informacion obtenida a partir de los datos.

El proyecto busca procesar datos comerciales, calcular indicadores basicos, generar resultados reproducibles y documentar el flujo de trabajo mediante Jira, Git, GitHub y Google Colab.

## Roles funcionales

P1 / Hugo: organizacion inicial del repositorio y estructura del proyecto.
P2 / Paco: desarrollo del script de analisis.
P3 / Luis: revision, documentacion, seguridad y control de calidad.

Los roles fueron representados mediante usuarios separados de Jira y GitHub para evidenciar el flujo colaborativo de trabajo.

## Herramientas utilizadas

- Jira: gestion de tareas, subtareas y seguimiento del flujo de trabajo.
- Git: control de versiones local.
- GitHub: repositorio remoto, ramas, Pull Request y revision de cambios.
- Google Colab: entorno de ejecucion del flujo tecnico.
- Python: lenguaje utilizado para el analisis.
- pandas: carga, exploracion, limpieza, imputacion y procesamiento del dataset.
- matplotlib: generacion del grafico de evolucion mensual de ventas

## Uso de pandas

La bilbioteca pandas se utiliza para trabajar con datos tabulares en formato CSV.

En el script principal se emplea para:

- cargar el archivo ventas.csv como un DataFrame;
- validar que el dataset contenga las columnas requeridas;
- convertir la columna de fecha a formato temporal;
- identificar valores nulos por columna;
- calcular el porcentaje de valores nulos respecto del total de registros;
- imputar valores faltantes cuando corresponde;
- calcular indicadores comerciales mediante agrupamientos;
- exportar resultados procesados en formato CSV.

El uso de pandas esta documentado en el codigo.

## Estructura del repositorio

```text
celula-ventas-tup/
├── datos/
│   └── ventas.csv
├── scripts/
│   └── analisis_ventas.py
├── resultados/
│   ├── grafico_ventas_mensuales.png
│   ├── reporte_nulos.csv
│   ├── resumen_indicadores.txt
│   ├── unidades_por_producto.csv
│   └── ventas_por_mes.csv
├── README.md
└── .gitignore
```

## Ejecucion

El analisis se ejecuta desde Google Colab utilizando el script ubicado en la carpeta /scripts.

```text
python scripts/analisis_ventas.py
```
### El script realiza las siguientes operaciones:

1. Carga el dataset desde /datos/ventas.csv.
2. Valida la estructura minima del archivo.
3. Explora valores nulos por columna.
4. Calcula el porcentaje de nulos sobre el total de registros.
5. Imputa valores faltantes cuando es posible.
6.Calcula indicadores comerciales.
7. Genera un grafico de evolucion mensual de ventas.
8. Exporta los resultados procesados en /resultados.

### Resultados generados

El analisis genera los siguientes archivos:

```text
/resultados/reporte_nulos.csv
/resultados/ventas_por_mes.csv
/resultados/unidades_por_producto.csv
/resultados/resumen_indicadores.txt
/resultados/grafico_ventas_mensuales.png
```

#### Descripcion de salidas:

- reporte_nulos.csv: cantidad y porcentaje de valores nulos por columna.
- ventas_por_mes.csv: ventas totales agrupadas por mes.
- unidades_por_producto.csv: unidades vendidas por producto.
- resumen_indicadores.txt: resumen de ventas totales y producto mas vendido.
- grafico_ventas_mensuales.png: visualizacion de la evolucion mensual de ventas.

### Flujo de trabajo

El trabajo se organizo mediante un flujo colaborativo basado en Jira, Git y GitHub.

#### El flujo aplicado fue:

1. Creacion de tareas y subtareas en Jira.
2. Inicializacion del repositorio por parte de Hugo.
3. Desarrollo tecnico en la rama feature/desarrollo-analisis por parte de Paco.
4. Registro de commits trazables con el identificador del ticket de Jira.
5. Creacion de Pull Request para solicitar la integracion.
6. Revision tecnica del Pull Request por parte de Luis.
7. Integracion final de los cambios a la rama main.

### Trazabilidad

Los commits del proyecto se registraron utilizando el identificador del ticket de Jira correspondiente.

### Seguridad y buenas practicas

El repositorio incluye un archivo .gitignore para evitar versionar archivos temporales, logs, checkpoints de notebooks, caches o archivos de entorno.

No se incluyen tokens, claves ni credenciales dentro del repositorio. La autenticacion contra GitHub se realizo mediante Personal Access Tokens cargados temporalmente desde Google Colab.
