# 🍫 Proyecto: Análisis Exploratorio de Datos para Decisiones Comerciales

## 📌 Descripción del Proyecto

Este proyecto tiene como objetivo aplicar técnicas de **Análisis Exploratorio de Datos (EDA)** sobre un dataset real de ventas de chocolates, con el fin de identificar patrones, relaciones y oportunidades estratégicas para mejorar la toma de decisiones comerciales.

El análisis fue desarrollado en Python utilizando las librerías:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels

---

## 🎯 Objetivos

- Explorar y limpiar el dataset.
- Identificar variables cuantitativas y categóricas.
- Detectar valores faltantes e inconsistencias.
- Calcular estadísticos descriptivos.
- Identificar valores atípicos.
- Construir visualizaciones avanzadas.
- Aplicar un modelo de regresión lineal.
- Generar conclusiones estratégicas basadas en datos.

---


---

## 🧹 1. Limpieza y Preparación de Datos

- Conversión de la variable `Amount` de string a tipo numérico.
- Conversión de la variable `Date` a formato datetime.
- Revisión de valores nulos y duplicados.
- Validación de consistencia en las variables categóricas.

---

## 📊 2. Estadística Descriptiva

Se calcularon:

- Media
- Mediana
- Moda
- Varianza
- Desviación estándar
- Cuartiles y percentiles

Se identificó que la distribución de ventas presenta asimetría positiva y presencia de valores atípicos.

---

## 📈 3. Visualizaciones

Se construyeron:

- Histogramas
- Boxplots
- Pairplots
- Violinplots
- Jointplots
- Heatmaps
- FacetGrid segmentado por país

Las visualizaciones permitieron detectar:

- Alta dispersión en los montos de venta.
- Diferencias en comportamiento por país.
- Ausencia de correlación significativa entre cajas enviadas y monto total.

---

## 📉 4. Modelamiento

Se aplicó un modelo de **Regresión Lineal** utilizando `statsmodels`.

Métricas evaluadas:
- R²
- MSE
- MAE
- Significancia estadística (p-values)

Resultados principales:
- No se encontró relación lineal significativa entre volumen de cajas enviadas y monto total de ventas.
- Se sugiere que el precio unitario y el tipo de producto influyen más en los ingresos.

---

## 💡 5. Principales Insights

- El volumen de cajas no explica el monto total de ventas.
- Existen diferencias comerciales por país.
- Algunos productos generan mayores ingresos con menor volumen.
- Se recomienda segmentar estrategias por mercado y tipo de producto.

---

## 🛠️ Tecnologías Utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Google Colab / VS Code


---

## 📌 Conclusión

Este proyecto demuestra la aplicación práctica de técnicas de análisis exploratorio y modelamiento estadístico para transformar datos comerciales en información estratégica útil para la toma de decisiones.