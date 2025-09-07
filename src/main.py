import os
import random
import shutil

# 📍 Carpetas originales
train_images_dir = r"data\xview folder\xview_correct_format_data\images for training"
train_labels_dir = r"data\xview folder\xview_correct_format_data\labels"

# 📍 Carpetas de validación que vamos a crear
val_images_dir = r"data\xview folder\xview_correct_format_data\val images"
val_labels_dir = r"data\xview folder\xview_correct_format_data\val images"

os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 📍 Listar imágenes
all_images = [f for f in os.listdir(train_images_dir) if f.lower().endswith(('.jpg', '.png'))]

# Calcular cuántas irán a validación (10%)
val_count = max(1, int(len(all_images) * 0.1))
val_images = random.sample(all_images, val_count)

# 📍 Mover imágenes y etiquetas
for img_name in val_images:
    label_name = os.path.splitext(img_name)[0] + ".txt"

    # Mover imagen
    shutil.move(
        os.path.join(train_images_dir, img_name),
        os.path.join(val_images_dir, img_name)
    )

    # Mover etiqueta
    if os.path.exists(os.path.join(train_labels_dir, label_name)):
        shutil.move(
            os.path.join(train_labels_dir, label_name),
            os.path.join(val_labels_dir, label_name)
        )

print(f"✅ {val_count} imágenes movidas a validación.")

# 📍 Crear data.yaml
classes_file = r"data\xview folder\xview_correct_format_data\classes.txt"
with open(classes_file, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

yaml_content = f"""train: E:/MACHINE LEARNING/AVANZADO 1/VSFOLDER A1 PROYECT/dataset/images/train
val: E:/MACHINE LEARNING/AVANZADO 1/VSFOLDER A1 PROYECT/dataset/images/val

nc: {len(class_names)}
names:
"""

for name in class_names:
    yaml_content += f"  - {name}\n"

import os

# Definir ruta completa del archivo, no solo la carpeta
yaml_path = r"outputs/model_output/data.yaml"

# Crear carpeta si no existe
os.makedirs(os.path.dirname(yaml_path), exist_ok=True)

# Guardar contenido
with open(yaml_path, "w") as f:
    f.write(yaml_content)

print(f"✅ data.yaml guardado en: {yaml_path}")
