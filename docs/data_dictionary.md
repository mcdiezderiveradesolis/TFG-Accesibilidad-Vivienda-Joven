# Data dictionary

## Objetivo de este documento

Este archivo documenta las variables de los datasets generados hasta el momento en el proyecto.

---

## Dataset: `salary_observed.csv`

### Descripción
Versión observada, limpia y estructurada de la fuente salarial del INE.

### Variables

- **`territory_name`**  
  Nombre normalizado del territorio.

- **`territory_type`**  
  Tipo de territorio. Valores esperados:
  - `España`
  - `CCAA`

- **`year`**  
  Año de referencia de la observación.

- **`sex`**  
  Categoría de sexo. Valores esperados:
  - `Total`
  - `Mujeres`
  - `Hombres`

- **`age_group`**  
  Grupo de edad normalizado. Valores esperados:
  - `all_ages`
  - `lt_25`
  - `25_34`
  - `35_44`
  - `45_54`
  - `55_plus`

- **`salary_annual_eur`**  
  Salario anual en euros.

- **`salary_missing_flag`**  
  Indicador de valor faltante.
  - `1` = dato faltante
  - `0` = dato disponible

- **`salary_low_sample_flag`**  
  Indicador de baja robustez muestral.
  - `1` = observación marcada por baja muestra
  - `0` = observación no marcada

- **`salary_source`**  
  Identificador técnico de la fuente. Valor actual:
  - `INE_EES_28201`

---

## Dataset: `salary_completed.csv`

### Descripción
Versión salarial completada tras el tratamiento de valores faltantes.

### Variables heredadas de `salary_observed.csv`
- `territory_name`
- `territory_type`
- `year`
- `sex`
- `age_group`
- `salary_annual_eur`
- `salary_missing_flag`
- `salary_low_sample_flag`
- `salary_source`

### Variables añadidas

- **`salary_observed_flag`**  
  Indicador de observación original.
  - `1` = dato observado originalmente
  - `0` = dato no observado originalmente

- **`salary_imputed_flag`**  
  Indicador de imputación.
  - `1` = dato imputado
  - `0` = dato no imputado

- **`imputation_method`**  
  Método utilizado para imputar la observación, cuando aplica. Valores esperados:
  - `linear_interpolation`
  - `national_growth_forward`
  - `national_growth_backward`
  - vacío / nulo si no hubo imputación

---

## Dataset: `salary_final.csv`

### Descripción
Versión salarial final armonizada para el periodo 2010–2025.

### Variables heredadas de `salary_completed.csv`
- `territory_name`
- `territory_type`
- `year`
- `sex`
- `age_group`
- `salary_annual_eur`
- `salary_missing_flag`
- `salary_low_sample_flag`
- `salary_source`
- `salary_observed_flag`
- `salary_imputed_flag`
- `imputation_method`

### Observaciones metodológicas
- Incluye estimaciones auxiliares para 2024 y 2025.
- Estas observaciones no proceden directamente de la fuente observada del INE, sino de una extensión documentada de la serie.

### Valores esperados adicionales en `imputation_method`
- `growth_estimation_2024_3_8pct`
- `growth_estimation_2025_3_6pct`

---

## Notas generales

- Los datasets salariales actuales constituyen la única fuente completada hasta el momento.
- La conversión de salario anual a salario mensual no forma parte aún de estos archivos; se realizará en una fase posterior de feature engineering.
- La integración con alquiler, paro y población se realizará más adelante en `data/processed/`.
