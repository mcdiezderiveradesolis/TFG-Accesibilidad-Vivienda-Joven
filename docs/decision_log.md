# Decision log

## Objetivo de este documento

Este archivo recoge de forma cronológica las decisiones metodológicas y técnicas adoptadas durante la construcción del dataset del TFG. Su finalidad es mantener trazabilidad, justificar cambios de criterio, documentar revisiones metodológicas y facilitar la redacción posterior de la memoria.

El documento no refleja solo el estado actual del proyecto, sino también la evolución del proceso: qué se planteó inicialmente, qué limitaciones se detectaron, qué decisiones fueron revisadas y cuál es la versión vigente en cada caso.

---

## 1. Decisiones estructurales del proyecto

### Entorno de trabajo
- El trabajo se desarrolla en Python.
- El entorno principal de trabajo es Google Colab.
- Los archivos de trabajo se guardan en Google Drive.
- GitHub se utiliza como repositorio del proyecto y control de versiones.
- Excel se utiliza únicamente para inspección visual, contraste puntual y auditoría del trabajo previo, no como entorno principal del pipeline actual.

### Estructura lógica del proyecto
- `data/raw`: fuentes originales sin modificar
- `data/clean`: datasets limpios por fuente
- `data/processed`: datasets integrados y derivados
- `notebooks`: notebooks de Google Colab
- `outputs`: tablas, controles y gráficos
- `docs`: documentación metodológica

### Alcance actual de la base principal
La base principal se construirá con:
- salarios
- alquiler
- paro
- población total
- población joven

### Fuente auxiliar
- emancipación juvenil

### Frecuencia y unidad de análisis
- La frecuencia objetivo del panel principal será anual.
- El nivel territorial principal será comunidad autónoma.
- Se conservará también España para comparaciones descriptivas.

---

## 2. Historial cronológico de decisiones

## [Inicio del rediseño] Replanteamiento completo de la base de datos

- **Situación inicial**:
  El trabajo contaba con una base previa construida principalmente en Excel, con una lógica razonable de descarga, limpieza, integración y cálculo de indicadores.

- **Problema detectado**:
  Aunque la base previa ya mostraba una estructura por fases, resultaba demasiado pequeña, dependía en exceso de transformaciones dentro de Excel y no garantizaba un nivel suficiente de trazabilidad, reproducibilidad y validación para una entrega de matrícula.

- **Alternativas consideradas**:
  1. Mantener el Excel previo como base principal y hacer ajustes menores.
  2. Reconstruir el pipeline desde cero en Python, conservando únicamente la lógica metodológica útil del trabajo previo.

- **Decisión final**:
  Reconstruir el pipeline desde cero en Python/Google Colab.

- **Justificación**:
  Esta opción permite un flujo más profesional, replicable y alineado con las exigencias de Ingeniería del Dato.

- **Impacto en el proyecto**:
  Se pasa de un flujo centrado en Excel a un pipeline programático por fuente.

- **Archivos afectados**:
  diseño general del proyecto, repositorio y futuros notebooks

- **Estado**:
  Vigente

---

## [Diseño metodológico] Python como entorno principal y Excel como apoyo

- **Situación inicial**:
  El trabajo previo estaba desarrollado principalmente en un workbook con varias hojas de proceso.

- **Problema detectado**:
  El uso de Excel como herramienta principal dificultaba la trazabilidad del pipeline y podía introducir errores de arrastre en fórmulas o cambios manuales difíciles de documentar.

- **Alternativas consideradas**:
  1. Mantener Excel como herramienta principal.
  2. Utilizar Excel solo como herramienta de inspección y Python como entorno principal de trabajo.

- **Decisión final**:
  Usar Python/Google Colab como entorno principal y Excel solo para revisar y auditar el trabajo previo.

- **Justificación**:
  Permite un proceso reproducible, más sólido y mejor defendible metodológicamente.

- **Impacto en el proyecto**:
  Todo el proceso de limpieza y transformación se documenta en notebooks y salidas diferenciadas.

- **Archivos afectados**:
  `notebooks/`, `data/clean/`, `data/processed/`

- **Estado**:
  Vigente

---

## [Auditoría del workbook previo] Revisión del Excel inicial como punto de partida

- **Situación inicial**:
  Se revisó el workbook previo del proyecto para entender su lógica interna antes de sustituirlo por el pipeline actual.

