# Inventario de fuentes

Siete fuentes oficiales (cinco que forman el panel y dos reservadas para validación y narrativa) más una complementaria. Todas se validan al arranque del cuaderno (existencia del archivo) y se auditan en bruto (forma y valores no nulos).

| # | Fuente | Organismo | Referencia | Forma en bruto | Rol |
|---|---|---|---|---|---|
| 1 | SERPAVI — precio mediano del alquiler | Min. de Vivienda | Sistema Estatal de Referencia del Precio del Alquiler | 53 × 282 | Panel — variable dependiente |
| 2 | Mercado de Trabajo, Modelo 190 — salario por edad | AEAT | 42 PDF (3 bandas × 14 años) | 42 PDF → 2.016 obs. | Panel — denominador del KPI |
| 3 | EPA — tasa de paro provincial | INE | Tabla 65349 | 179 × 292 | Panel — control |
| 4 | IPC — índice general | INE | Tabla 76136 | 314 × 1.173 | Panel — deflactor nacional |
| 5 | Salario mínimo interprofesional | Min. de Trabajo | Serie histórica SMI | 61 × 10 | Panel — contexto |
| 6 | EAES — salario por edad y CC. AA. | INE | Tabla 28201 | 1.978 × 4 | Validación del salario |
| 7 | EPA — paro por edad y CC. AA. | INE | Tabla 65334 | 80 × 680 | Narrativa (paro juvenil) |
| 8 | Padrón continuo — población 18–34 | INE | Cifras de población por provincia | 21.691 × 76 | Complementaria de impacto humano |

## Fuentes inspeccionadas y descartadas

- **IPVA — índice de precios de la vivienda en alquiler** (INE, tablas 59058 / 59059): descartadas como predictor por riesgo de circularidad con la variable dependiente (son índices del propio alquiler). Se conservan en `data/raw/` como evidencia de la inspección.
- **Subcomponente de alquiler del IPC**: descartado por la misma razón.

## Universo y horizonte

48 provincias de régimen fiscal común (46 provincias + Ceuta y Melilla), 2011–2024. Se excluyen los territorios forales (País Vasco y Navarra), no cubiertos homogéneamente por las fuentes tributarias, sin imputación.
