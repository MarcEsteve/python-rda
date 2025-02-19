from pdf2image import convert_from_path

import os
print(os.path.exists('C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/quijote-imagen-ocr.pdf'))  # Debe devolver True si el archivo existe


ruta_poppler = r"C:/Program Files/poppler-24.08.0/Library/bin"  # Ajusta según la versión descargada



imagenes = convert_from_path(r"C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/quijote-imagen-ocr.pdf", poppler_path=ruta_poppler)

#pip install pytesseract pdf2image pillow

import pytesseract
from pdf2image import convert_from_path

print(pytesseract.get_tesseract_version())  # Debe mostrar la versión de Tesseract
print(convert_from_path)