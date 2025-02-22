import os
import hashlib

# ruta_base = "C:\Program Files (x86)"

carpetas = os.listdir(ruta_base)

print("Carpetas encontradas:", carpetas)

for carpeta in carpetas:

    carpeta_actual = os.path.join(ruta_base, carpeta)

    if os.path.isdir(carpeta_actual):
        hashing = hashlib.md5(carpeta.encode("utf-8")).hexdigest()
        nueva_ruta = os.path.join(ruta_base, hashing)

        # Renombrar carpeta
        os.rename(carpeta_actual, nueva_ruta)
        print(f'Renombrado: {carpeta} -> {hashing}')