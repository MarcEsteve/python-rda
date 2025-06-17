from pypdf  import PdfReader, PdfWriter # pip install pypdf

# Ruta del archivo PDF
rutaPDF1 = r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/tecnologias_emergentes.pdf'
rutaPDF2 = r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/otras_tecnologias_emergentes.pdf'

# Abrimos los archivos de entrada manualmente en modo lectura binaria
pdf1File = open(rutaPDF1, 'rb') # Crea un objeto del primer pdf 
pdf2File = open(rutaPDF2, 'rb') # Crea un objeto del segundo pdf

reader1 = PdfReader(pdf1File) # Crea un objeto lector del primer pdf
reader2 = PdfReader(pdf2File) # Crea un objeto lector del segundo pdf
writer = PdfWriter() # Crea un objeto escritor del pdf

# Iteramos la lectura del PDF página por página
for i in range(len(reader1.pages)):
    pagina = reader1.pages[i]  # Acceder a cada página
    writer.add_page(pagina)  # Añadir la página al objeto escritor

for i in range(len(reader2.pages)):
    pagina = reader2.pages[i]  # Acceder a cada página
    writer.add_page(pagina)  # Añadir la página al objeto escritor

fichero_salida = open(r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/tecnologias_combinadas.pdf', 'wb')
writer.write(fichero_salida)

fichero_salida.close()
pdf1File.close()
pdf2File.close()