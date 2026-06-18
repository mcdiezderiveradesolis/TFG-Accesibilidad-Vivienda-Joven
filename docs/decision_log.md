# Decision log

## Objetivo de este documento

Registro cronológico de las decisiones metodológicas y técnicas del TFG. Documenta no solo el estado final, sino también la **evolución del proyecto**: qué se planteó al inicio, qué se revisó y cuál es la versión vigente. Sirve de trazabilidad y de apoyo a la redacción de la memoria.

> Este documento se ha actualizado para reflejar el diseño **definitivo** del trabajo (panel provincial, SERPAVI y AEAT como fuentes núcleo, 2011–2024). Las decisiones de la primera fase del repositorio (escala autonómica, alquiler de Idealista, salario de la EES como fuente principal) se conservan más abajo marcadas como **revisadas/sustituidas**, porque forman parte de la evolución del trabajo.

---

## 1. Decisiones estructurales vigentes

### Entorno de trabajo
- Desarrollo en **Python** sobre **Google Colab**; datos en Google Drive; control de versiones en GitHub.
- Excel se usa solo para inspección visual y auditoría puntual, no como entorno del pipeline.

### Unidad y horizonte de análisis (VIGENTE)
- Nivel territorial: **provincial**, 48 provincias de régimen fiscal común (46 provincias + Ceuta y Melilla).
- Se **excluyen los cuatro territorios forales** (País Vasco y Navarra), porque las fuentes tributarias no los recogen bajo la misma estadística. No se imputan.
- Horizonte: **2011–2024**, con proyección de escenario 2025–2027 en el pilar de Análisis.
- Frecuencia: **anual**.

### Estructura lógica del proyecto
- `data/raw`: fuentes originales sin modificar
- `data/clean`: salidas limpias e integradas del pipeline
- `notebooks`: cuadernos de Google Colab
- `figuras`: figuras de la memoria
- `docs`: documentación metodológica

### Fuentes del panel (VIGENTE)
Siete fuentes oficiales + una complementaria (ver `source_inventory.md`):
- Alquiler: **SERPAVI** (precio mediano real declarado, no de oferta).
- Salario joven provincial: **AEAT, Modelo 190** (42 PDF parseados).
- Paro: **EPA provincial**. Deflactor: **IPC**. Contexto: **SMI**.
- Validación del salario: **EAES**. Narrativa de paro juvenil: **EPA por edad**.
- Complementaria de impacto: **Padrón continuo** (población 18–34 por provincia).

---

## 2. Historial cronológico de decisiones

### [Punto de partida] El anteproyecto y su revisión
- **Situación inicial:** el trabajo arrancó con un anteproyecto que fijó el tema —el desequilibrio entre el precio del alquiler y el salario de la población joven— y un primer marco teórico, con una aproximación a **escala autonómica**, el alquiler tomado de portales inmobiliarios y el salario de la Encuesta de Estructura Salarial.
- **Aprendizaje:** esa primera aproximación coincidía con el nivel del seguimiento institucional ya existente y se apoyaba en precios de oferta y supuestos frágiles, de modo que no aportaba resolución nueva ni una base reproducible.
- **Decisión:** rediseñar el trabajo hacia un enfoque **provincial, explicativo y predictivo**, con fuentes oficiales de naturaleza fiscal y un pipeline reproducible. Las decisiones siguientes detallan ese rediseño.
- **Estado:** Vigente.

### [Rediseño] De una base en Excel a un pipeline en Python — VIGENTE
- **Situación inicial:** base previa construida principalmente en Excel.
- **Problema:** dependía en exceso de fórmulas en hojas, con escasa trazabilidad y riesgo de errores de arrastre (se detectó, por ejemplo, una fórmula de esfuerzo arrastrada con una referencia absoluta de alquiler).
- **Decisión:** reconstruir el pipeline desde cero en Python/Colab, conservando solo la lógica metodológica útil.
- **Justificación:** flujo reproducible, validado y defendible, alineado con Ingeniería del Dato.
- **Estado:** Vigente.

