import bs4 # Importamos la librería BeautifulSoup
import requests # Importamos la librería requests
import lxml # Importamos la librería lxml
import os # Importamos la librería os

os.system("cls") # Limpiamos la consola

# cabecera se lo explicamos al navegador como si fueramos un humano y no un bot
cabecera = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Obtener el precio de la página web milanuncios de un Tesla como ejemplo
url = "https://www.milanuncios.com/todoterreno-de-ocasion/tesla-model-y-536756562.htm"

# Otro ejemplo de url para obtener el precio de otro Tesla
# url = "https://www.milanuncios.com/coches-de-segunda-mano/tesla-model-y-520412004.htm"

# Hacemos la petición a la página web
response = requests.get(url, headers=cabecera)

# Creamos un objeto BeautifulSoup
soup = bs4.BeautifulSoup(response.text, 'lxml') # Parseamos el contenido de la página web

# print(soup.prettify()) # Mostramos el contenido de la página web de forma estructurada
print(soup) # Mostramos el título de la página web

# Buscamos el precio del Tesla en la página web con el selector CSS
elem = soup.select("#app > div.ma-LayoutBasic > div.ma-AdvertisementPageLayout.ma-AdvertisementPageLayout-justify--center > div.ma-AdvertisementPageLayout-center > div.ma-LayoutBasic-content.ma-AdDetail > div > main > article > section > div > div.ma-ContentAdDetail-priceWrapper > div > p > span > span")
print(elem) # Mostramos el <span> que contiene el precio del Tesla
elem[0].getText() # Obtenemos el texto del precio del Tesla con el método getText()
elem[0].text.strip() # Obtenemos el precio del Tesla con el método text y eliminamos los espacios en blanco con strip()

precio = elem[0].text.strip().replace('\xa0€', '').replace('.', '') # Obtenemos el precio del Tesla
# '\xa0€' es un espacio en blanco que se encuentra en el precio
# '.' es un separador de miles que se encuentra en el precio
precio = int(precio) # Convertimos el precio a un entero
print(precio) # Mostramos el precio del Tesla