- **Problema detectado**:
  Antes de rediseñar el trabajo era necesario distinguir qué partes del Excel previo tenían valor metodológico y qué partes debían mejorarse o abandonarse.

- **Alternativas consideradas**:
  1. Ignorar el workbook previo y empezar sin revisarlo.
  2. Auditarlo hoja por hoja para conservar su lógica útil y detectar limitaciones.

- **Decisión final**:
  Analizar el workbook anterior en profundidad.

- **Justificación**:
  El workbook previo sí mostraba una intención metodológica válida y útil para el rediseño.

- **Impacto en el proyecto**:
  Se conserva la lógica conceptual del proceso, pero se reimplementa en un pipeline más robusto.

- **Archivos afectados**:
  diseño metodológico general

- **Estado**:
  Vigente

---

## [Auditoría del workbook previo] Fortalezas detectadas en la base inicial

- **Situación inicial**:
  El Excel previo estaba estructurado en distintas hojas de trabajo.

- **Problema detectado**:
  Era necesario evaluar si existía ya un embrión de pipeline aprovechable.

- **Alternativas consideradas**:
  1. Considerar que el Excel era únicamente una maqueta pobre.
  2. Reconocer y conservar las decisiones útiles que ya estaban bien encaminadas.

- **Decisión final**:
  Conservar la lógica metodológica útil del workbook anterior.

- **Justificación**:
  El Excel previo ya separaba el proceso en hojas de:
  - descarga de salarios
  - limpieza de salarios
  - dataset salarial derivado
  - descarga de alquiler
  - limpieza de alquiler
  - dataset de alquiler derivado
  - integración intermedia
  - dataset final

  Además, contenía notas útiles sobre:
  - fuente salarial INE
  - alquiler de Idealista
  - uso de 60 m²
  - exclusión de Ceuta y Melilla
  - imputación salarial
  - estimaciones 2024–2025

- **Impacto en el proyecto**:
  La lógica del pipeline anterior se reutiliza como referencia conceptual, pero no como solución final.

- **Archivos afectados**:
  estructura metodológica general

- **Estado**:
  Vigente

---

## [Auditoría del workbook previo] Limitaciones detectadas en la base inicial

- **Situación inicial**:
  El workbook previo ya integraba salario, alquiler y esfuerzo salarial.

- **Problema detectado**:
  Se observaron varias debilidades metodológicas:
  - reducción demasiado temprana de la fuente salarial
  - mezcla de dato observado, imputado y estimado
  - dependencia de fórmulas en hojas Excel
  - escasa separación entre bruto, limpio, completado y final
  - vulnerabilidad a errores de arrastre

- **Alternativas consideradas**:
  1. Mantener el mismo diseño y corregir solo errores puntuales.
  2. Rediseñar el flujo con salidas diferenciadas y validación explícita.

- **Decisión final**:
  Rediseñar el flujo actual con salidas diferenciadas y validación explícita.

- **Justificación**:
  El nuevo diseño mejora mucho la trazabilidad y reduce el riesgo de errores silenciosos.

- **Impacto en el proyecto**:
  Se establecen salidas separadas por fuente y por fase del tratamiento.

- **Archivos afectados**:
  diseño actual del pipeline

- **Estado**:
  Vigente

---

## [Auditoría del workbook previo] Error detectado en la fórmula del esfuerzo salarial 25–34

- **Situación inicial**:
  El workbook previo contenía una hoja final con indicadores de esfuerzo salarial.

- **Problema detectado**:
  En la columna del esfuerzo salarial 25–34 se detectó que la fórmula estaba arrastrada en gran parte de las filas utilizando una referencia absoluta de alquiler mensual, en lugar del valor de alquiler correspondiente a cada fila.

- **Alternativas consideradas**:
  1. Corregir únicamente esa fórmula dentro del Excel.
  2. Registrar este hallazgo como evidencia de la necesidad de pasar a un pipeline programático y validado.

- **Decisión final**:
  Registrar el error como una de las justificaciones del rediseño metodológico.

- **Justificación**:
  Este tipo de error es precisamente el que se quiere evitar con un pipeline reproducible, validado y documentado fuera de Excel.

- **Impacto en el proyecto**:
  Refuerza la decisión de reconstruir la base en Python y validar cada salida por separado.

- **Archivos afectados**:
  workbook previo y diseño actual del pipeline

- **Estado**:
  Vigente

---

## [Diseño de la base] Ampliación de variables principales

