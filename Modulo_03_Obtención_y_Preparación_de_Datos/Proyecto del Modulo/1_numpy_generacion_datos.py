# 1. APLICANDO NUMPY PARA GENERAR DATOS
import numpy as np

# --------------------------------------------------
# Configuración inicial
# --------------------------------------------------
# Fijar semilla para asegurar reproducibilidad
np.random.seed(42)

# --------------------------------------------------
# Generación de datos ficticios
# --------------------------------------------------

# Datos de clientes
clientes_id = np.arange(1, 21)          # IDs de 20 clientes
edades = np.random.randint(18, 65, 20)  # Edades entre 18 y 64 años

# Datos de transacciones
montos = np.random.randint(5000, 100000, 20)  # Montos de compra en CLP

# --------------------------------------------------
# Operaciones matemáticas básicas
# --------------------------------------------------
total_monto = np.sum(montos)
promedio_monto = np.mean(montos)
cantidad_transacciones = montos.size

print("Total de ventas:", total_monto)
print("Venta promedio:", promedio_monto)
print("Cantidad de transacciones:", cantidad_transacciones)

# --------------------------------------------------
# Almacenamiento de datos para uso posterior en Pandas
# --------------------------------------------------
np.save("data/1_clientes_id.npy", clientes_id)
np.save("data/1_edades.npy", edades)
np.save("data/1_montos.npy", montos)

# --------------------------------------------------
# Justificación del uso de NumPy
# --------------------------------------------------
"""
NumPy es utilizado para la generación y manipulación inicial de los datos
debido a su alta eficiencia en operaciones numéricas. El uso de arrays
homogéneos y operaciones vectorizadas permite realizar cálculos de manera
rápida y con bajo consumo de memoria, lo que resulta especialmente útil
cuando se trabaja con grandes volúmenes de datos.

---------------------------------------------------------------------------

*clientes_id.npy: Contiene un arreglo NumPy con los identificadores únicos de 
cada cliente.

*edades.npy: Almacena las edades asociadas a cada cliente, utilizadas posteriormente
para análisis descriptivo y segmentación.

*montos.npy: Guarda los montos de las transacciones realizadas por los clientes, 
los cuales serán utilizados para cálculos financieros, limpieza de datos y creación 
de variables derivadas.

Estos archivos permiten separar la generación de datos del análisis, facilitando la 
reutilización de la información en las siguientes lecciones mediante Pandas.
"""
