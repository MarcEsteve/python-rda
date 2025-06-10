import os
os.system("cls") # Windows


# Definir la carpeta donde se guardarán los archivos
carpeta = "04_tareas_rep/archivos"

# Crear la carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Lista de nombres de archivos a crear
archivos = [
    "reporte_ventas_enero.txt",
    "analisis_datos_2025.txt",
    "proyecto_final_v1.txt",
    "documento_informe.txt",
    "resumen_reunion.txt"
]

# Crear los archivos dentro de la carpeta
for archivo in archivos:
    with open(os.path.join(carpeta, archivo), "w") as f:
        f.write("Contenido de prueba\n")

print("✅ Archivos creados en la carpeta 'archivos'.")
