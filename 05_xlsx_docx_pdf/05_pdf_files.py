import glob
import os
lista_ficheros_pdf = glob.glob(".\Inputs\*.pdf") #Lista con los nombres de los ficheros pdf en la carpeta Inputs
lista_ficheros_pdf
#Nos quedamos solo con los nombres del fichero pdf
lista_ficheros_pdf = list(map(lambda x: x.replace('.\\Inputs\\',''),lista_ficheros_pdf))
lista_ficheros_pdf
lista_proveedor = []

for fichero in lista_ficheros_pdf:
    pdfFile = open(os.path.join(".\Inputs",fichero),'rb')
    lector = PyPDF2.PdfFileReader(pdfFile)
    pag = lector.getPage(0)
    indice_final = pag.extractText().find('\n')
    proveedor_factura = pag.extractText()[0:indice_final]
    lista_proveedor.append(proveedor_factura)

lista_proveedor
diccionario_factura_proveedor = dict(zip(lista_ficheros_pdf, lista_proveedor))
diccionario_factura_proveedor
