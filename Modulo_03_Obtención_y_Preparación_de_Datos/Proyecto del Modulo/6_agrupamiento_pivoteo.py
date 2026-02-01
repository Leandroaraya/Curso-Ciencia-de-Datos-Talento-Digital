import pandas as pd
import numpy as np

# ==================================================
# 1. Carga del DataFrame final preparado
# ==================================================

df = pd.read_csv("data/5_df_wrangling.csv")

print("DataFrame final cargado correctamente")
print(df)

# ==================================================
# 2. Análisis agregado con groupby()
# ==================================================

# Ventas por ciudad
ventas_por_ciudad = df.groupby("ciudad")["monto"].agg(
    total_ventas="sum",
    promedio_ventas="mean",
    cantidad_transacciones="count"
).reset_index()

print("\nVentas por ciudad")
print(ventas_por_ciudad)

# Análisis descriptivo alternativo
print("\nResumen estadístico por ciudad (describe)")
print(df.groupby("ciudad")["monto"].describe())

# Ventas por nivel de compra
ventas_por_nivel = df.groupby("nivel_compra")["monto"].agg(
    total_ventas="sum",
    promedio_ventas="mean",
    operaciones="count"
).reset_index()

print("\nVentas por nivel de compra")
print(ventas_por_nivel)

# ==================================================
# 3. Análisis combinado por ciudad y segmento
# ==================================================

resumen_ciudad_segmento = df.groupby(
    ["ciudad", "segmento"]
)["monto"].agg(
    total="sum",
    promedio="mean",
    transacciones="count"
).reset_index()

print("\nResumen por ciudad y segmento")
print(resumen_ciudad_segmento)

# ==================================================
# 4. Reestructuración de datos: pivot() y melt()
# ==================================================

# Tabla dinámica: promedio de ventas por ciudad y segmento
pivot_ventas = resumen_ciudad_segmento.pivot(
    index="ciudad",
    columns="segmento",
    values="promedio"
)

print("\nTabla pivot - Promedio de ventas por ciudad y segmento")
print(pivot_ventas)

# Volver a formato largo usando melt
melt_ventas = pivot_ventas.reset_index().melt(
    id_vars="ciudad",
    var_name="segmento",
    value_name="promedio_ventas"
)

# Eliminación de valores nulos generados por el pivot
melt_ventas_limpio = melt_ventas.dropna()

print("\nDatos reestructurados en formato largo (melt)")
print(melt_ventas_limpio)

# ==================================================
# 5. Incorporación de nuevas fuentes de datos
# ==================================================

# DataFrame auxiliar con información adicional de clientes
df_clientes_info = df[["cliente_id"]].drop_duplicates().reset_index(drop=True)

df_clientes_info["antiguedad_meses"] = np.random.randint(
    6, 48, size=len(df_clientes_info)
)

df_clientes_info["canal"] = np.random.choice(
    ["Web", "App"], size=len(df_clientes_info)
)

print("\nInformación adicional de clientes")
print(df_clientes_info.head())

# ==================================================
# 6. Combinación de datos: merge() y concat()
# ==================================================

# Merge para incorporar información adicional de clientes
df_merge = df.merge(
    df_clientes_info,
    on="cliente_id",
    how="left"
)

print("\nDataFrame combinado con merge")
print(df_merge.head())

# Simulación de nuevos registros usando concat
df_extra = df_merge.sample(5, random_state=42).copy()
df_extra["monto"] = df_extra["monto"] * 1.05  # ajuste simulado

df_final = pd.concat(
    [df_merge, df_extra],
    ignore_index=True
)

print("\nDataFrame final luego de concat")
print(df_final.tail())
print(df_final)

# ==================================================
# 7. Exportación del dataset final
# ==================================================

df_final.to_csv("data/6_dataset_final_ecommerce.csv", index=False)
print("\nArchivo CSV final exportado correctamente")

df_final.to_excel("data/6_dataset_final_ecommerce.xlsx", index=False)
print("Archivo Excel final exportado correctamente")
