
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# 1. Carga del DataFrame consolidado
# ==================================================

df_unificado = pd.read_csv("data/3_1_dataset_unificado.csv")

print("DataFrame unificado cargado correctamente")
print(df_unificado.head())

# ==================================================
# 2. Identificación de valores nulos iniciales
# ==================================================

print("\nCantidad de valores nulos por columna")
print(df_unificado.isnull().sum())

print("\nPorcentaje de valores nulos (%)")
print((df_unificado.isnull().mean() * 100).round(2))

# ==================================================
# 3. Tratamiento de valores inválidos en la variable edad
# ==================================================

"""
Las edades negativas o superiores a 120 años no son valores realistas,
por lo que se consideran errores de registro y se convierten en NaN.
"""

edad_min = 0
edad_max = 120

df_unificado.loc[
    (df_unificado["edad"] < edad_min) |
    (df_unificado["edad"] > edad_max),
    "edad"
] = np.nan

print("\nEdades fuera de rango convertidas a NaN")
print(df_unificado["edad"].isnull().sum())

# Imputación de valores faltantes en edad con la media
media_edad = df_unificado["edad"].mean()
df_unificado["edad"] = df_unificado["edad"].fillna(media_edad)

print("\nMedia de edad utilizada para imputación:", round(media_edad, 2))


# ==================================================
# 4. Detección de outliers en la variable monto (IQR)
# ==================================================

# Asegurar tipo numérico correcto
df_unificado["monto"] = df_unificado["monto"].astype(float)
df_unificado["edad"] = df_unificado["edad"].astype(int)

# -------------------------------
# Visualización exploratoria
# -------------------------------
"""
Se utiliza un boxplot como herramienta exploratoria para visualizar
la dispersión de los montos y la presencia de posibles valores atípicos.
Esta visualización sirve como apoyo al análisis estadístico, pero no
reemplaza el método programático de detección.
"""

plt.figure(figsize=(6, 4))
plt.boxplot(df_unificado["monto"], vert=False)
plt.title("Boxplot de montos de transacción")
plt.xlabel("Monto")
plt.show()

# -------------------------------
# Cálculo estadístico con IQR
# -------------------------------

Q1 = df_unificado["monto"].quantile(0.25)
Q3 = df_unificado["monto"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_iqr = df_unificado[
    (df_unificado["monto"] < limite_inferior) |
    (df_unificado["monto"] > limite_superior)
]

print("\nOutliers detectados mediante IQR")
print(outliers_iqr)


"""
Los outliers corresponden a valores atípicos que pueden distorsionar
las métricas estadísticas del conjunto de datos. Se detectan usando
el método del rango intercuartílico (IQR), el cual es robusto ante
distribuciones no normales.
"""

# ==================================================
# 5. Tratamiento de outliers
# ==================================================

# Media calculada sin considerar valores extremos
media_monto = df_unificado.loc[
    (df_unificado["monto"] >= limite_inferior) &
    (df_unificado["monto"] <= limite_superior),
    "monto"
].mean()

# Reemplazo de outliers por la media
df_unificado.loc[
    (df_unificado["monto"] < limite_inferior) |
    (df_unificado["monto"] > limite_superior),
    "monto"
] = media_monto

print("\nMedia utilizada para reemplazar outliers:", round(media_monto, 2))
print("\nDataFrame después del tratamiento de valores inválidos y outliers")
print(df_unificado.head())

# ==================================================
# 6. Guardado del DataFrame limpio
# ==================================================

df_unificado.to_csv("data/4_dataset_unificado_limpio.csv", index=False)

print("\nDataset limpio guardado correctamente")
print(df_unificado)
