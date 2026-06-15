"""Funciones reutilizables para el analisis del Mundial FIFA 2022.

Este modulo concentra las funciones del pipeline de Fase 2 para que los
notebooks actuen como orquestadores del flujo y no como unico lugar donde
vive la logica del proyecto.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def cargar_csv(ruta: str | Path, **kwargs) -> pd.DataFrame:
    """Carga un CSV y retorna un DataFrame."""
    return pd.read_csv(ruta, **kwargs)


def guardar_csv(df: pd.DataFrame, ruta: str | Path, **kwargs) -> None:
    """Guarda un DataFrame en CSV creando directorios si es necesario."""
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(destino, index=False, **kwargs)


def cargar_datos(ruta):
    """
    Carga el conjunto de datos desde un archivo CSV.

    Parametros
    ----------
    ruta : str
        Ruta del archivo CSV de entrada.

    Retorna
    -------
    pd.DataFrame
        DataFrame con los datos cargados.

    Lanza
    -----
    FileNotFoundError
        Si la ruta indicada no existe.
    """
    try:
        df = pd.read_csv(ruta)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"No se encontro el archivo '{ruta}'. "
            "Verifica que el CSV este en la ruta indicada."
        )

    print(f"Datos cargados: {df.shape[0]} filas y {df.shape[1]} columnas.")
    return df


def explorar_dataframe(df):
    """
    Genera un resumen exploratorio inicial del DataFrame.

    Parametros
    ----------
    df : pd.DataFrame
        Dataset a explorar.

    Retorna
    -------
    pd.DataFrame
        Estadisticos descriptivos de las variables numericas.
    """
    print("Dimensiones:", df.shape)
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print("\nEstadisticos descriptivos de variables numericas:")
    return df.describe()


def normalizar_nombres_columnas(df):
    """
    Normaliza los nombres de columnas eliminando espacios extremos,
    reemplazando espacios multiples por uno solo y convirtiendo a minusculas.

    Esto evita errores por columnas con dobles espacios o diferencias de formato.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", " ", regex=True)
    )
    return df


def imputar_nulos_numericos(df, columna, estrategia="mediana"):
    """
    Imputa valores nulos en una columna numerica usando media o mediana.

    Parametros
    ----------
    df : pd.DataFrame
        Dataset de entrada.
    columna : str
        Nombre de la columna numerica.
    estrategia : str
        Estrategia de imputacion: 'media' o 'mediana'.

    Retorna
    -------
    pd.DataFrame
        Dataset con la columna imputada.
    """
    if columna not in df.columns:
        raise KeyError(f"La columna '{columna}' no existe en el DataFrame.")

    if not pd.api.types.is_numeric_dtype(df[columna]):
        raise TypeError(f"La columna '{columna}' debe ser numerica para imputar.")

    df = df.copy()
    n_nulos = int(df[columna].isnull().sum())

    if estrategia == "media":
        valor = df[columna].mean()
    elif estrategia == "mediana":
        valor = df[columna].median()
    else:
        raise ValueError("estrategia debe ser 'media' o 'mediana'.")

    df[columna] = df[columna].fillna(valor)
    print(f"'{columna}': {n_nulos} nulos imputados con {estrategia} = {valor:.2f}")
    return df


def convertir_porcentaje(df, columna):
    """
    Convierte una columna con porcentajes en texto a valores numericos float.

    Ejemplo: '42%' -> 42.0
    """
    if columna not in df.columns:
        raise KeyError(f"La columna '{columna}' no existe en el DataFrame.")

    df = df.copy()
    df[columna] = (
        df[columna]
        .astype(str)
        .str.replace('%', '', regex=False)
        .str.strip()
        .astype(float)
    )
    return df


def transformar_fecha_hora(df, columna_fecha='date', columna_hora='hour'):
    """
    Transforma columnas de fecha y hora en variables numericas derivadas.

    Parametros
    ----------
    df : pd.DataFrame
        Dataset de entrada.
    columna_fecha : str
        Columna que contiene la fecha del partido.
    columna_hora : str
        Columna que contiene la hora del partido.

    Retorna
    -------
    pd.DataFrame
        Dataset con variables temporales derivadas.
    """
    for columna in [columna_fecha, columna_hora]:
        if columna not in df.columns:
            raise KeyError(f"La columna '{columna}' no existe en el DataFrame.")

    df = df.copy()

    # La fecha viene en formato como '20 NOV 2022'.
    df['match_date'] = pd.to_datetime(df[columna_fecha], format='%d %b %Y')
    df['match_day'] = df['match_date'].dt.day
    df['match_month'] = df['match_date'].dt.month

    # La hora viene en formato como '17 : 00'. Se extrae la hora antes de ':'.
    df['match_hour'] = (
        df[columna_hora]
        .astype(str)
        .str.replace(' ', '', regex=False)
        .str.split(':')
        .str[0]
        .astype(int)
    )

    return df


