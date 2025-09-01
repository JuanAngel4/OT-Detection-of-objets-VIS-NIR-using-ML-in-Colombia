import json
import os

# Rutas de entrada y salida
geojson_path = r"data\xVIEW\train_labels\xView_train.geojson" #entrada de mi archivo original de xVIEW
output_dir = r"correct format data\labels" # salida en mi carpeta de outputs\lo borre para no generar mas y mas datos

os.makedirs(output_dir, exist_ok=True)

# Clases xView filtradas (27 clases clave)
xview_classes = {
    17: "passenger vehicle",
    18: "small car",
    19: "bus",
    20: "pickup truck",
    21: "cargo truck",
    23: "truck tractor",
    24: "trailer",
    26: "armored vehicle",
    27: "tank",
    29: "motorcycle",
    32: "ship",
    33: "fishing vessel",
    36: "yacht",
    38: "container ship",
    39: "oil tanker",
    40: "train",
    46: "building",
    47: "factory",
    48: "house",
    50: "school",
    51: "hospital",
    56: "runway",
    61: "bridge",
    66: "harbor",
    68: "wind turbine",
    69: "solar panel",
    70: "water tower",
    71: "oil tank"
}

# Lista de IDs válidos y ordenados
class_ids = list(xview_classes.keys())

# Cargar GeoJSON
with open(geojson_path) as f:
    data = json.load(f)

# Procesar cada feature
for feature in data["features"]:
    props = feature["properties"]
    image_id = props["image_id"]
    coords_str = props["bounds_imcoords"]
    type_id = props["type_id"]

    # Saltar anotaciones vacías
    if coords_str == "EMPTY":
        continue

    # Saltar clases que no estén en nuestra lista filtrada
    if type_id not in class_ids:
        continue

    # Convertir coordenadas a float
    coords = list(map(float, coords_str.split(",")))
    xmin, ymin, xmax, ymax = coords

    # Normalizar coordenadas para YOLO (imágenes de 1024x1024 px en xView)
    img_w, img_h = 1024, 1024
    x_center = (xmin + xmax) / 2 / img_w
    y_center = (ymin + ymax) / 2 / img_h
    w = (xmax - xmin) / img_w
    h = (ymax - ymin) / img_h

    # Obtener índice YOLO (0 a 26)
    class_index = class_ids.index(type_id)

    # Guardar etiqueta en formato YOLO
    label_path = os.path.join(output_dir, f"{image_id}.txt")
    with open(label_path, "a") as lf:
        lf.write(f"{class_index} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

print(f"✅ Conversión completada. Etiquetas YOLO guardadas en: {output_dir}")

# Generar archivo de clases en el orden correcto
# Ruta donde quieres guardar el archivo de clases
classes_dir = r"correct format data"
os.makedirs(classes_dir, exist_ok=True)

# Generar archivo de clases en el orden correcto
classes_txt_path = os.path.join(classes_dir, "classes.txt")
with open(classes_txt_path, "w") as cf:
    for cid in class_ids:
        cf.write(f"{xview_classes[cid]}\n")

print(f"✅ Archivo de clases generado en: {classes_txt_path}")
