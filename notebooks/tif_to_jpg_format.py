from PIL import Image
import os
from glob import glob

input_dir = r"data\xVIEW\val_images\val_images"
output_dir = r"data\xview folder\xview_correct_format_data\val images"
os.makedirs(output_dir, exist_ok=True)

for tif_path in glob(os.path.join(input_dir, "*.tif")):
    img = Image.open(tif_path)
    file_name = os.path.splitext(os.path.basename(tif_path))[0]
    jpg_path = os.path.join(output_dir, f"{file_name}.jpg")
    img.convert("RGB").save(jpg_path, "JPEG", quality=95)

print("✅ Conversión completada a JPG.")
