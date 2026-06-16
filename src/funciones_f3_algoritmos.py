"""Algoritmos de apoyo para la Fase 3 del proyecto FIFA World Cup 2022.

Este módulo contiene prototipos iniciales para comparar enfoques
estructurados, recursivos y vectorizados sobre el dataset procesado en Fase 2.
El objetivo es dejar evidencia de diseño algorítmico, modularidad y mediciones
básicas de complejidad temporal/espacial.
"""

from __future__ import annotations

import sys
import timeit
from typing import Callable, Iterable, Sequence

import pandas as pd


GOLES_TEAM1 = "number of goals team1"
GOLES_TEAM2 = "number of goals team2"
TEAM1 = "team1"
TEAM2 = "team2"


def validar_columnas(df: pd.DataFrame, columnas: Sequence[str]) -> bool:
    """Verifica que todas las columnas requeridas existan en el DataFrame."""
    faltantes = [col for col in columnas if col not in df.columns]
    if faltantes:
        raise KeyError(f"Columnas faltantes en el DataFrame: {faltantes}")
    return True


def preparar_lista_goles(
    df: pd.DataFrame,
    col_goles_team1: str = GOLES_TEAM1,
    col_goles_team2: str = GOLES_TEAM2,
) -> list[int]:
    """Construye una lista simple con los goles de ambos equipos por partido.

    Entrada: DataFrame de partidos.
    Proceso: selecciona las columnas de goles, las convierte a enteros y une
    ambos vectores en una sola lista.
    Salida: lista de enteros para algoritmos iterativos y recursivos.
    """
    validar_columnas(df, [col_goles_team1, col_goles_team2])

    goles_team1 = pd.to_numeric(df[col_goles_team1], errors="coerce").fillna(0).astype(int)
    goles_team2 = pd.to_numeric(df[col_goles_team2], errors="coerce").fillna(0).astype(int)

    return goles_team1.tolist() + goles_team2.tolist()


def suma_iterativa(datos: Iterable[int | float]) -> int | float:
    """Suma una colección usando programación estructurada iterativa.

    Complejidad temporal esperada: O(n).
    Complejidad espacial adicional esperada: O(1).
    """
    total = 0
    for valor in datos:
        total += valor
    return total


def suma_recursiva(datos: Sequence[int | float], indice: int = 0) -> int | float:
    """Suma una secuencia usando recursividad con índice.

    Se evita usar slicing para no crear copias de listas en cada llamada.
    Complejidad temporal esperada: O(n).
    Complejidad espacial adicional esperada: O(n), por la pila de llamadas.
    """
    if indice >= len(datos):
        return 0
    return datos[indice] + suma_recursiva(datos, indice + 1)


def suma_vectorizada_pandas(
    df: pd.DataFrame,
    col_goles_team1: str = GOLES_TEAM1,
    col_goles_team2: str = GOLES_TEAM2,
) -> int | float:
    """Suma goles usando operaciones vectorizadas de pandas."""
    validar_columnas(df, [col_goles_team1, col_goles_team2])
    return df[col_goles_team1].sum() + df[col_goles_team2].sum()


def obtener_goles_por_equipo(
    df: pd.DataFrame,
    col_team1: str = TEAM1,
    col_team2: str = TEAM2,
    col_goles_team1: str = GOLES_TEAM1,
    col_goles_team2: str = GOLES_TEAM2,
) -> list[tuple[str, int]]:
    """Calcula goles acumulados por selección a partir de team1 y team2."""
    validar_columnas(df, [col_team1, col_team2, col_goles_team1, col_goles_team2])

    goles_1 = df[[col_team1, col_goles_team1]].rename(
        columns={col_team1: "team", col_goles_team1: "goals"}
    )
    goles_2 = df[[col_team2, col_goles_team2]].rename(
        columns={col_team2: "team", col_goles_team2: "goals"}
    )

    goles = pd.concat([goles_1, goles_2], ignore_index=True)
    goles["goals"] = pd.to_numeric(goles["goals"], errors="coerce").fillna(0).astype(int)

    acumulado = goles.groupby("team", as_index=False)["goals"].sum()
    return list(acumulado.itertuples(index=False, name=None))


def merge_sort_recursivo(datos: Sequence[tuple[str, int]]) -> list[tuple[str, int]]:
    """Ordena recursivamente pares (equipo, goles) de mayor a menor.

    Este algoritmo usa la estrategia divide and conquer.
    Complejidad temporal esperada: O(n log n).
    Complejidad espacial adicional esperada: O(n).
    """
    if len(datos) <= 1:
        return list(datos)

    mitad = len(datos) // 2
    izquierda = merge_sort_recursivo(datos[:mitad])
    derecha = merge_sort_recursivo(datos[mitad:])

    return _mezclar_descendente(izquierda, derecha)


def _mezclar_descendente(
    izquierda: Sequence[tuple[str, int]],
    derecha: Sequence[tuple[str, int]],
) -> list[tuple[str, int]]:
    """Mezcla dos listas ordenadas de pares (equipo, goles) en orden descendente."""
    resultado: list[tuple[str, int]] = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][1] >= derecha[j][1]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def ordenar_builtin(datos: Sequence[tuple[str, int]]) -> list[tuple[str, int]]:
    """Ordena pares (equipo, goles) con la función optimizada sorted de Python."""
    return sorted(datos, key=lambda item: item[1], reverse=True)


def medir_tiempo(funcion: Callable, repeticiones: int = 1000) -> float:
    """Mide el tiempo de ejecución de una función sin argumentos."""
    return timeit.timeit(funcion, number=repeticiones)


def estimar_memoria_lista(datos: Sequence) -> int:
    """Estima memoria superficial de una lista y sus elementos en bytes.

    La medición es aproximada y se utiliza solo como referencia básica para la
    discusión de complejidad espacial.
    """
    return sys.getsizeof(datos) + sum(sys.getsizeof(item) for item in datos)
