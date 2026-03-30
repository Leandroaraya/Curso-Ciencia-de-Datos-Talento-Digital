# Proyecto: Análisis estadístico de hábitos saludables en jóvenes universitarios

## Descripción del proyecto

Este proyecto aplica el **método científico** y técnicas de **estadística inferencial** para analizar los factores que influyen en los hábitos de sueño, alimentación y actividad física en estudiantes universitarios.  

Se utiliza un **dataset simulado de 150 estudiantes** que incluye variables como horas de sueño, nivel de estrés, horas de ejercicio, consumo de comida rápida y promedio académico. El objetivo es **identificar patrones, estimar parámetros poblacionales y realizar pruebas de hipótesis** para orientar decisiones de bienestar estudiantil.

---

## Objetivos

- Aplicar el **método científico completo**.
- Formular preguntas de investigación y establecer hipótesis.
- Simular un **dataset realista** de hábitos saludables.
- Analizar distribuciones de probabilidad y aplicar el **Teorema del Límite Central**.
- Calcular **intervalos de confianza** y realizar **test de significancia**.
- Documentar los resultados de manera clara y reproducible.

---

---

## Notebooks

### 01_metodo_cientifico.ipynb
- Definición del problema
- Hipótesis nula y alternativa
- Identificación de variables cuantitativas y cualitativas
- Diseño preliminar del estudio

### 02_probabilidad_muestreo.ipynb
- Espacio muestral
- Eventos aleatorios y representación mediante árbol de probabilidades
- Simulación de dataset (≥100 registros)
- Cálculo de probabilidades básicas, uniones, intersecciones y complementos

### 03_distribuciones_probabilidad.ipynb
- Identificación de distribuciones continuas y discretas
- Distribución normal, binomial y Poisson
- Cálculo de probabilidades y gráficos

### 04_teorema_limite_central.ipynb
- Generación de distribuciones muestrales
- Demostración empírica del **Teorema del Límite Central**
- Comparación distribución original vs media muestral
- Análisis de dispersión según tamaño de muestra

### 05_intervalos_confianza.ipynb
- Cálculo de **intervalos de confianza** para media de variables
- Comparación entre niveles de confianza 90%, 95% y 99%
- Efecto del tamaño de muestra sobre el ancho del intervalo
- Interpretación de resultados

### 06_test_significancia.ipynb
- Pruebas de hipótesis para medias y proporciones
- Cálculo de valor-p
- Comparación con nivel de significancia α
- Explicación de errores tipo I y II
- Conclusiones basadas en evidencia estadística

---

## Dataset

El dataset simulado contiene las siguientes variables:

| Variable | Tipo | Descripción |
|----------|------|-------------|
| edad | Cuantitativa | Edad del estudiante (18-29 años) |
| genero | Cualitativa | Masculino / Femenino |
| horas_sueno | Cuantitativa | Promedio de horas de sueño por noche |
| horas_ejercicio | Cuantitativa | Horas de ejercicio por semana |
| comida_rapida_semana | Cuantitativa | Cantidad de comidas rápidas por semana |
| estres | Cuantitativa | Nivel de estrés (1-10) |
| gpa | Cuantitativa | Promedio académico |
| duerme_bien | Binaria | 1 si horas_sueno ≥ 7, 0 si < 7 |

Archivo CSV: `data/raw/habitos_saludables_estudiantes.csv`

---

## Herramientas y librerías utilizadas

- Python 3.x  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- SciPy (estadística)  
- Jupyter Notebook

---

## Resultados y visualizaciones

- Histogramas y KDE de variables continuas
- Diagramas de dispersión y boxplots
- Distribuciones muestrales para demostrar TLC
- Intervalos de confianza y test de hipótesis
- Reporte reproducible de análisis estadístico completo


---