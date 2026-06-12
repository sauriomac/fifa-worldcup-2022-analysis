# Proyecto FIFA World Cup 2022 - MCDI500

Repositorio del proyecto académico desarrollado para la asignatura **MCDI500 – Herramientas de Software Científico**, orientado al análisis del conjunto de datos del Mundial FIFA Qatar 2022 mediante un flujo de trabajo reproducible y colaborativo.

---

## Descripción del Proyecto

El proyecto busca analizar las estadísticas del Mundial FIFA Qatar 2022 para identificar variables y patrones asociados al desempeño de las selecciones participantes.

Se utilizan herramientas del ecosistema científico de Python y buenas prácticas de desarrollo colaborativo, asegurando trazabilidad, documentación y reproducibilidad.

---

## Pregunta de Investigación

**¿Qué estadísticas influyen en el desempeño y los resultados obtenidos por las selecciones participantes en la Copa Mundial FIFA Qatar 2022?**

---

## Objetivo General

Analizar los datos del Mundial FIFA Qatar 2022 mediante técnicas de exploración, limpieza y transformación de datos, generando una base reproducible para posteriores análisis y visualizaciones.

---

## Objetivos Específicos

* Obtener y validar el conjunto de datos.
* Explorar la estructura y calidad de las variables.
* Identificar y tratar valores faltantes e inconsistencias.
* Transformar los datos para facilitar su análisis.
* Documentar las decisiones técnicas realizadas.
* Mantener un entorno reproducible y colaborativo mediante Git y GitHub.

---

## Dataset Utilizado

**Fuente:**

* FIFA World Cup 2022 Complete Dataset
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
6. Interpretación de resultados.

---

## Estructura del Repositorio

```text
proyecto-fifa-mcdi500/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── F1_Definicion.ipynb
│   └── F2_Definicion.ipynb
│
├── docs/
│
├── results/
│
├── src/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Estrategia de Trabajo Colaborativo

Se utiliza GitHub con una rama principal (**main**) y ramas por funcionalidad para cada integrante.

### Ramas

* `feature/f2-obtencion-exploracion`
* `feature/f2-limpieza-transformacion`
* `feature/f2-documentacion-validacion`

La integración se realiza mediante Pull Requests revisados por el equipo antes del merge a `main`.

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
feat(f2): agrega carga inicial del dataset

feat(f2): incorpora exploración del dataframe

feat(f2): implementa limpieza y transformación de datos

docs(f2): documenta decisiones técnicas
```

---

## Herramientas Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git
* GitHub

---

## Reproducibilidad

1. Clonar el repositorio.

```bash
git clone https://github.com/sauriomac/fifa-worldcup-2022-analysis.git
```

2. Crear entorno virtual.

```bash
python -m venv .venv
```

3. Activar el entorno.

```bash
source .venv/bin/activate
```

4. Instalar dependencias.

```bash
pip install -r requirements.txt
```

5. Ejecutar los notebooks ubicados en la carpeta `notebooks`.

---

## Integrantes

* Luis Rodrigo Espinoza
* Claudio Alarcón
* Enzo Pinilla

---

## Estado del Proyecto

Proyecto académico en desarrollo correspondiente al Magíster en Ciencia de Datos e Inteligencia Artificial.