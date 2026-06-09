# proyecto-fifa-mcdi500

Repositorio para el analisis del Mundial FIFA 2022 con enfoque en organizacion, trazabilidad y reproducibilidad del trabajo en equipo.

## Estructura del proyecto

```text
proyecto-fifa-mcdi500/
├── data/
│   ├── raw/                  # dataset original descargado desde Kaggle
│   └── processed/            # datos transformados y preparados
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
```

## Primeros commits proyectados

- `docs: agrega README inicial del proyecto`
- `data: incorpora dataset FIFA World Cup 2022`
- `feat: crea notebook de analisis exploratorio`
- `docs: agrega documentacion inicial del proyecto`
- `feat: incorpora visualizaciones preliminares`
- `fix: corrige nombres y formatos de variables`
- `refactor: reorganiza estructura del repositorio`

## Estrategia de ramas

La rama principal es `main` y cada integrante trabaja en ramas por funcionalidad:

- `feature-data`
- `feature-analysis`
- `feature-documentation`
- `feature-visualization`

La integracion se realiza mediante Pull Requests revisados por el equipo antes de mergear a `main`.

## Convencion de commits

Se utiliza Conventional Commits para mantener un historial claro y consistente:

- `feat`: nueva funcionalidad
- `docs`: cambios de documentacion
- `fix`: correcciones de errores
- `refactor`: mejoras internas sin cambiar funcionalidad
- `chore`: tareas de mantenimiento

## Entorno de trabajo

1. Crear y activar entorno virtual.
2. Instalar dependencias desde `requirements.txt`.
3. Ejecutar notebooks en la carpeta `notebooks/`.