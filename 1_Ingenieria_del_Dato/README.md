# 1 · Ingeniería del Dato

Primera entrega con nota del TFG. Construye un **panel provincial integrado y reproducible** (48 provincias de régimen fiscal común, 2011–2024) a partir de fuentes oficiales, siguiendo el esquema ETL.

## Contenido de la carpeta

| Carpeta | Qué hay |
|---|---|
| `notebooks/` | `Notebook_IngenieriaDato.ipynb` — cuaderno completo ejecutado (Google Colab), de la extracción a la auditoría final |
| `data/raw/` | Fuentes originales sin modificar (SERPAVI, 42 PDF de la AEAT, Excel del INE, SMI, Padrón) |
| `data/clean/` | Salidas del pipeline: panel principal, panel por edad, panel de población joven y diccionario de variables |
| `figuras/` | Figuras 1–8 de la memoria (PNG; diagrama de flujo también en SVG) |
| `memoria/` | `MEMORIA_Ingenieria_del_Dato.docx` — documento de la entrega |

## Resultado

- **Panel principal:** 672 observaciones × 30 variables (48 provincias × 14 años).
- **Paneles auxiliares:** por edad (2.016 obs.) y de población joven (576 obs.).
- Indicador central: **tasa de esfuerzo** (alquiler mensual / salario neto mensual de la población joven), contrastada con el umbral del 30 %.

## Reproducción

El cuaderno está pensado para Google Colab con los datos en Google Drive. Las rutas apuntan a la carpeta del proyecto en Drive; basta con colocar los ficheros de `data/raw/` en esa ruta y ejecutar **Entorno de ejecución → Reiniciar y ejecutar todo**. El cuaderno valida al arranque que están los archivos de las ocho fuentes y se detiene si falta alguno.

> Nota: `data/raw/SERPAVI.xlsx` (~80 MB) puede superar el límite de subida por web de GitHub; si es así, se enlaza desde Google Drive en lugar de subirlo al repositorio.
