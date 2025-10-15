# OT - Detección de Objetos VIS–NIR en Colombia  
**Sistema de visión multiespectral para observación terrestre con técnicas de inteligencia artificial**

---

Este repositorio contiene el desarrollo de un sistema de detección de objetos basado en imágenes multiespectrales (VIS y NIR), enfocado en el análisis de **observación terrestre (OT)** en regiones de Colombia.  
Se emplean técnicas de **visión por computador e inteligencia artificial**, especialmente arquitecturas de redes neuronales.  

El estudio aborda la **composición espectral en múltiples bandas** para objetos puntuales, considerando su posible discriminación como una **distribución probabilística** derivada de un **análisis frecuencial**.

<p align="center">
  <img width="532" height="402" alt="image" src="https://github.com/user-attachments/assets/5c145a31-fe28-4dcc-ad61-4f23480c83a9" />
</p>

---

## 🧩 Etapa 1 – Revisión del estado del arte  

Se realizó un estudio físico y computacional de las bases del problema, utilizando los **coeficientes de Fresnel** y su relación con el **índice de reflexión** e **intensidad asociada** de cada material.  
Esto permitió comprender la naturaleza **estocástica y determinista** de la obtención de imágenes digitales.

**Bibliografía consultada:**  
- *Digital Image Processing Using MATLAB*

---

## 🛰️ Etapa 2 – Exploración del espacio N-dimensional conformado por imágenes multibanda  

Se exploraron diversos datasets de clasificación y segmentación de objetos.  
Bajo criterios de **resolución espacial**, **bandas espectrales**, **calidad de anotaciones** y **relevancia temática**, se seleccionaron los siguientes conjuntos:

### 📘 Dataset VEDAI  

- **Nombre:** Vehicle Detection in Aerial Imagery (VEDAI)  
- **Descripción:** Ortofotografías aéreas de Utah (EE. UU.) con resolución de 12,5 cm/píxel.  
- **Espectros:** RGB y NIR  
- **Tamaño de tiles:** 1024×1024 px  
- **Anotaciones:** Bounding boxes en más de 1.200 vehículos, incluyendo automóviles, furgonetas, camiones, pickups y autobuses.  
- **Aplicación:** Detección de objetos en imágenes aéreas de alta resolución.

### 📗 Dataset MBRSC (Humans in the Loop)  

- **Origen:** Mohammed Bin Rashid Space Center (Dubái)  
- **Etiquetado:** Segmentación semántica *pixel-wise* con 6 clases: edificios, tierra, carreteras, vegetación, agua y no etiquetado.  
- **Tamaño:** 72 imágenes agrupadas en 6 tiles principales.  
- **Anotaciones:** Realizadas por la *Roia Foundation* (Siria).  
- **Uso:** Análisis de cobertura terrestre.

---

## 🔬 Etapa 3 – Estudio multiespectral de datasets seleccionados (`data_exploration`)  

En la carpeta `data_exploration` se estudió cada dataset, sus anotaciones y representaciones de etiquetas.  
Los resultados y conclusiones se almacenan en la carpeta `relevant_outputs`.

---

### 🗺️ Data_Exploration_land_cover.py  

Se generó un **histograma general** de todas las imágenes, analizando la densidad de probabilidad de cada canal.

<p align="center">
  <img width="768" height="317" src="https://github.com/user-attachments/assets/94ed75d3-7add-4d68-9a44-8340621699c6" />
</p>

> Los valores saturados (252–255) y los muy bajos (0–4) no fueron filtrados, ya que suelen indicar ruido o información no definida.

Se visualizó la forma de etiquetado:

<p align="center">
  <img width="950" height="384" src="https://github.com/user-attachments/assets/c0ee7ce1-112b-48ac-a5d1-af6313ed2bfc" />
</p>

Y la segmentación semántica de clases:

<p align="center">
  <img width="1000" height="600" src="https://github.com/user-attachments/assets/137ec71c-5870-47c1-b298-268d32c46e57" />
</p>

Finalmente, se generaron **máscaras por clase** para analizar la densidad de probabilidad específica de cada una:

