import PyPDF2  # pip install PyPDF2

# Ruta del archivo PDF
rutaPDF = "C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/tecnologias_emergentes.pdf"

# Abrir el archivo en modo binario
with open(rutaPDF, "rb") as pdfFile:
    lector = PyPDF2.PdfReader(pdfFile)  # Usa PdfReader en lugar de PdfFileReader
    
    # Número de páginas del PDF
    num_paginas = len(lector.pages)
    print(f"El PDF tiene {num_paginas} páginas.\n")

    # Leer el contenido de la primera página
    pagina = lector.pages[0]  # Acceder a la primera página (índice 0)
    texto = pagina.extract_text()
    print("Texto extraído de la primera página:")
    print(texto)

# Abrir el archivo en modo binario y mantenerlo abierto durante toda la lectura
with open(rutaPDF, "rb") as pdfFile:
    lector = PyPDF2.PdfReader(pdfFile)  # Usa PdfReader en lugar de PdfFileReader
    
    # Número de páginas del PDF
    num_paginas = len(lector.pages)
    print(f"El PDF tiene {num_paginas} páginas.\n")

    # Iteramos la lectura del PDF página por página
    for i in range(num_paginas):
        pagina = lector.pages[i]  # Acceder a cada página
        texto = pagina.extract_text()  # Extraer el texto de la página
        
        print(f"\nTexto extraído de la página {i + 1}:")
        print(texto if texto else "⚠ No se pudo extraer texto de esta página.")
