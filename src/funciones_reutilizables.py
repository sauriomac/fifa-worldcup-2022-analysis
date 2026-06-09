"""Funciones reutilizables para el analisis del Mundial FIFA 2022."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def cargar_csv(ruta: str | Path, **kwargs) -> pd.DataFrame:
    """Carga un CSV y retorna un DataFrame."""
    return pd.read_csv(ruta, **kwargs)


def guardar_csv(df: pd.DataFrame, ruta: str | Path, **kwargs) -> None:
    """Guarda un DataFrame en CSV creando directorios si es necesario."""
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(destino, index=False, **kwargs)
