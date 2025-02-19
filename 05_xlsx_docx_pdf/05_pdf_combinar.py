import PyPDF2  # pip install PyPDF2

# Ruta del archivo PDF
rutaPDF1 = r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/tecnologias_emergentes.pdf'
rutaPDF2 = r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/otras_tecnologias_emergentes.pdf'

# Abrir el archivo en modo binario
pdf1FileObject = open(rutaPDF1, "rb")
pdf1Reader = PyPDF2.PdfReader(pdf1FileObject)
pdf2FileObject = open(rutaPDF2, "rb")
pdf2Reader = PyPDF2.PdfReader(pdf2FileObject)

# Crear un objeto escritor de PDF
pdfWriter = PyPDF2.PdfWriter()

# Iteramos la lectura del PDF página por página
for i in range(len(pdf1Reader.pages)):
    pagina = pdf1Reader.pages[i]  # Acceder a cada página
    pdfWriter.add_page(pagina)  # Añadir la página al objeto escritor

for i in range(len(pdf2Reader.pages)):
    pagina = pdf2Reader.pages[i]  # Acceder a cada página
    pdfWriter.add_page(pagina)  # Añadir la página al objeto escritor

fichero_salida = open(r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/tecnologias_combinadas.pdf', 'wb')
pdfWriter.write(fichero_salida)

fichero_salida.close()
pdf1FileObject.close()
pdf2FileObject.close()