### [Escala territorial] De comunidad autónoma a provincia — SUSTITUYE a la decisión inicial
- **Situación inicial:** el primer diseño trabajaba a escala de comunidad autónoma.
- **Problema:** la resolución autonómica oculta la fuerte heterogeneidad territorial del alquiler y coincide con el nivel del seguimiento institucional existente (CJE, INJUVE, Eurostat); no aporta resolución nueva.
- **Decisión:** trabajar a **escala provincial** (48 provincias de régimen común).
- **Justificación:** es la aportación diferencial del trabajo y exige fuentes con desagregación provincial.
- **Estado:** Vigente. *(Revisa la decisión inicial de nivel autonómico.)*

### [Fuente de alquiler] De Idealista al SERPAVI — SUSTITUYE a "Idealista como fuente principal"
- **Situación inicial:** el anteproyecto y la base previa usaban informes de Idealista (precio €/m² × 60 m²).
- **Problema:** los portales difunden **precios de oferta**, que introducen un sesgo al alza, y la estimación por 60 m² es un supuesto frágil.
- **Decisión:** usar el **SERPAVI** (Sistema Estatal de Referencia del Precio del Alquiler), única fuente oficial de precios reales de alquiler con desagregación provincial, basada en declaraciones del IRPF.
- **Justificación:** recoge contratos reales firmados y declarados, coherente con la naturaleza fiscal del salario de la AEAT.
- **Estado:** Vigente. *(Revisa la decisión inicial de mantener Idealista y los 60 m².)*

### [Fuente de salario] La AEAT como fuente principal; la EES pasa a validación — SUSTITUYE a "EES como fuente principal"
- **Situación inicial:** el primer diseño usaba la Encuesta de Estructura Salarial (EES, t=28201) del INE como fuente salarial principal.
- **Problema:** la EES solo llega a nivel autonómico, incompatible con el panel provincial.
- **Decisión:** usar el salario provincial por edad de la **AEAT (Modelo 190)** como fuente núcleo y reservar la **EES** para validar externamente nivel y tendencia.
- **Justificación:** la AEAT es la única fuente con salario joven a escala provincial; la EES aporta un contraste independiente.
- **Estado:** Vigente. *(Revisa la decisión inicial sobre la fuente salarial.)*

### [Conversión del salario] De bruto a neto — VIGENTE
- **Decisión:** convertir el salario bruto de la AEAT a **neto** (cotización del 6,35 % + IRPF con escala general y mínimo personal), porque la tasa de esfuerzo se define sobre renta disponible.
- **Estado:** Vigente.

### [Cobertura territorial] Inclusión de Ceuta y Melilla, exclusión de forales — SUSTITUYE a "excluir Ceuta y Melilla"
- **Situación inicial:** el primer diseño excluía Ceuta y Melilla.
- **Decisión vigente:** **incluir** Ceuta y Melilla (forman parte del territorio fiscal común) y **excluir** los territorios forales, no cubiertos homogéneamente por las fuentes tributarias.
- **Estado:** Vigente. *(Revisa la decisión inicial sobre Ceuta y Melilla.)*

### [Tratamiento de nulos] Exclusión documentada, sin imputación — VIGENTE
- **Decisión:** los valores ausentes por territorios fuera del universo (forales) no se imputan, se excluyen y se documentan; la interpolación solo procedería ante huecos internos de una serie homogénea.
- **Estado:** Vigente.

### [Fuente complementaria] Padrón continuo para el impacto — VIGENTE
- **Decisión:** añadir la población joven (18–34) por provincia del **Padrón continuo** como octava fuente complementaria, validada desde el control inicial pero **fuera del panel de modelado**; solo traduce la tasa de esfuerzo en magnitud humana.
- **Estado:** Vigente.

