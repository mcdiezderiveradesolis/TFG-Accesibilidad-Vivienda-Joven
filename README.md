# TFG · Desequilibrio entre el precio del alquiler y el salario de la población joven en España (2011–2024)

Trabajo de Fin de Grado del Doble Grado en Business Analytics + ADE (Universidad Francisco de Vitoria).

Análisis del desequilibrio entre el precio del alquiler y el salario de la población joven en España a **escala provincial** (48 provincias de régimen fiscal común), con un enfoque **explicativo y predictivo**.

## Pregunta de investigación

¿Cuál es la magnitud del desequilibrio entre alquiler y salario joven a escala provincial, cómo varía entre provincias y en el tiempo, y qué escenarios cabe proyectar? El indicador central es la **tasa de esfuerzo** (alquiler mensual / salario neto mensual de la población joven), contrastada con el umbral del **30 %** de asequibilidad.

## Estructura del repositorio

El TFG se compone de **cuatro entregas**: los tres pilares con nota y, después, la memoria completa que las integra. Cada pilar tiene su carpeta para que el corrector localice su parte rápido.

| Carpeta | Contenido | Estado |
|---|---|---|
| [`1_Ingenieria_del_Dato/`](1_Ingenieria_del_Dato/) | Construcción del panel provincial integrado y reproducible | Completada |
| [`2_Analisis_del_Dato/`](2_Analisis_del_Dato/) | Modelado explicativo, agrupación y predicción | Completada |
| [`3_Analisis_de_Negocio/`](3_Analisis_de_Negocio/) | Lectura de negocio e implicaciones | Completada |
| [`memoria_final/`](memoria_final/) | Memoria completa que integra los tres pilares | Completada |
| [`docs/`](docs/) | Documentación metodológica: historial de decisiones, diccionario de variables e inventario de fuentes | Actualizada |

Dentro de cada carpeta de entrega se mantiene la misma organización (`notebooks/`, `data/` con `raw` y `clean`, `figuras/` y `memoria/`); el pilar de Análisis de Negocio, al ser de redacción y no incorporar cuaderno ni datos propios, incluye `memoria/` y `tablas/` (tres tablas de elaboración propia: síntesis de objetivos, matriz de decisión 2×2 y ficha del producto).

## Datos y fuentes

El panel se construye a partir de **siete fuentes oficiales** de cuatro organismos, más una **octava fuente complementaria** para dimensionar el impacto humano:

| # | Fuente | Organismo | Rol |
|---|---|---|---|
| 1 | SERPAVI (alquiler mediano provincial) | Min. de Vivienda | Panel — variable dependiente |
| 2 | Mercado de Trabajo, Modelo 190 (salario por edad, 42 PDF) | AEAT | Panel — denominador del KPI |
| 3 | EPA provincial (t=65349) | INE | Panel — paro (control) |
| 4 | IPC (t=76136) | INE | Panel — deflactor nacional |
| 5 | Salario mínimo interprofesional | Min. de Trabajo | Panel — contexto |
| 6 | EAES (t=28201) | INE | Validación del salario |
| 7 | EPA por edad (t=65334) | INE | Narrativa (paro juvenil) |
| 8 | Padrón continuo (población 18–34) | INE | Complementaria — impacto humano |

El alquiler procede del **SERPAVI** (precios reales declarados, no de oferta) y el salario joven de la **AEAT a escala provincial**; ambas comparten naturaleza fiscal. El universo son las 48 unidades de régimen común (46 provincias más las ciudades autónomas de Ceuta y Melilla); se excluyen los territorios forales, que las fuentes tributarias no cubren de forma homogénea, sin imputar.

## Panel resultante

- **Panel principal:** 672 observaciones × 30 variables (48 provincias × 14 años, 2011–2024).
- **Panel por edad:** 2.016 observaciones (48 × 14 × 3 bandas de edad), para el gradiente.
- **Panel de población joven:** 576 observaciones, para la dimensión del impacto.

## Entorno y reproducibilidad

Todo el tratamiento se desarrolla en **Python** sobre **Google Colab**, con los datos en Google Drive y control de versiones en este repositorio. Las librerías principales son pandas, numpy, pypdf (lectura de los PDF de la AEAT), python-calamine (.xls), matplotlib y seaborn (visualización) y statsmodels y scipy (contrastes del análisis exploratorio). El proceso sigue el esquema ETL (extracción, transformación y carga) y se documenta paso a paso en el cuaderno y en [`docs/decision_log.md`](docs/decision_log.md).