- **Situación inicial**:
  El trabajo previo estaba muy centrado en salarios y alquiler.

- **Problema detectado**:
  La base quedaba demasiado limitada para explicar con suficiente profundidad el fenómeno del esfuerzo salarial juvenil.

- **Alternativas consideradas**:
  1. Mantener salario y alquiler como núcleo único.
  2. Incorporar variables laborales y demográficas adicionales.

- **Decisión final**:
  Definir como base principal:
  - salarios
  - alquiler
  - paro
  - población total
  - población joven

- **Justificación**:
  Esto aumenta la potencia explicativa del panel sin perder coherencia.

- **Impacto en el proyecto**:
  La base final será más rica y más defendible en el análisis descriptivo y econométrico.

- **Archivos afectados**:
  diseño general del proyecto

- **Estado**:
  Vigente

---

## [Diseño de fuentes] Emancipación como fuente auxiliar

- **Situación inicial**:
  Se valoró integrar la emancipación juvenil dentro del panel principal.

- **Problema detectado**:
  Su estructura y lógica de uso no encajan tan limpiamente como salarios, alquiler, paro y población dentro del dataset maestro inicial.

- **Alternativas consideradas**:
  1. Integrarla desde el principio en la base principal.
  2. Tratarla como fuente auxiliar.

- **Decisión final**:
  Mantener la emancipación como fuente auxiliar.

- **Justificación**:
  Sigue siendo importante para el relato del TFG, pero su función será principalmente contextual y de contraste.

- **Impacto en el proyecto**:
  La base principal gana coherencia estructural.

- **Archivos afectados**:
  diseño general del proyecto

- **Estado**:
  Vigente

---

## [Cobertura territorial] Exclusión de Ceuta y Melilla del panel principal

- **Situación inicial**:
  Se valoró trabajar con todos los territorios disponibles.

- **Problema detectado**:
  La fuente de alquiler no ofrece una cobertura homogénea suficiente para Ceuta y Melilla, y en el propio planteamiento previo ya se recogía su exclusión por series incompletas.

- **Alternativas consideradas**:
  1. Mantenerlas con huecos.
  2. Imputarlas.
  3. Excluirlas del panel principal.

- **Decisión final**:
  Excluir Ceuta y Melilla del panel principal.

- **Justificación**:
  Se prioriza la homogeneidad territorial del panel.

- **Impacto en el proyecto**:
  El panel principal queda definido como España + 17 CCAA.

- **Archivos afectados**:
  diseño de alquiler e integración futura

- **Estado**:
  Vigente

---

## [Diseño inicial del salario] Reducción temprana a ambos sexos y dos grupos de edad

- **Situación inicial**:
  En la base previa en Excel, la fuente salarial se reducía al uso práctico de:
  - ambos sexos
  - menores de 25 años
  - grupo 25–34 años

- **Problema detectado**:
  Esta reducción simplificaba mucho el análisis, pero recortaba información útil de la fuente original y empobrecía el potencial del dataset.

- **Alternativas consideradas**:
  1. Mantener la reducción temprana desde el inicio del pipeline.
  2. Conservar más detalle de la fuente en las primeras fases y reducir solo cuando haga falta para análisis o integración.

- **Decisión final**:
  En el pipeline actual se conserva una estructura salarial más rica en la fase de limpieza.

- **Justificación**:
  Mantener más granularidad mejora la trazabilidad, el análisis descriptivo y la flexibilidad futura.

- **Impacto en el proyecto**:
  La fuente salarial actual se construye primero en formato más completo y después podrá agregarse según convenga.

- **Archivos afectados**:
  `01_clean_salary.ipynb` y outputs salariales

- **Estado**:
  Vigente

---

## [Diseño analítico] Conservación de la variable sexo

- **Situación inicial**:
  El workbook previo reducía el uso práctico de salarios a un único agregado por sexo.

- **Problema detectado**:
  Reducir la fuente a un único agregado desaprovechaba parte del valor analítico del INE.

- **Alternativas consideradas**:
  1. Trabajar solo con el agregado.
  2. Conservar la desagregación por sexo.

- **Decisión final**:
  Conservar la variable sexo en la base salarial.

- **Justificación**:
  Mejora el análisis descriptivo y la riqueza de la base sin cambiar el foco principal del TFG.

- **Impacto en el proyecto**:
  La fuente salarial actual conserva:
  - `Total`
  - `Mujeres`
  - `Hombres`

