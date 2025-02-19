from pdf2image import convert_from_path  # Extrae imágenes del PDF (usa Poppler)
import pytesseract  # Aplica OCR (usa Tesseract)
import os


os.system("pip install pytesseract pdf2image")  # Instalar las librerías necesarias
os.system("cls")  # Limpiar la consola

# 📌 Configuración de rutas
ruta_pdf = "C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/quijote-imagen-ocr.pdf"
ruta_poppler = r"C:/Program Files/poppler-24.08.0/Library/bin"   # Asegúrate de actualizar esta ruta con la correcta

# Convertir PDF a imágenes (usa Poppler)
imagenes = convert_from_path(ruta_pdf, poppler_path=ruta_poppler)

# Crear una carpeta temporal para guardar imágenes
os.makedirs("imagenes_temp", exist_ok=True)

texto_extraido = ""

# Iterar sobre las imágenes y aplicar OCR
for i, imagen in enumerate(imagenes):
    ruta_imagen = f"imagenes_temp/pagina_{i + 1}.png"
    imagen.save(ruta_imagen, "PNG")  # Guardar imagen temporalmente
    
    # Aplicar OCR con Tesseract
    texto = pytesseract.image_to_string(imagen, lang="eng")  # OCR en inglés
    texto_extraido += f"\n--- Página {i + 1} ---\n" + texto

# 📌 Guardar el texto extraído en un archivo
with open("texto_extraido.txt", "w", encoding="utf-8") as f:
    f.write(texto_extraido)

print("✅ Extracción de texto completada. Revisa el archivo 'texto_extraido.txt'.")

# 📌 Mostrar el texto extraído
# import os
print("Directorio actual:", os.getcwd())  # Muestra dónde se está ejecutando el script en nuestro caso desde Jupyter Notebook