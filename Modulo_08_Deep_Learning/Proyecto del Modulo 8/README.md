# 👕 Clasificador Inteligente de Imágenes de Ropa (Deep Learning)

## 📌 Descripción del proyecto
Este proyecto consiste en el desarrollo de un modelo de **Deep Learning** capaz de clasificar automáticamente imágenes de prendas de vestir en distintas categorías.

Fue desarrollado como parte del módulo **Fundamentos de Deep Learning**, con el objetivo de automatizar la categorización de productos en una tienda e-commerce, mejorando la eficiencia y reduciendo errores humanos.

---

## 🎯 Objetivos
- Diseñar e implementar una red neuronal densa.
- Implementar una red neuronal convolutiva (CNN).
- Comparar el rendimiento entre ambos modelos.
- Aplicar técnicas de optimización y regularización.
- Generar predicciones sobre nuevas imágenes.

---

## 📊 Dataset
Se utilizó el dataset **Fashion-MNIST**, que contiene:

- 70.000 imágenes en escala de grises
- Tamaño: 28x28 píxeles
- 10 categorías de ropa (camisetas, pantalones, zapatillas, etc.)

---

## 🧠 Modelos implementados

### 🔹 1. Red Neuronal Densa (ANN)
- Capa Flatten
- Capa densa (128 neuronas, ReLU)
- Dropout (0.3)
- Capa de salida (Softmax)

### 🔹 2. Red Neuronal Convolutiva (CNN)
- Capas Conv2D (32 y 64 filtros)
- MaxPooling
- Capa Flatten
- Capa densa (128 neuronas)
- Dropout (0.3)
- Capa de salida (Softmax)

---

## ⚙️ Tecnologías utilizadas
- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Google Colab

---

## 📈 Resultados

| Modelo | Accuracy aproximado |
|--------|------------------|
| Red Densa | ~88% |
| CNN | ~92% - 94% |

👉 La CNN logró mejor rendimiento debido a su capacidad para extraer características espaciales de las imágenes.

---

## 🔧 Técnicas aplicadas

- ✔ Normalización de datos
- ✔ Optimización con Adam
- ✔ Regularización con Dropout
- ✔ Ajuste de hiperparámetros
- ✔ Validación con conjunto de validación

---

## 🖼️ Ejemplo de predicción

El modelo es capaz de predecir correctamente la categoría de nuevas imágenes, mostrando resultados visuales junto con la etiqueta predicha.

---

## 📁 Estructura del proyecto
