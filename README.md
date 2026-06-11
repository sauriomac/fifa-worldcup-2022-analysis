# proyecto-fifa-mcdi500

Repositorio para el análisis del Mundial FIFA Qatar 2022 con enfoque en organización, trazabilidad, reproducibilidad y trabajo colaborativo utilizando herramientas de Ciencia de Datos.

## Descripción del Proyecto

Este proyecto tiene como propósito analizar los datos del Mundial FIFA Qatar 2022 mediante técnicas de exploración, limpieza, transformación y visualización de datos.

El análisis busca identificar patrones relevantes relacionados con el rendimiento de las selecciones participantes, resultados de los encuentros, distribución de goles y comportamiento general del torneo.

## Objetivo General

Analizar los datos del Mundial FIFA 2022 para obtener información descriptiva y generar visualizaciones que permitan comprender el desempeño de los equipos durante la competencia.

## Objetivos Específicos

* Explorar la estructura y calidad de los datos.
* Identificar y corregir valores faltantes o inconsistencias.
* Realizar análisis exploratorio de datos (EDA).
* Generar estadísticas descriptivas relevantes.
* Construir visualizaciones para apoyar la interpretación de resultados.
* Documentar el proceso para asegurar la reproducibilidad del proyecto.

## Dataset Utilizado

Fuente de datos: FIFA World Cup 2022 Dataset.

Información considerada para el análisis:

* Equipos participantes.
* Resultados de los partidos.
* Goles anotados.
* Fechas de los encuentros.
* Fases del torneo.
* Estadísticas generales de desempeño.

## Metodología de Trabajo

El proyecto sigue las siguientes etapas:

### 1. Comprensión del problema

Definición de objetivos y preguntas de análisis.

### 2. Exploración de Datos (EDA)

* Revisión de variables.
* Tipos de datos.
* Estadísticas descriptivas.
* Identificación de anomalías.

### 3. Limpieza de Datos

* Tratamiento de valores nulos.
* Corrección de inconsistencias.
* Homologación de formatos.

### 4. Transformación de Datos

* Preparación de variables.
* Generación de atributos derivados cuando corresponda.

### 5. Visualización

* Distribución de goles.
* Comparación de selecciones.
* Resultados por fase del torneo.
* Análisis descriptivo general.

### 6. Interpretación de Resultados

Obtención de conclusiones y hallazgos relevantes.

## Estructura del Proyecto

```text
proyecto-fifa-mcdi500/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_limpieza.ipynb
│   └── 03_analisis.ipynb
├── docs/
│   ├── referencias.md
│   └── notas_proyecto.md
├── results/
│   ├── figures/
│   └── reports/
├── src/
│   └── funciones_reutilizables.py
├── requirements.txt
├── .gitignore
└── README.md

## Primeros Commits Proyectados

* docs: agrega README inicial del proyecto
* data: incorpora dataset FIFA World Cup 2022
* feat: crea notebook de análisis exploratorio
* docs: agrega documentación inicial del proyecto
* feat: incorpora visualizaciones preliminares
* fix: corrige nombres y formatos de variables
* refactor: reorganiza estructura del repositorio

## Estrategia de Ramas

La rama principal es **main** y cada integrante trabaja en ramas por funcionalidad:

* feature-data
* feature-analysis
* feature-documentation
* feature-visualization

La integración se realiza mediante Pull Requests revisados por el equipo antes de realizar merge a la rama principal.

## Convención de Commits

Se utiliza Conventional Commits para mantener un historial claro y consistente:

* feat: nueva funcionalidad
* docs: cambios de documentación
* fix: correcciones de errores
* refactor: mejoras internas sin cambiar funcionalidad
* chore: tareas de mantenimiento

## Herramientas Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git
* GitHub

## Entorno de Trabajo

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar dependencias desde requirements.txt.
4. Ejecutar los notebooks ubicados en la carpeta notebooks/.
5. Generar resultados y visualizaciones en la carpeta results/.

## Integrantes

* Rodrigo Espinoza
* Claudio Alarcón
* Enzo Pinilla

## Estado del Proyecto

Proyecto académico en desarrollo para la asignatura de Ciencia de Datos.
