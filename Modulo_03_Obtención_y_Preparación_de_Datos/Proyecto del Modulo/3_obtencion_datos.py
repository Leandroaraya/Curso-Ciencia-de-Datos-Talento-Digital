import pandas as pd

# ==================================================
# LECCIÓN 3 – OBTENCIÓN E INTEGRACIÓN DE DATOS
# ==================================================

# --------------------------------------------------
# 1. Creación de datos complementarios (Excel)
# --------------------------------------------------
# Información adicional asociada a cada cliente
info_complementaria = pd.DataFrame({
    "cliente_id": range(1, 21),
    "ciudad": [
        "Santiago", "Valparaíso", "Concepción", "La Serena", "Antofagasta",
        "Rancagua", "Talca", "Chillán", "Temuco", "Valdivia",
        "Osorno", "Puerto Montt", "Coyhaique", "Punta Arenas", "Arica",
        "Iquique", "Calama", "Copiapó", "Ovalle", "Los Andes"
    ],
    "segmento": [
        "Premium", "Regular", "Regular", "Premium", "Básico",
        "Regular", "Básico", "Regular", "Premium", "Regular",
        "Básico", "Premium", "Regular", "Básico", "Premium",
        "Regular", "Básico", "Regular", "Premium", "Básico"
    ]
})

# Guardar información complementaria en archivo Excel
info_complementaria.to_excel("data/3_0_info_clientes.xlsx", index=False)

print("Archivo Excel con información complementaria creado correctamente")


# --------------------------------------------------
# 2. Carga de datos desde archivo CSV (Lección 2)
# --------------------------------------------------

df_clientes = pd.read_csv("data/2_clientes_preliminar.csv")

print("\nDatos cargados desde CSV")
print(df_clientes.head())


# --------------------------------------------------
# 3. Carga de datos desde archivo Excel
# --------------------------------------------------

df_info_excel = pd.read_excel("data/3_info_clientes.xlsx")

print("\nDatos cargados desde Excel")
print(df_info_excel.head())


# --------------------------------------------------
# 4. Unificación de fuentes de datos (merge)
# --------------------------------------------------

df_unificado = pd.merge(
    df_clientes,
    df_info_excel,
    on="cliente_id",
    how="inner"
)

print("\nDataFrame unificado correctamente")
print(df_unificado.head())


# --------------------------------------------------
# 5. Guardar DataFrame unificado
# --------------------------------------------------

df_unificado.to_csv("data/3_1_dataset_unificado.csv", index=False)

print("\nDataFrame unificado guardado como 'dataset_unificado.csv'")
