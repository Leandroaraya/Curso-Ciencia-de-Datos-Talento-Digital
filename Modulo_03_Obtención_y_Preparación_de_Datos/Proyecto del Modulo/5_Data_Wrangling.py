import pandas as pd
import matplotlib.pyplot as plt
# =========================
# 1. Carga del dataset limpio
# =========================

df = pd.read_csv("data/4_dataset_unificado_limpio.csv")

print("DataFrame limpio cargado correctamente")
print(df.head())

# =========================
# 2. Eliminación de registros duplicados
# =========================

print("\nCantidad de filas antes de eliminar duplicados:", len(df))
print("Duplicados encontrados:", df.duplicated().sum())

df = df.drop_duplicates()

print("Cantidad de filas después de eliminar duplicados:", len(df))

# =========================
# 3. Revisión y transformación de tipos de datos
# =========================

print("\nTipos de datos antes de transformación")
print(df.dtypes)

# (En este caso los tipos ya son correctos, pero este paso es clave
# para validar consistencia antes de cálculos)

# =========================
# 4. Creación de nuevas columnas calculadas
# =========================

# Cálculo del IVA (19%)
df["iva"] = df["monto"] * 0.19

# Cálculo del total con IVA
df["total_con_iva"] = df["monto"] + df["iva"]

# =========================
# 5. Creación de variable categórica derivada
# =========================
# Clasificación del monto de compra en niveles

def clasificar_monto(monto):
    if monto < 20000:
        return "Bajo"
    elif monto < 50000:
        return "Medio"
    else:
        return "Alto"

df["nivel_compra"] = df["monto"].apply(clasificar_monto)

print("\nDataFrame después de las transformaciones")
print(df.head())

#---------------------------------------------
#Boxplot para ver cambios
plt.figure(figsize=(6, 4))
plt.boxplot(df["monto"], vert=False)
plt.title("Boxplot de montos de transacción luego de los cambios")
plt.xlabel("Monto")
plt.show()


# =========================
# 6. Guardado del dataset transformado
# =========================

df.to_csv("data/5_df_wrangling.csv", index=False)

print("\nDataFrame optimizado guardado correctamente")

