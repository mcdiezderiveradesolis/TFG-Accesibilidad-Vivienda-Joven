# 1 · Ingeniería del Dato

Primera entrega con nota del TFG. Construye un **panel provincial integrado y reproducible** (48 provincias de régimen fiscal común, 2011–2024) a partir de fuentes oficiales, siguiendo el esquema ETL.

## Contenido de la carpeta

| Carpeta | Qué hay |
|---|---|
| `notebooks/` | `Notebook_IngenieriaDato.ipynb` — cuaderno completo ejecutado (Google Colab), de la extracción a la auditoría final |
| `data/raw/` | Fuentes originales sin modificar (SERPAVI, 42 PDF de la AEAT, Excel del INE, SMI, Padrón) |
| `data/clean/` | Salidas del pipeline: panel principal, panel por edad, panel de población joven y diccionario de variables |
| `figuras/` | Figuras 1–8 de la memoria (PNG; diagrama de flujo también en SVG) |
| `tablas/` | Tablas 1–8 de la memoria, en un Excel con ocho hojas y, en `csv/`, una por tabla |
| `memoria/` | `Entrega_Ingenieria del Dato.pdf` — documento final de la entrega (PDF) |

## Resultado

- **Panel principal:** 672 observaciones × 30 variables (48 provincias × 14 años).
- **Paneles auxiliares:** por edad (2.016 obs.) y de población joven (576 obs.).
- Indicador central: **tasa de esfuerzo** (alquiler mensual / salario neto mensual de la población joven), contrastada con el umbral del 30 %.

## Reproducción

El cuaderno se entrega **ya ejecutado**, con todas sus salidas visibles. Todo lo necesario para reproducirlo está en este repositorio: el cuaderno (`notebooks/`) y los datos (`data/raw/` y `data/clean/`).

Está desarrollado en **Google Colab** y sus rutas apuntan a la carpeta del proyecto en Google Drive, de modo que para **volver a ejecutarlo** hay que colocar los ficheros de `data/raw/` en esa ruta de Drive (o adaptar las rutas del cuaderno a la ubicación local de `data/`). Al arranque, el cuaderno valida que están los archivos de las ocho fuentes y se detiene si falta alguno.

> Carpeta de trabajo en Google Drive (cuaderno y datos en su estructura original, solo lectura): https://drive.google.com/drive/folders/18d1wfJ25i_LwQmnLMyLlbNR1vx0CBgS5?usp=sharing

> Nota: `data/raw/SERPAVI.xlsx` (~68 MB) se incluye en el repositorio y se sube sin problema con GitHub Desktop (el límite es 100 MB por archivo; solo aparece un aviso informativo a partir de 50 MB).