- **Archivos afectados**:
  `01_clean_salary.ipynb` y outputs salariales

- **Estado**:
  Vigente

---

## [Normalización - decisión revisada] Uso de `Ambos` en lugar de `Total`

- **Situación inicial**:
  Durante una fase intermedia del diseño del notebook se planteó utilizar `Ambos` como categoría agregada de la variable `sex`.

- **Problema detectado**:
  Al revisar la coherencia de la nomenclatura de salida, se observó que `Total` resultaba más estándar y más cómodo para documentación, diccionario de variables y tablas de validación.

- **Alternativas consideradas**:
  1. Mantener `Ambos`
  2. Sustituirlo por `Total`

- **Decisión final en esa fase**:
  Se utilizó temporalmente `Ambos`.

- **Justificación**:
  Se consideró inicialmente una etiqueta más natural para una variable de sexo.

- **Impacto en el proyecto**:
  La categoría agregada de sexo se definió provisionalmente como `Ambos`.

- **Archivos afectados**:
  fase intermedia de `01_clean_salary.ipynb`

- **Estado**:
  Revisada / sustituida

---

## [Normalización vigente] Uso de `Total` en la categoría agregada de sexo

- **Situación inicial**:
  Tras una versión intermedia en la que se utilizó `Ambos`, se revisó la nomenclatura final de la variable `sex` en los outputs salariales.

- **Problema detectado**:
  Era necesario fijar una única etiqueta final y consistente para la categoría agregada de sexo en todos los archivos de salida y en la documentación del proyecto.

- **Alternativas consideradas**:
  1. Mantener `Ambos`
  2. Utilizar `Total`

- **Decisión final**:
  Utilizar `Total` como categoría agregada de la variable `sex`.

- **Justificación**:
  `Total` funciona mejor como etiqueta técnica y documental en los datasets, el diccionario de variables y las tablas de validación. Además, facilita una nomenclatura más homogénea en los outputs.

- **Impacto en el proyecto**:
  La variable `sex` queda finalmente definida con las categorías:
  - `Total`
  - `Mujeres`
  - `Hombres`

- **Archivos afectados**:
  `01_clean_salary.ipynb`
  `data/clean/salary_observed.csv`
  `data/clean/salary_completed.csv`
  `data/clean/salary_final.csv`

- **Estado**:
  Vigente

---

## [Diseño del alquiler] Mantenimiento de Idealista como fuente principal

- **Situación inicial**:
  El workbook previo utilizaba informes de Idealista como base para los precios de alquiler.

- **Problema detectado**:
  Era necesario decidir si se mantenía esa fuente o si se sustituía por otra referencia distinta.

- **Alternativas consideradas**:
  1. Mantener Idealista como fuente principal del alquiler.
  2. Buscar una fuente alternativa completamente distinta.

- **Decisión final**:
  Mantener Idealista como fuente principal del alquiler.

- **Justificación**:
  La fuente ya estaba planteada en el anteproyecto, proporciona cobertura anual, es interpretable y encaja con el objetivo del trabajo.

- **Impacto en el proyecto**:
  El notebook de alquiler se construirá sobre informes anuales de Idealista.

- **Archivos afectados**:
  futuro `02_clean_rent.ipynb`

- **Estado**:
  Vigente

---

## [Diseño del alquiler] Mantenimiento de 60 m² como superficie estándar

- **Situación inicial**:
  El workbook previo y el anteproyecto ya trabajaban con una superficie estándar de 60 m² para estimar el gasto mensual de alquiler juvenil.

- **Problema detectado**:
  Era necesario decidir si se mantenía este supuesto o se reemplazaba por otro.

- **Alternativas consideradas**:
  1. Mantener 60 m².
  2. Cambiar la superficie estándar.
  3. Dejar la superficie como variable abierta.

- **Decisión final**:
  Mantener de momento 60 m² como criterio operativo de trabajo.

- **Justificación**:
  Es el supuesto ya utilizado en la base previa y está acompañado de una justificación documental en el planteamiento anterior. Esta decisión podrá refinarse si durante la memoria se considera necesario fortalecer aún más la fundamentación.

- **Impacto en el proyecto**:
  El alquiler mensual estimado se seguirá construyendo como:
  `precio €/m² × 60`

- **Archivos afectados**:
  diseño de alquiler, integración y futuros indicadores

