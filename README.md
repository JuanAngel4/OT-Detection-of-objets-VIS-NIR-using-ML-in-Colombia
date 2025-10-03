# OT-Deteccion-de-objetos-VIS-NIR-ML-Colombia
Este repositorio contiene el desarrollo de un sistema de detección de objetos basado en imágenes multiespectrales (VIS y NIR), enfocado en el análisis de observación terrestre (OT) en regiones de Colombia. Se emplean técnicas de visión por computadora e inteligencia artificial, especialmente arquitecturas de redes neuronales.
Se estudio la composicion espectral en multiples bandas para objetos puntuales, entendiendo su posible discriminacion como una distribucion probabilistica a su vez de un analisis frecuencial.

## ETAPA 1 - REVISION DEL ESTADO DEL ARTE
Se estudio, desde un punto de vista fisico y computacional, las bases que se pueden llevar a cabo, utilizando principalmente la fisica explicada por los coeficientes de fresnel a su vez su relacion con el indice de reflexion de cada material y su intenisada asociada, lo cual se relaciona con la naturaleza de la obtencion de imagenes digitales que poseen parte estocastica y determinista.
Libros consultados:  - Digital Image Processing Using MATLAB

## ETAPA 2 - EXPLORACION DEL ESPACIO N-DIMENSIONAL CONFORMADOS POR LAS IMAGENES EN MULTIPLES BANDAS
- Se exploraron multiples opciones de dataset para clasificacion de objetos y uno de segmentacion de instancias, sin embargo, bajo criterios de mayor resolucion espacial, bandas espectrales de interes, imagenes correctamente etiquetadas, entre otras caracteristicas de interes se termino eligiendo:
El dataset VEDAI (Vehicle Detection in Aerial Imagery) está compuesto por ortofotos aéreas tomadas en Utah (EE. UU.) desde avión, con resolución espacial de 12,5 cm/px. Las imágenes están disponibles tanto en espectro RGB como en infrarrojo cercano (NIR), y se encuentran organizadas en tiles de 1024×1024 píxeles. El conjunto incluye más de 1.200 vehículos anotados mediante bounding boxes, distribuidos en distintas categorías como automóviles, furgonetas, camiones, pick-ups y autobuses, lo que lo convierte en un recurso de alta calidad para tareas de detección de objetos en imágenes aéreas de muy alta resolución.
- El dataset publicado por Humans in the Loop en colaboración con el Mohammed Bin Rashid Space Center (MBRSC) consiste en imágenes aéreas de Dubái obtenidas por satélites del MBRSC y anotadas con segmentación semántica pixel-wise en 6 clases: edificios, tierra sin pavimentar, carreteras, vegetación, agua y no etiquetado. El conjunto contiene un total de 72 imágenes agrupadas en 6 tiles principales, con codificación de colores para cada clase. Las anotaciones fueron realizadas por los aprendices de la Roia Foundation en Siria, en el marco de un proyecto abierto y de acceso libre.

## ETAPA 3 -   Estudio multiespectral de datasets seleccionados para cobertura terrestre y objetos.(data_exploration)
En la carpeta "data_exploration" se llevo a cabo el estudio independiente de cada dataset y su contenido, ademas de exponer su forma de anotacion, mas una detallada representacion de sus etiquetas para cada caso, cada estudio independiente se llevo a cabo en las sub-carpetas "Data_Exploration_land_cover.py" y "Data_Exploration_object_detection".
A continuacion se mostraran resultados obtenidos para cada caso, ademas de exponer las conclusiones para cada caso.todas las imagenes presentadas a partir de esta seccion estarán en la carpeta "relevant_outputs".
### Data_Exploration_land_cover.py
Primeramente, se expone un historgama general de todas las imagenes a trabajar, de esta manera se puede entender el aporte de intensidades sobre la densidad de probabilidad de cada canal.
<img width="768" height="317" alt="image" src="https://github.com/user-attachments/assets/94ed75d3-7add-4d68-9a44-8340621699c6" />

Es importante mencionar que, para la imagen anterior, no fue realizado un filtro de las intensidades que indican saturacion, es decir, el rango 252-255,y tambien los valores en 0-4, que usualmente indican ruido o informacion no definida.
Ahora bien, se indico la forma de etiquetado:

<img width="950" height="384" alt="image" src="https://github.com/user-attachments/assets/c0ee7ce1-112b-48ac-a5d1-af6313ed2bfc" />

Tambien se indico cada clase de una imagen para vizualizacion de la segmentacion semantica de las clases en el dataset.

<img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/137ec71c-5870-47c1-b298-268d32c46e57" />

Por ultimo, se discrimino cada clase en marcaras que solo contengan informacion de la clase visualizada con el fin de predecir la densidad de probabilidad de cada clase en especifico.

<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/897ede3f-5573-47d4-b5a5-524ce81878b8" />
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/e8d90ddb-55c9-42a7-b812-0df140fbe2b5" />
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/1992ba7c-f4cd-4267-ad59-536287286e06" />
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/d91bb13b-b8ad-41a7-bf4a-937efb2807e1" />
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/1713c1b5-a724-4964-a16d-205543eecde2" />
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/20db424c-c889-4a4d-8b04-146ce58ae83d" />



### Data_Exploration_object_detection
## ETAPA 4 - Diseño e implementación del modelo IA
En Desarrollo.
## ETAPA 5 - Evaluación y validación con datos QBee
No iniciado.
## ETAPA 6 - Análisis de resultados y redacción técnica
No iniciado.
# Entrada (2 imagenes)
Dos imagenes, una en el espectro visible y otra en el infrarojo cercano.
Idealmente VIS:400–700 nm NIR: 825–875 nm
<img width="636" height="350" alt="image" src="https://github.com/user-attachments/assets/f0eefd3b-2d63-487e-ad4c-a4c8cc2b6d68" />

# Exploracion de datos - Para deteccion de objetos(carros,camionetas,vans,avionetas...)
Histograma general del dataset en RGB, histogramas puntuales segun clase.
<img width="768" height="316" alt="image" src="https://github.com/user-attachments/assets/a853a60d-d07b-4261-9122-db69f8c24068" />


