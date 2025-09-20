# OT-Deteccion-de-objetos-VIS-NIR-ML-Colombia
Este repositorio contiene el desarrollo de un sistema de detección de objetos basado en imágenes multiespectrales (VIS y NIR), enfocado en el análisis de observación terrestre (OT) en regiones de Colombia. Se emplean técnicas de visión por computadora e inteligencia artificial, especialmente arquitecturas de redes neuronales.
Se estudio la composicion espectral en multiples bandas para objetos puntuales, entendiendo su posible discriminacion como una distribucion probabilistica a su vez de un analisis frecuencial.
## ETAPA 1 - REVISION DEL ESTADO DEL ARTE
Se estudio, desde un punto de vista fisico y computacional, las bases que se pueden llevar a cabo, utilizando principalmente la fisica explicada por los coeficientes de fresnel a su vez su relacion con el indice de reflexion de cada material y su intenisada asociada, lo cual se relaciona con la naturaleza de la obtencion de imagenes digitales que poseen parte estocastica y determinista.
## ETAPA 2 - EXPLORACION DEL ESPACIO N-DIMENSIONAL CONFORMAOD POR LAS IMAGENES
- Se exploraron multiples opciones de dataset para clasificacion de objetos y uno de segmentacion de instancias, sin embargo, bajo criterios de mayor resolucion espacial, bandas espectrales de interes, imagenes correctamente etiquetadas, entre otras caracteristicas de interes se termino eligiendo:
El dataset VEDAI (Vehicle Detection in Aerial Imagery) está compuesto por ortofotos aéreas tomadas en Utah (EE. UU.) desde avión, con resolución espacial de 12,5 cm/px. Las imágenes están disponibles tanto en espectro RGB como en infrarrojo cercano (NIR), y se encuentran organizadas en tiles de 1024×1024 píxeles. El conjunto incluye más de 1.200 vehículos anotados mediante bounding boxes, distribuidos en distintas categorías como automóviles, furgonetas, camiones, pick-ups y autobuses, lo que lo convierte en un recurso de alta calidad para tareas de detección de objetos en imágenes aéreas de muy alta resolución.
- El dataset publicado por Humans in the Loop en colaboración con el Mohammed Bin Rashid Space Center (MBRSC) consiste en imágenes aéreas de Dubái obtenidas por satélites del MBRSC y anotadas con segmentación semántica pixel-wise en 6 clases: edificios, tierra sin pavimentar, carreteras, vegetación, agua y no etiquetado. El conjunto contiene un total de 72 imágenes agrupadas en 6 tiles principales, con codificación de colores para cada clase. Las anotaciones fueron realizadas por los aprendices de la Roia Foundation en Siria, en el marco de un proyecto abierto y de acceso libre.
# Entrada (2 imagenes)
Dos imagenes, una en el espectro visible y otra en el infrarojo cercano.
Idealmente VIS:400–700 nm NIR: 825–875 nm
<img width="636" height="350" alt="image" src="https://github.com/user-attachments/assets/f0eefd3b-2d63-487e-ad4c-a4c8cc2b6d68" />

# Exploracion de datos - Para deteccion de objetos(carros,camionetas,vans,avionetas...)
Histograma general del dataset en RGB, histogramas puntuales segun clase.
<img width="768" height="316" alt="image" src="https://github.com/user-attachments/assets/a853a60d-d07b-4261-9122-db69f8c24068" />


