import glob
import os
import PyPDF2  # Asegúrate de instalarlo con pip install PyPDF2

# 📌 Obtener la lista de archivos PDF en la carpeta de Inputs
ruta_inputs = "C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/05_xlsx_docx_pdf/Inputs"
lista_ficheros_pdf = glob.glob(os.path.join(ruta_inputs, "*.pdf"))  # Lista con los nombres de los PDFs en la carpeta Inputs

# 📌 Extraer solo los nombres de los archivos sin la ruta completa
lista_ficheros_pdf = [os.path.basename(fichero) for fichero in lista_ficheros_pdf]

# Lista donde almacenaremos los proveedores extraídos de cada PDF
lista_proveedor = []

# 📌 Procesar cada PDF para extraer el proveedor
for fichero in lista_ficheros_pdf:
    ruta_pdf = os.path.join(ruta_inputs, fichero)  # Ruta completa del PDF
    
    with open(ruta_pdf, 'rb') as pdfFile:
        lector = PyPDF2.PdfReader(pdfFile)  # Crear el lector del PDF
        
        if len(lector.pages) > 0:  # Verificar que el PDF no esté vacío
            pag = lector.pages[0]  # Obtener la primera página
            texto_pagina = pag.extract_text()  # Extraer el texto de la página
            
            if texto_pagina:
                lineas = texto_pagina.split('\n')  # Dividir el texto en líneas
                proveedor_factura = lineas[0].strip() if lineas else "No se pudo extraer texto"
            else:
                proveedor_factura = "No se pudo extraer texto"
        else:
            proveedor_factura = "PDF vacío"
    
    lista_proveedor.append(proveedor_factura.replace(" Fecha", ""))  # Eliminar la palabra "Fecha" si está presente

# 📌 Crear un diccionario que asocia el nombre del PDF con el proveedor extraído
diccionario_factura_proveedor = dict(zip(lista_ficheros_pdf, lista_proveedor))

# 📌 Mostrar el resultado
print("Diccionario de facturas y proveedores:")
for factura, proveedor in diccionario_factura_proveedor.items():
    print(f"{factura}: {proveedor}")
