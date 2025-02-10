# Para ejecutar este script, es necesario instalar las siguientes librerías:
# pip install requests beautifulsoup4

import os
import requests
from bs4 import BeautifulSoup

# Limpiar la terminal
os.system('cls')

# URL de la página web a extraer datos
url = "https://pr0j3ct.com"

# Realizar una solicitud GET a la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraer el primer título <h1> encontrado
    titulo = soup.find("h1")
    
    if titulo:
        print(f"Título de la página: {titulo.text}")
    else:
        print("No se encontró un título <h1> en la página.")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
