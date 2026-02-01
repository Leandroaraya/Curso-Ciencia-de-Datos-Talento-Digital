# 📊 Proyecto: Preparación y Análisis de Datos con Python

Este proyecto corresponde al desarrollo completo del flujo de **obtención, limpieza, transformación y análisis de datos**, aplicando librerías fundamentales del ecosistema Python como **NumPy y Pandas**.

El trabajo se organiza en seis lecciones progresivas, donde se simula un escenario de datos de clientes y transacciones de un e-commerce, abordando problemas reales como datos erróneos, valores nulos, outliers, integración de fuentes y análisis agregado.

---

## 🎯 Objetivo general

Aplicar técnicas de **Data Preparation, Data Wrangling, Agrupamiento y Pivoteo** para transformar datos crudos en un dataset final limpio, estructurado y listo para análisis.

---

## 🧰 Tecnologías utilizadas

* Python 3.x
* NumPy
* Pandas
* Jupyter Notebook
* Excel / CSV

---

## 🗂️ Estructura del proyecto

```text
proyecto_preparacion_datos/
│
├── leccion_1_numpy.ipynb
├── leccion_2_pandas.ipynb
├── leccion_3_integracion_datos.ipynb
├── leccion_4_limpieza_outliers.ipynb
├── leccion_5_data_wrangling.ipynb
├── leccion_6_agrupamiento_pivoteo.ipynb
│
├── data/
│   ├── clientes.npy
│   ├── edades.npy
│   ├── montos.npy
│   ├── clientes_preliminar.csv
│   ├── info_clientes.xlsx
│   ├── dataset_unificado.csv
│   ├── dataset_unificado2.csv
│   ├── df_wrangling.csv
│   ├── dataset_final_ecommerce.csv
│   └── dataset_final_ecommerce.xlsx
│
└── README.md
```

---

## 📘 Descripción por lección

### 🔹 Lección 1 – NumPy

* Generación de datos ficticios de clientes y transacciones.
* Operaciones matemáticas vectorizadas.
* Persistencia de datos en archivos `.npy`.

### 🔹 Lección 2 – Pandas (Exploración inicial)

* Carga de datos NumPy en DataFrame.
* Exploración con `head()`, `tail()`, `describe()`.
* Aplicación de filtros condicionales.
* Exportación a CSV.

### 🔹 Lección 3 – Integración de datos

* Creación de fuente externa en Excel.
* Integración de datos mediante `merge()`.

### 🔹 Lección 4 – Limpieza y calidad de datos

* Introducción y detección de errores intencionales.
* Identificación de valores nulos.
* Validación de rangos lógicos (edad).
* Tratamiento de outliers con método IQR.
* Imputación de valores faltantes.

### 🔹 Lección 5 – Data Wrangling

* Eliminación de registros duplicados.
* Transformación de tipos de datos.
* Creación de nuevas variables:

  * IVA
  * Total con IVA
  * Nivel de compra

### 🔹 Lección 6 – Agrupamiento y pivoteo

* Análisis agregado con `groupby()`.
* Tablas dinámicas con `pivot()`.
* Reestructuración con `melt()`.
* Integración de nuevas fuentes (`merge()`).
* Simulación de nuevos registros (`concat()`).
* Exportación final en CSV y Excel.

---

## 📈 Resultado final

El proyecto culmina con un **dataset final optimizado**, enriquecido y estructurado, listo para:

* Análisis exploratorio
* Visualización
* Modelos de Machine Learning

---


## 📌 Notas

Este proyecto tiene fines educativos y simula un escenario real de preparación de datos en un entorno de análisis de datos.
