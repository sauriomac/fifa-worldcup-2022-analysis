# CHANGELOG

Historial de cambios del proyecto **fifa-worldcup-2022-analysis** para la asignatura **MCDI500 – Herramientas de Software Científico**.

Este archivo registra la evolución técnica del proyecto, las mejoras incorporadas y la progresión entre las fases F1, F2, F3 y F4. Su propósito es mantener la trazabilidad entre el repositorio, los notebooks, el informe final y las contribuciones del equipo.

---

## [F4] - Proyecto final integrador

**Fecha:** 20/06/2026  
**Objetivo:** Integrar las fases F1, F2 y F3 en un cierre final reproducible, incorporando visualizaciones, resultados, discusión, conclusiones y trazabilidad del proceso.

### Added

- Notebook final `F4_Definicion.ipynb`, integrando las fases F1, F2, F3 y F4.
- Sección de introducción, contextualización, problemática, objetivos y alcance.
- Integración del flujo reproducible completo del proyecto.
- Visualizaciones analíticas finales para comunicar los hallazgos.
- Secciones de resultados, discusión y conclusiones.
- Tabla de trazabilidad de mejoras entre F1, F2, F3 y F4.
- Archivo `CHANGELOG.md` como registro de evolución técnica.
- Actualización del enfoque comunicacional para informe final y presentación audiovisual.

### Changed

- Consolidación del proyecto en un notebook integrador final.
- Mejora de la documentación técnica y de la reproducibilidad.
- Refuerzo de la interpretación analítica de los resultados obtenidos.
- Organización del notebook como evidencia central para el informe final.
- Actualización del README para incluir F4, `CHANGELOG.md`, nuevas ramas y flujo de trabajo final.

### Validation

- Ejecución recomendada mediante `Kernel → Restart & Run All`.
- Verificación de coherencia entre notebook, informe técnico, README y repositorio GitHub.
- Validación de figuras y resultados intermedios.
- Confirmación de trazabilidad mediante Pull Requests, commits y contribuciones individuales.

### Commits y Pull Requests destacados

- `feat(f4): integrar contexto y reproducibilidad del proyecto`  
  Rama: `feature/f4-contexto-reproducibilidad`  
  Pull Request: `#29`  
  Responsable: Enzo Pinilla.

- `feat(f4): incorporar algoritmos eficiencia y POO`  
  Rama: `feature/f4-algoritmos-poo`  
  Pull Request: `#28`  
  Responsable: Claudio Alarcón.

- `feat(f4): agregar visualizaciones cierre y changelog`  
  Rama: `feature/f4-visualizacion-cierre`  
  Pull Request: `#30`  
  Responsable: Luis Rodrigo Espinoza.

---

## [F3] - Núcleo algorítmico, eficiencia y programación orientada a objetos

**Fecha:** 14/06/2026 - 18/06/2026  
**Objetivo:** Implementar soluciones algorítmicas eficientes, comparar enfoques, medir complejidad e incorporar programación orientada a objetos.

### Added

- Notebook `F3_Definicion.ipynb`.
- Reutilización del pipeline completo desarrollado en F2.
- Implementación de suma iterativa.
- Implementación de suma recursiva.
- Implementación de operaciones vectorizadas con Pandas.
- Implementación de ordenamiento recursivo mediante Merge Sort.
- Comparación con `sorted()`.
- Mediciones de eficiencia temporal mediante `timeit`.
- Análisis de complejidad temporal y espacial.
- Programación orientada a objetos con encapsulamiento, herencia y polimorfismo.
- Documentación técnica mediante celdas Markdown, comentarios y docstrings.
- Bibliografía y citas APA 7 incorporadas al notebook e informe.

### Changed

- Se corrigió la observación formativa sobre el pipeline incompleto, integrando el preprocesamiento reutilizado desde F2.
- Se incorporó POO para fortalecer modularidad, mantenibilidad y extensibilidad.
- Se mejoró la estructura del README para reflejar la fase algorítmica.
- Se reforzó la documentación técnica de las decisiones algorítmicas.

### Validation

- Validación de equivalencia entre resultados iterativos, recursivos y vectorizados.
- Pruebas mediante `assert`.
- Verificación de casos normales, límite y excepciones.
- Ejecución recomendada mediante `Kernel → Restart & Run All`.

### Commits y Pull Requests destacados

- `feat(f3): integrar pipeline completo reutilizado desde F2`  
  Rama: `feature/integrar_pipeline`  
  Pull Request: `#24`  
  Commit: `2193460`  
  Responsable: Claudio Alarcón.

- `feat(f3): implementar nucleo algoritmico y mediciones de complejidad`  
  Rama: `feature/integrar_nucleo`  
  Pull Request: `#25`  
  Commit: `6cb286a`  
  Responsable: Enzo Pinilla.

