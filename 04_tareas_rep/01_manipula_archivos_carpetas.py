import os
from datetime import datetime

# Limpiar pantalla (opcional)
os.system('cls')

# Ruta de la carpeta que contiene los archivos a renombrar
ruta_carpeta = '04_tareas_rep/archivos'

# Verificar que la carpeta existe
if not os.path.exists(ruta_carpeta):
    print("❌ La carpeta no existe. Asegúrate de ejecutar primero 'crear_archivos.py'.")
    exit()

# Iterar sobre cada archivo en la carpeta
for nombre_archivo in os.listdir(ruta_carpeta):
    ruta_original = os.path.join(ruta_carpeta, nombre_archivo)
    
    # Verificar si es un archivo (no una carpeta)
    if os.path.isfile(ruta_original):
        # Obtener la fecha de modificación del archivo
        timestamp_modificacion = os.path.getmtime(ruta_original)
        fecha_modificacion = datetime.fromtimestamp(timestamp_modificacion)
        
        # Formatear la fecha de modificación según 'YYYYMMDD_HHMMSS'
        fecha_formateada = fecha_modificacion.strftime('%Y%m%d_%H%M%S')

        # Obtener la extensión del archivo
        nombre, extension = os.path.splitext(nombre_archivo)

        # Generar un nuevo nombre de archivo
        nuevo_nombre = f"informe_proyecto_{fecha_formateada}{extension}"
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

        # Verificar si el archivo ya existe y agregar un sufijo incremental
        contador = 1
        while os.path.exists(ruta_nueva):
            nuevo_nombre = f"informe_proyecto_{fecha_formateada}_{contador}{extension}"
            ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)
            contador += 1

        # Renombrar el archivo
        os.rename(ruta_original, ruta_nueva)

print("✅ Archivos renombrados correctamente en la carpeta 'archivos'.")