- **Estado**:
  Vigente, pendiente de redacción final de la justificación documental

---

## [Fuente 1] Cierre de la versión observada de salarios

- **Situación inicial**:
  La fuente salarial del INE llegaba en una estructura jerárquica orientada a lectura.

- **Problema detectado**:
  No podía integrarse directamente ni analizarse como tabla.

- **Alternativas consideradas**:
  1. Simplificación manual en Excel.
  2. Reconstrucción programática a formato largo.

- **Decisión final**:
  Reconstruir la fuente en Python y generar una versión observada limpia.

- **Justificación**:
  Garantiza trazabilidad, reproducibilidad y validación.

- **Impacto en el proyecto**:
  Se genera `salary_observed.csv` con la estructura final de sexo:
  - `Total`
  - `Mujeres`
  - `Hombres`

- **Archivos afectados**:
  `notebooks/01_clean_salary.ipynb`
  `data/clean/salary_observed.csv`

- **Estado**:
  Vigente

---

## [Fuente 1] Tratamiento de valores especiales del INE

- **Situación inicial**:
  La fuente salarial del INE incluía:
  - `..` para datos no facilitados
  - valores negativos usados como marca de baja robustez muestral

- **Problema detectado**:
  Era necesario decidir cómo interpretar estos valores sin destruir información útil.

- **Alternativas consideradas**:
  1. Eliminar observaciones conflictivas.
  2. Tratar `..` como nulos y los negativos como valores absolutos con flag.

- **Decisión final**:
  - `..` se interpreta como faltante
  - los valores negativos se convierten a valor absoluto
  - se crean:
    - `salary_missing_flag`
    - `salary_low_sample_flag`

- **Justificación**:
  Permite mantener la mayor cantidad de información posible sin introducir interpretaciones erróneas.

- **Impacto en el proyecto**:
  Se conserva la lógica original de la fuente y se documenta mejor que en el workbook previo.

- **Archivos afectados**:
  `01_clean_salary.ipynb`
  `salary_observed.csv`

- **Estado**:
  Vigente

---

## [Fuente 1] Imputación de faltantes salariales

- **Situación inicial**:
  La fuente salarial observada presentaba huecos en determinadas combinaciones de territorio, edad y año.

- **Problema detectado**:
  Esos huecos dificultaban la continuidad temporal de la serie y la futura integración del panel.

- **Alternativas consideradas**:
  1. Eliminar observaciones con nulos.
  2. Imputar todo con una sola técnica.
  3. Aplicar un criterio mixto según el tipo de hueco.

- **Decisión final**:
  Aplicar:
  - interpolación lineal en huecos cortos
  - tasa de crecimiento nacional en huecos largos

- **Justificación**:
  Este criterio ya estaba recogido en el planteamiento metodológico previo y además es coherente con la lógica temporal de la serie.

- **Impacto en el proyecto**:
  Se genera `salary_completed.csv` y se añaden:
  - `salary_observed_flag`
  - `salary_imputed_flag`
  - `imputation_method`

- **Archivos afectados**:
  `01_clean_salary.ipynb`
  `data/clean/salary_completed.csv`

- **Estado**:
  Vigente

---

## [Diseño de outputs] Separación entre observado, completado y final

- **Situación inicial**:
  En la base previa en Excel el dato salarial observado, el imputado, el estimado y el mensualizado quedaban mucho más mezclados.

- **Problema detectado**:
  Esa mezcla hacía más difícil auditar el proceso y explicar con claridad qué parte del dato era observada y qué parte era estimada.

- **Alternativas consideradas**:
  1. Mantener una sola salida salarial.
  2. Separar las versiones del dato por fase del tratamiento.

- **Decisión final**:
  Separar la fuente salarial en tres salidas:
  - `salary_observed.csv`
  - `salary_completed.csv`
  - `salary_final.csv`

- **Justificación**:
  Aumenta muchísimo la trazabilidad y facilita la explicación metodológica en la memoria.

- **Impacto en el proyecto**:
  El pipeline actual distingue claramente entre observación, imputación y estimación final.

- **Archivos afectados**:
  `01_clean_salary.ipynb`
  `data/clean/salary_observed.csv`
  `data/clean/salary_completed.csv`
  `data/clean/salary_final.csv`

- **Estado**:
  Vigente

---

## [Normalización] Mantenimiento de la trazabilidad de fuente salarial

