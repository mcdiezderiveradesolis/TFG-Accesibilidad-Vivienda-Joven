# Source inventory

## Objetivo de este documento

Este archivo resume las fuentes de datos del proyecto, su papel dentro del pipeline, su estado actual y las salidas esperadas.

---

## Fuente 1. Salarios

- **Fuente**: INE – Encuesta de Estructura Salarial
- **Tabla**: 28201
- **Variable principal**: salario medio anual por trabajador
- **Cobertura observada**: 2010–2023
- **Extensión estimada**: 2024–2025
- **Nivel territorial**: España + CCAA
- **Desagregación actual**:
  - sexo
  - grupo de edad
- **Tipo de fuente**: oficial
- **Estado**: completada

### Salidas generadas
- `data/clean/salary_observed.csv`
- `data/clean/salary_completed.csv`
- `data/clean/salary_final.csv`

### Observaciones metodológicas
- La fuente original llega en estructura jerárquica orientada a lectura.
- Se transforma a formato largo.
- Se tratan valores faltantes y marcas de baja robustez muestral.
- Se generan estimaciones auxiliares para 2024 y 2025.

---

## Fuente 2. Alquiler

- **Fuente**: Idealista – Informes del precio del alquiler
- **Variable principal**: precio medio del alquiler (€/m²)
- **Cobertura objetivo**: 2010–2025
- **Nivel territorial objetivo**: España + CCAA
- **Tipo de fuente**: privada / repositorio consolidado
- **Estado**: pendiente de limpieza

### Salida esperada
- `data/clean/rent_observed.csv`
- `data/clean/rent_final.csv`

### Observaciones metodológicas
- Se trabajará con España y las 17 CCAA.
- Ceuta y Melilla quedarán fuera del panel principal.
- La variable derivada posterior será el alquiler mensual estimado a partir de una superficie estándar de 60 m².

---

## Fuente 3. Paro

- **Fuente**: INE – Tasas de paro por distintos grupos de edad, sexo y comunidad autónoma
- **Variable principal**: tasa de paro
- **Cobertura objetivo**: 2010–2025
- **Nivel territorial objetivo**: CCAA
- **Desagregación esperada**:
  - sexo
  - grupo de edad
- **Tipo de fuente**: oficial
- **Estado**: pendiente de limpieza

### Salida esperada
- `data/clean/unemployment_final.csv`

### Observaciones metodológicas
- La fuente se limpiará por separado antes de la integración.
- Se anualizará o resumirá respetando la coherencia temporal del panel final.

---

## Fuente 4. Población

- **Fuente**: INE – Población residente por fecha, sexo, grupo de edad y nacionalidad
- **Variables principales previstas**:
  - población total
  - población joven
- **Cobertura objetivo**: 2010–2025
- **Nivel territorial objetivo**: España + CCAA
- **Tipo de fuente**: oficial
- **Estado**: pendiente de limpieza

### Salida esperada
- `data/clean/population_final.csv`

### Observaciones metodológicas
- Se incorporará como bloque contextual del panel.
- Permitirá medir tamaño y composición demográfica de cada territorio.

---

## Fuente auxiliar. Emancipación

- **Fuente**: INJUVE / CJE
- **Variable principal**: tasa de emancipación juvenil
- **Papel en el proyecto**: fuente auxiliar de contraste e interpretación
- **Tipo de fuente**: institucional
- **Estado**: pendiente

### Observaciones metodológicas
- No forma parte del dataset maestro inicial.
- Se utilizará como apoyo contextual y de validación externa del análisis.

---

## Estado actual del inventario

### Completado
- salarios

### Pendiente
- alquiler
- paro
- población
- emancipación auxiliar
