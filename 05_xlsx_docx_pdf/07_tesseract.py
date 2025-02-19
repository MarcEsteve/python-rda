import pytesseract # OCR tool "pip install pytesseract"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Verifica si está instalado correctamente ejecutando:
print(pytesseract.get_tesseract_version())
