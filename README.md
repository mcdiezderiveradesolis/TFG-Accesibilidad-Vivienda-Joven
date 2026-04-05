# TFG - Accesibilidad a la vivienda en alquiler entre la población joven en España

Repositorio de trabajo del TFG del Grado en Business Analytics (UFV).

## Objetivo
Construir una base de datos integrada, homogénea y reproducible para analizar el esfuerzo salarial juvenil en el acceso a la vivienda en alquiler en España por comunidad autónoma y año.

## Estado actual
- Estructura inicial del proyecto creada
- Documentación metodológica base creada
- Fuente salarial completada
- Notebook de salarios disponible en `notebooks/01_clean_salary.ipynb`
- Salidas limpias disponibles en:
  - `data/clean/salary_observed.csv`
  - `data/clean/salary_completed.csv`
  - `data/clean/salary_final.csv`

## Fuentes principales
- INE – Encuesta de Estructura Salarial (Tabla 28201)
- Idealista – Informes del precio del alquiler
- INE – Tasas de paro por edad, sexo y CCAA
- INE – Población residente
- INJUVE / CJE – Emancipación juvenil (fuente auxiliar)

## Estructura del proyecto
- `data/raw`: fuentes originales
- `data/clean`: datos limpios por fuente
- `data/processed`: base final integrada
- `notebooks`: notebooks de Google Colab
- `outputs`: tablas, controles y gráficos
- `docs`: documentación metodológica

## Progreso del pipeline
- [x] Salarios
- [ ] Alquiler
- [ ] Paro
- [ ] Población
- [ ] Integración del panel
- [ ] Feature engineering
- [ ] Análisis del dato