<p align="center">
  <img width="450" height="250" src="https://github.com/user-attachments/assets/897ede3f-5573-47d4-b5a5-524ce81878b8" />
  <img width="450" height="250" src="https://github.com/user-attachments/assets/e8d90ddb-55c9-42a7-b812-0df140fbe2b5" />
  <img width="450" height="250" src="https://github.com/user-attachments/assets/1992ba7c-f4cd-4267-ad59-536287286e06" />
</p>

---

### 🚗 Data_Exploration_object_detection  

Se analizó la estructura del dataset y su anotación.  
Posteriormente, se generó un **histograma acumulado** de las primeras 1000 imágenes RGB y NIR:

<p align="center">
  <img width="768" height="316" src="https://github.com/user-attachments/assets/a853a60d-d07b-4261-9122-db69f8c24068" />
  <img width="636" height="350" src="https://github.com/user-attachments/assets/b8b9769a-b8dc-4bf7-9ea9-531b37abc94d" />
</p>


**Formato de anotación:**
- 554 605 607 558 1004 996 1016 1021
- (x1, x2, x3, x4, y1, y2, y3, y4)


<p align="center">
  <img width="481" height="504" src="https://github.com/user-attachments/assets/03d258b8-a8dd-431c-862d-bd17c1bd380f" />
</p>

Se visualizaron las *bounding boxes* y las máscaras correspondientes:

<p align="center">
  <img width="515" height="276" src="https://github.com/user-attachments/assets/7c954d74-964e-4b27-9914-41d6658467cd" />
</p>

Luego, se generaron las **densidades de probabilidad por clase**:

<p align="center">
  <img width="990" height="1490" src="https://github.com/user-attachments/assets/d7c36ddd-aded-4049-b8a9-2beb98a2dbc2" />
</p>

---

## 🌱 Etapa 4 – Comparación con datos propios (Queen-Bee)  

Se replicó el proceso anterior sobre datos **NIR propios** del módulo Queen-Bee, comparándolos con los del dataset VEDAI.  
Se obtuvieron las siguientes **densidades de probabilidad normalizadas**:

<p align="center">
  <img width="1189" height="990" src="https://github.com/user-attachments/assets/4dd2c8d2-6d92-49d8-9381-9f697f438b73" />
</p>

### 📈 Métricas de comparación  

#### Correlación de Pearson  
Métrica estadística que mide la relación lineal entre dos variables:  
- **+1:** correlación positiva perfecta  
- **–1:** correlación negativa perfecta  
- **0:** sin correlación  

#### Chi-cuadrado  
Métrica que compara dos distribuciones de frecuencia y cuantifica su grado de similitud.  

<p align="center">
  <img width="631" height="165" src="https://github.com/user-attachments/assets/bbfa3f92-a795-4ca2-8ad8-19636ba71a67" />
</p>

---

## 🧠 Etapa 5 – Conformación del conjunto de datos final  

Tras analizar los datos extraídos de Queen-Bee, se definieron dos conjuntos de datos.  
El **conjunto L1** será el utilizado para el desarrollo del modelo de IA para reconocimiento de objetos.

<p align="center">
  <img width="611" height="541" src="https://github.com/user-attachments/assets/2898d412-d39e-4768-9670-a91536854d42" />
</p>

---

## 📊 Etapa 6 – Evaluación y validación con datos QBee  
**Estado:** No iniciado.

---

## 🧾 Etapa 7 – Análisis de resultados y redacción técnica  
**Estado:** No iniciado.

---

## 🔎 Entrada (2 imágenes)  

El sistema trabaja con dos imágenes:  
- **VIS:** rango 400–700 nm  
- **NIR:** rango 825–875 nm  

<p align="center">
  <img width="636" height="350" src="https://github.com/user-attachments/assets/f0eefd3b-2d63-487e-ad4c-a4c8cc2b6d68" />
</p>

---

## 💬 Autor  

**Juan Ángel**  
Ingeniero Físico | Especialización en Ciencia de Datos  
Proyecto Avanzado 1 – 2025  


**Formato de anotación:**  