### [Variables descartadas] IPVA y subcomponentes del IPC del alquiler — VIGENTE
- **Decisión:** descartar las tablas IPVA del INE (índice de precios de la vivienda en alquiler) y el subcomponente de alquiler del IPC como predictores, por **riesgo de circularidad** con la variable dependiente.
- **Estado:** Vigente.

### [Modelado supervisado] Competición de modelos: el dato elige el método — VIGENTE
- **Decisión:** comparar un modelo base regularizado (**Ridge**) con dos avanzados de árboles (**Random Forest** y **Gradient Boosting**) bajo validación temporal; **gana Ridge** por su mejor ajuste fuera de muestra.
- **Justificación:** en un panel pequeño y con tendencia, el modelo lineal regularizado generaliza mejor que los de árboles, que quedan limitados por el techo de extrapolación. El dato gobierna la elección del método, no al revés.
- **Estado:** Vigente.

### [Inferencia] Efectos fijos provinciales y diagnóstico de colinealidad — VIGENTE
- **Decisión:** complementar la predicción con un modelo de **efectos fijos provinciales (LSDV)** con errores estándar clusterizados por provincia, y diagnosticar la **colinealidad** (matriz de correlación y factor de inflación de la varianza).
- **Justificación:** separa la heterogeneidad estructural de cada territorio de la dinámica temporal y obliga a leer las variables salariales en bloque, no una a una.
- **Estado:** Vigente.

### [No supervisado] Tipologías provinciales con K-Means (k = 3) — VIGENTE
- **Decisión:** agrupar las 48 provincias por **nivel y tendencia** de la tasa de esfuerzo con **K-Means**, eligiendo **k = 3** por interpretabilidad (silueta casi idéntica a k = 2 pero lectura más rica) y validando la partición con un agrupamiento jerárquico independiente.
- **Estado:** Vigente.

### [Series temporales] Proyección como escenario, no como predicción — VIGENTE / SUSTITUYE al SARIMAX mensual
- **Decisión:** proyectar la tasa de esfuerzo 2025–2027 con **ARIMA** sobre la serie diferenciada, presentada con intervalos y **como escenario**, no como predicción puntual, dada la brevedad de la serie (catorce observaciones anuales).
- **Justificación:** al ser un dato anual no procede un componente estacional, por lo que se descarta el SARIMAX mensual de los ejemplos; también se descarta un estimador dinámico de panel (Arellano-Bond) por el tamaño reducido del panel.
- **Estado:** Vigente.

### [Análisis de Negocio] Interpretar, no re-explicar; matriz de decisión — VIGENTE
- **Decisión:** el pilar de negocio **traduce** los resultados del Análisis del Dato en decisiones de consultoría y política pública **sin reabrir la técnica**. Su aportación diferencial es una **matriz provincial** que distingue la **tensión estructural** (esfuerzo explicado por los fundamentales) de la **tensión residual** (precio por encima de los fundamentales, planteada como hipótesis), cada una con su palanca, y unas recomendaciones **tipificadas** (inmediata, estratégica, técnica y futura).
- **Justificación:** responde a la modalidad de consultoría del TFG; se descarta de forma consciente un plan de negocio o lienzo de modelo, que no corresponde a este pilar.
- **Estado:** Vigente.

---

## 3. Estado actual del proyecto

### Completado
- Rediseño del pipeline y migración a Python/Colab.
- **Pilar de Ingeniería del Dato:** panel principal 672×30, paneles auxiliares (2.016 y 576), auditoría final, memoria de la entrega. 
- **Pilar de Análisis del Dato:** competición supervisada (Ridge vs Random Forest y Gradient Boosting, gana Ridge), inferencia por efectos fijos provinciales (LSDV), tipologías con K-Means (k = 3) y escenario 2025–2027 con ARIMA; memoria de la entrega. 
- **Pilar de Análisis de Negocio:** interpretación de los resultados en clave de negocio y de política pública, con conclusiones y recomendaciones tipificadas; memoria de la entrega. 
> Memoria completa (≈ 50 páginas) que integra los tres pilares.