- `feat(f3): incorporar POO y documentacion final de arquitectura`  
  Rama: `feature/incorporar_poo`  
  Pull Request: `#26`  
  Commit: `00fa9fd`  
  Responsable: Luis Rodrigo Espinoza.

- `docs(readme): actualiza documentación y estructura del repositorio para la fase 3`  
  Commit: `2959ba8`.

- `docs(f3): agrega bibliografía y referencias APA 7 al notebook F3_Definicion`  
  Commit: `92d4da3`.

- `feat(f3): completar notebook con métricas y conclusiones`  
  Commit: `f150480`.

---

## [F2] - Obtención, limpieza y transformación de datos

**Fecha:** 12/06/2026 - 15/06/2026  
**Objetivo:** Construir un pipeline de preprocesamiento reproducible para preparar el dataset del Mundial FIFA Qatar 2022.

### Added

- Notebook `F2_Definicion.ipynb`.
- Carga del dataset desde `data/raw/`.
- Revisión de estructura del dataset.
- Validación de valores nulos.
- Validación de registros duplicados.
- Conversión de variables porcentuales a formato numérico.
- Transformación de variables necesarias para análisis posterior.
- Normalización y escalamiento de características.
- Generación de dataset procesado en `data/processed/`.
- Funciones reutilizables en `src/funciones_reutilizables.py`.

### Changed

- Se reorganizó el flujo de preprocesamiento para mejorar trazabilidad.
- Se separaron funciones reutilizables desde el notebook hacia `src/`.
- Se mejoró el README con instrucciones de ejecución y estructura del repositorio.
- Se normalizaron autores mediante `.mailmap`.

### Validation

- Validación de nulos y duplicados.
- Comprobación del dataset procesado.
- Verificación de consistencia entre notebook, datos procesados y funciones reutilizables.

### Commits y Pull Requests destacados

- `docs(readme):actualizacion de readme`  
  Commit: `43e3894`  
  Responsable: Claudio Alarcón.

- `doc(referencias): update referencias`  
  Commit: `c09f7a6`  
  Responsable: Enzo Pinilla.

- `feat: update de funciones reutilizables y update de import de funciones en archivo f2`  
  Commit: `8ce82f6`.

- `chore: unificar git contributor identities usando mailmap`  
  Commit: `1235552`.

- `chore: normalizar autores con mailmap`  
  Commit: `8238d35`.

- Merge de ramas `feature-data`, `feature-analysis` y `feature-visualization` hacia `main`.

---

## [F1] - Definición y orientación del problema

**Fecha:** Junio 2026  
**Objetivo:** Definir la problemática, la pregunta de investigación, los objetivos y la estructura inicial del proyecto reproducible.

### Added

- Definición de la problemática asociada al análisis del Mundial FIFA Qatar 2022.
- Pregunta de investigación.
- Objetivo general y objetivos específicos.
- Descripción inicial del dataset.
- Organización preliminar del repositorio.
- Configuración inicial de carpetas para datos, notebooks, resultados y documentación.
- Primeras referencias bibliográficas del proyecto.

### Changed

- Ajuste de la estructura del repositorio para alinearse con el flujo reproducible del proyecto.
- Incorporación progresiva de README y documentación inicial.
- Preparación del entorno para trabajo colaborativo mediante Git y GitHub.

### Validation

- Revisión de coherencia entre problema, dataset y objetivos.
- Confirmación de que la estructura inicial permitiera continuar con F2, F3 y F4.

---

## Síntesis de trazabilidad F1-F4

| Fase | Propósito | Mejora principal | Evidencia |
|---|---|---|---|
| F1 | Definir problema y objetivos | Estructura inicial reproducible | `F1_Definicion.ipynb`, README inicial |
| F2 | Preparar datos | Pipeline de limpieza, transformación y validación | `F2_Definicion.ipynb`, `funciones_reutilizables.py` |
| F3 | Implementar algoritmos y POO | Eficiencia, recursividad, `timeit` y clases | `F3_Definicion.ipynb`, `funciones_f3_algoritmos.py` |
| F4 | Integrar y comunicar resultados | Visualizaciones, conclusiones y trazabilidad final | `F4_Definicion.ipynb`, `CHANGELOG.md`, informe final |

---

## Validación final del proyecto

Antes de la entrega final se debe verificar:

- Ejecutar `Kernel → Restart & Run All` en los notebooks principales.
- Confirmar que `requirements.txt` contiene las dependencias necesarias.
- Confirmar que `README.md` describe correctamente la ejecución y organización del proyecto.
- Confirmar que `CHANGELOG.md` registra la evolución F1-F4.
- Confirmar que las figuras se encuentran en `results/figures/`.
- Confirmar coherencia entre repositorio, notebooks, informe final y presentación audiovisual.
