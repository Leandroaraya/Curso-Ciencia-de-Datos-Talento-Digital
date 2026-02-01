# --------------------------------------------------
# Importación de librerías
# --------------------------------------------------
import numpy as np
import pandas as pd

# --------------------------------------------------
# Carga de datos generados con NumPy
# --------------------------------------------------
clientes = np.load("data/1_clientes_id.npy")
edades = np.load("data/1_edades.npy")
montos = np.load("data/1_montos.npy")

# --------------------------------------------------
# Creación del DataFrame
# --------------------------------------------------
df = pd.DataFrame({
    "cliente_id": clientes,
    "edad": edades,
    "monto": montos
})

print("DataFrame creado correctamente")
print(df)
# --------------------------------------------------
# Creacion de data erronea
#-------------------------------------------------
# --------------------------------------------------
# Introducción intencional de datos erróneos (simulación)
# --------------------------------------------------

# Edad negativa (error)
df.loc[0, "edad"] = -20

# Edad excesivamente alta (error)
df.loc[1, "edad"] = 130

# Monto extremadamente alto (outlier)
df.loc[2, "monto"] = 1_233_000

# Valor faltante (NaN)
df.loc[7, "edad"] = np.nan   # edad faltante
# --------------------------------------------------
# Introducción de registros duplicados
# --------------------------------------------------

# Duplicar 4 filas aleatorias
filas_duplicadas = df.sample(4, random_state=42)
df = pd.concat([df, filas_duplicadas], ignore_index=True)

print("\nDataFrame con datos erróneos y duplicados")
print(df)




# --------------------------------------------------
# Exploración inicial de los datos
# --------------------------------------------------

# Visualización de las primeras y últimas filas
print("\nPrimeras filas del DataFrame")
print(df.head())

print("\nÚltimas filas del DataFrame")
print(df.tail())

# --------------------------------------------------
# Estadísticas descriptivas
# --------------------------------------------------
print("\nCaracterísticas descriptivas de los datos")
print(df.describe())

# --------------------------------------------------
# Aplicación de filtros
# --------------------------------------------------
print("\nTransacciones con monto mayor a 20.000")
df_filtrado = df[df["monto"] > 20000]
print(df_filtrado)

# --------------------------------------------------
# Exportación del DataFrame preliminar
# --------------------------------------------------
df.to_csv("data/2_clientes_preliminar.csv", index=False)

print("\nArchivo 'clientes_preliminar.csv' exportado correctamente")

# --------------------------------------------------
# Comentario descriptivo del proceso
# --------------------------------------------------
"""
En esta etapa se utilizaron las funcionalidades de la librería Pandas para cargar,
explorar y analizar los datos generados previamente con NumPy. Los arreglos fueron
convertidos en un DataFrame, lo que permitió trabajar con una estructura tabular
más flexible y adecuada para el análisis de datos.

Durante la exploración inicial se visualizaron las primeras y últimas filas del
dataset, facilitando la comprensión de su estructura y contenido. Asimismo, se
obtuvieron estadísticas descriptivas que permitieron analizar el comportamiento
general de los montos de las transacciones.

Posteriormente, se aplicaron filtros condicionales para seleccionar transacciones
con montos superiores a 20.000, demostrando la facilidad con la que Pandas permite
extraer subconjuntos de información según criterios definidos.

Finalmente, el DataFrame preliminar fue exportado a formato CSV para su uso en
etapas posteriores del flujo de trabajo de análisis de datos.
"""