- **Situación inicial**:
  Era necesario definir una etiqueta técnica que identificara la procedencia exacta de la variable salarial.

- **Problema detectado**:
  Sin una variable de trazabilidad, la documentación futura y la integración entre fuentes sería menos clara.

- **Alternativas consideradas**:
  1. No incluir ningún identificador de fuente.
  2. Incluir una etiqueta técnica interna.

- **Decisión final**:
  Utilizar:
  - `salary_source = INE_EES_28201`

- **Justificación**:
  Facilita la trazabilidad y la documentación del pipeline.

- **Impacto en el proyecto**:
  La fuente salarial queda claramente identificada en todas sus salidas.

- **Archivos afectados**:
  `01_clean_salary.ipynb`
  outputs salariales

- **Estado**:
  Vigente

---

## [Revisión metodológica] Cambio en las tasas de estimación salarial para 2024 y 2025

- **Situación inicial**:
  En el workbook previo y en el anteproyecto se había planteado:
  - 2024 = +5%
  - 2025 = +3,5%

- **Problema detectado**:
  Durante el desarrollo del notebook se revisó que estas tasas no eran la opción más sólida para la variable salarial concreta que se estaba utilizando.

- **Alternativas consideradas**:
  1. Mantener +5% y +3,5%.
  2. Sustituirlas por proxies oficiales más consistentes.

- **Decisión final**:
  Revisar el criterio y usar:
  - 2024 = +3,8%
  - 2025 = +3,6%

- **Justificación**:
  Se consideró metodológicamente más sólido utilizar proxies oficiales del INE para extender la serie, dejando claro que 2024 y 2025 son estimaciones auxiliares y no observaciones directas de la misma operación estadística.

- **Impacto en el proyecto**:
  Cambia la construcción de `salary_final.csv` respecto al workbook previo y respecto al planteamiento inicial del anteproyecto.

- **Archivos afectados**:
  `01_clean_salary.ipynb`
  `data/clean/salary_final.csv`
  futura memoria metodológica

- **Estado**:
  Vigente

---

## [Fuente 1] Cierre de la fuente salarial final

- **Situación inicial**:
  Tras construir la versión observada y la versión completada, faltaba armonizar la serie con el horizonte temporal del TFG.

- **Problema detectado**:
  La serie observada terminaba en 2023 y el panel objetivo es 2010–2025.

- **Alternativas consideradas**:
  1. Detener la fuente en 2023.
  2. Extenderla con estimaciones documentadas para 2024 y 2025.

- **Decisión final**:
  Generar una versión final armonizada 2010–2025.

- **Justificación**:
  Facilita la futura integración con el resto de fuentes dentro del horizonte temporal del estudio.

- **Impacto en el proyecto**:
  Se genera `salary_final.csv`.

- **Archivos afectados**:
  `01_clean_salary.ipynb`
  `data/clean/salary_final.csv`

- **Estado**:
  Vigente

---

## [Diseño documental] GitHub como apoyo directo de la memoria

- **Situación inicial**:
  El repositorio podía limitarse a guardar archivos sueltos del proyecto.

- **Problema detectado**:
  Si GitHub no refleja el proceso metodológico real, luego la memoria escrita exige reconstruir decisiones y justificaciones desde cero.

- **Alternativas consideradas**:
  1. Usar GitHub solo como almacén de ficheros.
  2. Usarlo como evidencia ordenada del pipeline y del proceso metodológico.

- **Decisión final**:
  Usar GitHub como repositorio vivo y documentado del proceso.

- **Justificación**:
  Facilita la trazabilidad, el control de versiones y la redacción posterior de la memoria.

- **Impacto en el proyecto**:
  Se actualizan de forma coherente:
  - notebooks
  - datasets limpios
  - README
  - decision log
  - diccionario y documentación de fuentes

- **Archivos afectados**:
  estructura completa del repositorio

- **Estado**:
  Vigente

---

## 3. Estado actual del proyecto

### Completado
- auditoría del workbook previo
- rediseño del pipeline
- estructura del proyecto en GitHub
- documentación metodológica inicial
- fuente salarial observada
- fuente salarial completada
- fuente salarial final armonizada 2010–2025

### Pendiente inmediato
- limpieza y reconstrucción de la fuente de alquiler en `02_clean_rent.ipynb`

### Pendiente posterior
- limpieza de paro
- limpieza de población
- integración del panel principal
- feature engineering
- análisis del dato
