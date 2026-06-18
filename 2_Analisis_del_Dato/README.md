# 2 · Análisis del Dato

Segunda entrega con nota del TFG. Sobre el panel construido en la Ingeniería del Dato, desarrolla la capa de modelado: determinantes del alquiler (explicación), tipologías provinciales (agrupación) y proyección de la tasa de esfuerzo (predicción).

## Contenido de la carpeta

| Carpeta | Qué hay |
|---|---|
| `notebooks/` | `Notebook_AnalisisDato.ipynb` — cuaderno completo ejecutado (Google Colab); `generar_diagrama_flujo_analisis.py` — script que genera la Figura 1 |
| `data/clean/` | Paneles de entrada heredados de la Ingeniería del Dato (panel principal, panel por edad y panel de población joven) |
| `figuras/` | Figuras 1–6 de la memoria (PNG) |
| `tablas/` | Tablas 1–6 de la memoria, en un Excel con seis hojas y, en `csv/`, una por tabla |
| `memoria/` | `Entrega_Analisis del Dato.pdf` — documento final de la entrega (PDF) |

## Modelos y resultados

- **Supervisado (determinantes del alquiler):** competición entre Ridge (modelo base) frente a Random Forest y Gradient Boosting, con validación temporal. Gana Ridge (R² fuera de muestra ≈ 0,94, frente a 0,61 y 0,73), en línea con el principio de que el dato gobierna la elección del método.
- **Inferencia complementaria:** efectos fijos provinciales (LSDV) con errores estándar clusterizados y diagnóstico de colinealidad (VIF).
- **No supervisado:** K-Means con k = 3 para las tipologías provinciales (robustez ARI = 0,86 frente al agrupamiento jerárquico).
- **Series temporales:** escenario de la tasa de esfuerzo 2025–2027 con ARIMA, presentado con intervalos de confianza y como escenario, no como predicción puntual.
- **Métricas:** MAE, RMSE, MAPE y R², todas calculadas fuera de muestra.

## Reproducción

El cuaderno se entrega **ya ejecutado**, con todas sus salidas visibles. Toma como entrada los paneles de `data/clean/` (las salidas de la Ingeniería del Dato), incluidos en este repositorio.

Está desarrollado en **Google Colab** y sus rutas apuntan a la carpeta del proyecto en Google Drive, de modo que para **volver a ejecutarlo** hay que colocar esos paneles en la ruta de Drive (o adaptar las rutas del cuaderno a la ubicación local de `data/clean/`).

> Carpeta de trabajo en Google Drive (cuaderno y datos en su estructura original, solo lectura): https://drive.google.com/drive/folders/18d1wfJ25i_LwQmnLMyLlbNR1vx0CBgS5?usp=sharing
