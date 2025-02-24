# BeutifulSoup es una librería de Python que permite extraer información de páginas web.
# Se utiliza para extraer datos de HTML y XML.
# Para instalarla, ejecuta el siguiente comando en tu terminal:
#  pip install beautifulsoup4

# Ejemplo de uso de BeautifulSoup
from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>Web scraping example</title> 
</head> 

<body>
    <h1>Web scraping with BeautifulSoup</h1>
    <p>This is a paragraph.</p>
    <p>This is another paragraph.</p>
    <a href="https://www.example.com">This is a link.</a>
</body>
</html>
"""

# Creamos un objeto BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#Parser significa que vamos a analizar el contenido HTML visualmente mediante un navegador web

# Accedemos a las etiquetas del documento
print(soup.title)  # <title>Web scraping example</title>
print(soup.h1)  # <h1>Web scraping with BeautifulSoup</h1>
print(soup.p)  # <p>This is a paragraph.</p>
print(soup.a)  # <a href="https://www.example.com">This is a link.</a>

# Accedemos al contenido de las etiquetas
print(soup.title.string)  # Web scraping example
print(soup.h1.string)  # Web scraping with BeautifulSoup
print(soup.p.string)  # This is a paragraph.

# Accedemos a los atributos de las etiquetas
print(soup.a['href'])  # https://www.example.com

# Encontrar todas las etiquetas de un tipo
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.string)

# Encontrar la primera etiqueta de un tipo
first_paragraph = soup.find('p')
print(first_paragraph.string)
