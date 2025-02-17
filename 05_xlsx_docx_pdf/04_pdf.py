import PyPDF2 #Instalar previamente con pip install PyPDF2
pdfFile = open('.\Inputs\Factura proveedor 1.pdf','rb') #rb para especificar formato binario
lector = PyPDF2.PdfFileReader(pdfFile) #Creamos el objeto "lector" capaz de leer el fichero pdf cargado en pdfFile
lector.numPages #Número de páginas del pdf
pag = lector.getPage(0) #Cogemos la primero página del pdf, el índice 0 es la primera
pag.extractText() #Extraemos el texto de la página
indice_final = pag.extractText().find('\n') #Identificamos donde se encuentra el primer salto de línea puesto que hasta ahí llegaría el nombre del proveedor
proveedor_factura = pag.extractText()[0:indice_final] #Extraemos el nombre del proveedor
proveedor_factura