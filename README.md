# Proyecto FIFA World Cup 2022 - MCDI500

Repositorio del proyecto académico desarrollado para la asignatura **MCDI500 – Herramientas de Software Científico**, orientado al análisis reproducible del conjunto de datos del Mundial FIFA Qatar 2022 mediante herramientas de Ciencia de Datos y trabajo colaborativo.

---

## Descripción del Proyecto

El proyecto busca analizar las estadísticas del Mundial FIFA Qatar 2022 para identificar variables y patrones asociados al desempeño de las selecciones participantes.

Se utilizan herramientas del ecosistema científico de Python y buenas prácticas de desarrollo colaborativo, asegurando trazabilidad, documentación y reproducibilidad.

---

## Pregunta de Investigación

**¿Qué estadísticas influyen en el desempeño y los resultados obtenidos por las selecciones participantes en la Copa Mundial FIFA Qatar 2022?**

---

## Objetivo General

Analizar los datos del Mundial FIFA Qatar 2022 mediante técnicas de exploración, limpieza, transformación y análisis algorítmico, generando una base reproducible para comprender el desempeño de las selecciones participantes.

---

## Objetivos Específicos

* Obtener y validar el conjunto de datos.
* Explorar la estructura y calidad de las variables.
* Identificar y tratar valores faltantes e inconsistencias.
* Transformar los datos para facilitar su análisis.
* Implementar algoritmos estructurados y recursivos.
* Comparar distintas estrategias mediante mediciones de complejidad.
* Documentar las decisiones técnicas realizadas.
* Mantener un entorno reproducible y colaborativo utilizando Git y GitHub.

---

## Dataset Utilizado

**Fuente:** FIFA World Cup 2022 Complete Dataset

* Autor: Diego Orige
* Plataforma: Kaggle

https://www.kaggle.com/datasets/die9origephit/fifa-world-cup-2022-complete-dataset

---

## Metodología

El proyecto sigue una adaptación de la metodología **CRISP-DM**:

1. Comprensión del problema.
2. Obtención de los datos.
3. Exploración y comprensión del dataset.
4. Limpieza y transformación de datos.
5. Análisis y visualización.
6. Diseño de algoritmos y evaluación de complejidad.
7. Interpretación de resultados.

---

## Fases del Proyecto

### Fase 1

* Definición del problema.
* Organización del entorno reproducible.
* Diseño del repositorio y documentación inicial.

### Fase 2

* Obtención y validación de los datos.
* Limpieza y transformación del dataset.
* Construcción del pipeline de preprocesamiento.

### Fase 3

* Implementación de algoritmos estructurados y recursivos.
* Comparación entre enfoques iterativos y vectorizados.
* Medición de complejidad temporal mediante `timeit`.
* Modularización del código y documentación técnica.

---

## Estructura del Repositorio

```text
fifa-worldcup-2022-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   ├── F1_Definicion.ipynb
│   ├── F2_Definicion.ipynb
│   ├── F3_Definicion.ipynb
│   └── otros.ipynb
│
├── results/
│   ├── figures/
│   │   └── .gitkeep
│   └── reports/
│       └── .gitkeep
│
├── src/
│   ├── funciones_reutilizables.py
│   └── funciones_f3_algoritmos.py
│
├── requirements.txt
├── .gitignore
├── .mailmap
└── README.md

---

## Algoritmos Implementados

Durante la Fase 3 se desarrollaron distintas estrategias para analizar estadísticas del torneo:

* Suma iterativa.
* Suma recursiva.
* Merge Sort recursivo.
* Ordenamiento utilizando `sorted()`.
* Operaciones vectorizadas con Pandas.

Las mediciones de complejidad temporal fueron realizadas utilizando la biblioteca estándar `timeit`.

---

## Arquitectura del Código

La solución se encuentra organizada mediante módulos independientes.

| Componente                 | Responsabilidad                       |
| -------------------------- | ------------------------------------- |
| F2_Definicion.ipynb        | Pipeline de datos                     |
| F3_Definicion.ipynb        | Análisis algorítmico                  |
| funciones_reutilizables.py | Funciones reutilizables               |
| funciones_f3_algoritmos.py | Algoritmos estructurados y recursivos |
| data/raw                   | Datos originales                      |
| data/processed             | Datos procesados                      |
| results/figures            | Figuras                               |
| results/reports            | Reportes                              |

---

## Estrategia de Trabajo Colaborativo

El desarrollo se realiza utilizando GitHub y ramas por funcionalidad.

### Ramas utilizadas

* `main`
* `feature-data`
* `feature-analysis`
* `feature-documentation`
* `feature-visualization`
* `feature-f3-algorithms`
* `feature-f3-docs`
* `feature-f3-newnotebook`

La integración se realiza mediante Pull Requests y revisión colaborativa.

---

## Convención de Commits

Se emplea la especificación **Conventional Commits**:

* `feat`: nuevas funcionalidades.
* `docs`: documentación.
* `fix`: correcciones.
* `refactor`: mejoras internas.
* `chore`: mantenimiento.

Ejemplos:

```text
feat(f3): implementa estructuras y algoritmos recursivos

feat(f3): agrega nueva sección notebook F3_Definicion

docs(f3): actualiza documentación técnica

fix: corrige estructura del repositorio
```

---

## Herramientas Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* Git
* GitHub

---

## Reproducibilidad

### 1. Clonar el repositorio

```bash
git clone https://github.com/sauriomac/fifa-worldcup-2022-analysis.git
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar los notebooks

Los notebooks principales se encuentran en:

```text
notebooks/F1_Definicion.ipynb
notebooks/F2_Definicion.ipynb
notebooks/F3_Definicion.ipynb
```

Se recomienda ejecutar:

**Kernel → Restart & Run All**

para verificar la reproducibilidad completa del proyecto.

---

## Integrantes

* Luis Rodrigo Espinoza
* Claudio Alarcón
* Enzo Pinilla

---

## Estado del Proyecto

Proyecto académico correspondiente al **Magíster en Ciencia de Datos e Inteligencia Artificial**, actualmente en desarrollo dentro de la asignatura **MCDI500 – Herramientas de Software Científico**.
