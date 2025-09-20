carpeta_entrada = r"E:\MACHINE LEARNING\AVANZADO 1\VSFOLDER A1 PROYECT\OT-Detecci-n-de-objetos-VIS-NIR-ML-Colombia\Own_Data_Exploration\Land cover\qbee_segmentation_data\images"
import os
from PIL import Image

# Ruta de salida para guardar las imágenes TIF
carpeta_salida = r"E:\MACHINE LEARNING\AVANZADO 1\VSFOLDER A1 PROYECT\OT-Detecci-n-de-objetos-VIS-NIR-ML-Colombia\Own_Data_Exploration\Land cover\qbee_segmentation_data\images_tif"

# Crear carpeta de salida si no existe
os.makedirs(carpeta_salida, exist_ok=True)

# Recorrer todos los archivos de la carpeta de entrada
for archivo in os.listdir(carpeta_entrada):
    if archivo.lower().endswith(".png"):
        ruta_png = os.path.join(carpeta_entrada, archivo)
        nombre_base = os.path.splitext(archivo)[0]
        ruta_tif = os.path.join(carpeta_salida, nombre_base + ".tif")

        # Abrir y convertir
        with Image.open(ruta_png) as img:
            img.save(ruta_tif, format="TIFF")

print("✅ Conversión completada.")
