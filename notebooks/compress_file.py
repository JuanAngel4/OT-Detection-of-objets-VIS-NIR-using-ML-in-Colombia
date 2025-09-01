import zipfile
import os

# Carpeta que quieres comprimir
folder_to_zip = r"xview_correct_format_data"

# Ruta de salida del ZIP
zip_path = r"data\xview folder"

# Crear el ZIP
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(folder_to_zip):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, folder_to_zip)  # Relativo a la carpeta base
            zipf.write(file_path, arcname)

print(f"✅ ZIP creado en: {zip_path}")