def crear_variables_resultado(df):
    """
    Crea variables derivadas asociadas al resultado del partido.
    """
    requeridas = ['number of goals team1', 'number of goals team2']
    for col in requeridas:
        if col not in df.columns:
            raise KeyError(f"La columna requerida '{col}' no existe.")

    df = df.copy()
    df['goal_difference_team1'] = df['number of goals team1'] - df['number of goals team2']

    condiciones = [
        df['goal_difference_team1'] > 0,
        df['goal_difference_team1'] == 0,
        df['goal_difference_team1'] < 0
    ]
    valores = ['win', 'draw', 'loss']
    df['result_team1'] = np.select(condiciones, valores, default='unknown')

    return df


def codificar_one_hot_auto(df, columna, prefijo=None):
    """
    Codifica una variable categorica nominal usando One-Hot Encoding.

    Parametros
    ----------
    df : pd.DataFrame
        Dataset de entrada.
    columna : str
        Columna categorica a codificar.
    prefijo : str
        Prefijo para las nuevas columnas. Si no se entrega, usa el nombre de la columna.

    Retorna
    -------
    tuple[pd.DataFrame, list]
        DataFrame transformado y lista de nuevas columnas creadas.
    """
    if columna not in df.columns:
        raise KeyError(f"La columna '{columna}' no existe en el DataFrame.")

    df = df.copy()
    prefijo = prefijo or columna.replace(' ', '_')

    dummies = pd.get_dummies(df[columna], prefix=prefijo, dtype=int)
    df = df.drop(columns=[columna])
    df = pd.concat([df, dummies], axis=1)

    print(f"'{columna}' codificada en {len(dummies.columns)} columnas.")
    return df, dummies.columns.tolist()


def eliminar_columnas(df, columnas):
    """
    Elimina columnas especificadas si existen en el DataFrame.
    """
    df = df.copy()
    existentes = [col for col in columnas if col in df.columns]
    df = df.drop(columns=existentes)
    print(f"Columnas eliminadas: {existentes}")
    return df


def obtener_columnas_a_escalar(df, excluir=None):
    """
    Selecciona columnas numericas continuas para escalamiento.

    Se excluyen columnas binarias y columnas definidas manualmente.
    """
    excluir = excluir or []
    columnas = []

    for col in df.select_dtypes(include=[np.number]).columns:
        valores_unicos = df[col].dropna().unique()
        es_binaria = set(valores_unicos).issubset({0, 1})
        if not es_binaria and col not in excluir:
            columnas.append(col)

    return columnas


def escalar_caracteristicas(df, columnas):
    """
    Estandariza columnas numericas usando StandardScaler.

    Parametros
    ----------
    df : pd.DataFrame
        Dataset de entrada.
    columnas : list[str]
        Columnas numericas a estandarizar.

    Retorna
    -------
    tuple[pd.DataFrame, StandardScaler]
        Dataset transformado y scaler ajustado.
    """
    df = df.copy()

    if not columnas:
        raise ValueError("Debe existir al menos una columna para escalar.")

    for col in columnas:
        if col not in df.columns:
            raise KeyError(f"La columna '{col}' no existe en el DataFrame.")
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise TypeError(f"La columna '{col}' debe ser numerica para escalar.")

    scaler = StandardScaler()
    df[columnas] = scaler.fit_transform(df[columnas])
    return df, scaler


def validar_dataset(df, grupos_one_hot=None):
    """
    Valida integridad, consistencia y coherencia del dataset final.

    Lanza AssertionError si alguna condicion critica no se cumple.
    """
    print("VALIDACION DEL DATASET FINAL")
    print("-" * 50)

    # 1. Integridad: sin valores nulos
    nulos = int(df.isnull().sum().sum())
    assert nulos == 0, f"Quedan {nulos} valores nulos."
    print(f"[OK] Sin valores nulos: {nulos}")

    # 2. Consistencia: todas las columnas numericas
    no_numericas = df.select_dtypes(exclude=[np.number]).columns.tolist()
    assert not no_numericas, f"Columnas no numericas: {no_numericas}"
    print("[OK] Todas las columnas son numericas")

    # 3. Coherencia de grupos One-Hot
    if grupos_one_hot:
        for nombre, columnas in grupos_one_hot.items():
            columnas_existentes = [c for c in columnas if c in df.columns]
            suma = df[columnas_existentes].sum(axis=1)
            assert (suma == 1).all(), f"El grupo '{nombre}' no suma 1 en todas las filas."
            print(f"[OK] Grupo one-hot '{nombre}' coherente")

    # 4. Duplicados
    duplicados = int(df.duplicated().sum())
    print(f"[INFO] Filas duplicadas: {duplicados}")

    # 5. Dimensiones finales
    assert df.shape[0] > 0, "El dataset final quedo sin filas."
    assert df.shape[1] > 0, "El dataset final quedo sin columnas."
    print(f"[INFO] Dimensiones finales: {df.shape}")

    return True
