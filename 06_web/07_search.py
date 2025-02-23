# Automatización Búsqueda Web https://www.oscaro.es/filtro-de-aceite-7-g
import bs4
import requests
import lxml
import json

# Conveniente definir el elemento headers para evitar problemas de acceso
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} 

# Obtener el contenido en reailer https://www.oscaro.es/ para la búsqueda de un filtro de aceite
res = requests.get('https://www.oscaro.es/filtro-de-aceite-7-g', headers=headers)

# Creamos el objeto BeautifulSoup
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Seleccionamos selector CSS de interés dentro del objeto soup
soup.select('#root > main > div.flex-container > div.container.home-products > div.best-product > article:nth-child(1) > a > p > span')

# Definimos el elemento y nos quedamos con el texto
elem1 = soup.select('#root > main > div.flex-container > div.container.home-products > div.best-product > article:nth-child(1) > a > p > span')
elem1[0].getText().strip()

precio_1 = elem1[0].getText().strip().replace(' â\x82¬', '').replace(',', '.')

# Cogemos elemento 2 y 3

elem2 = soup.select('#root > main > div.flex-container > div.container.home-products > div.best-product > article:nth-child(2) > a > p > span')
elem3 = soup.select('#root > main > div.flex-container > div.container.home-products > div.best-product > article:nth-child(3) > a > p > span')
precio_2 = elem2[0].getText().strip().replace(' â\x82¬', '').replace(',', '.')
precio_3 = elem3[0].getText().strip().replace(' â\x82¬', '').replace(',', '.')

import numpy as np # Importamos la librería numpy para trabajar con arrays y valores numéricos
# Convertimos los precios a valores numéricos
array_precios = np.array([float(precio_1), float(precio_2), float(precio_3)])
precio_promedio = np.mean(array_precios) # Calculamos el precio promedio
print(precio_promedio) # Mostramos el precio promedio
