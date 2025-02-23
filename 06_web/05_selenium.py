# *** Para instalar en Jupyter Notebook:
# !pip install selenium
# !pip install webdriver-manager

import os # Importamos la librería os
os.system("cls") # Limpiamos la consola

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Si queremos utilizar Edge:
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Si queremos utilizar Safari:
# from selenium.webdriver.safari.service import Service
# from webdriver_manager.safari import SafariDriverManager

# Si queremos utilizar Opera:
# from selenium.webdriver.opera.service import Service
# from webdriver_manager.opera import OperaDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install())) # Iniciamos el driver de Firefox

# Navegar a una página web
driver.get("https://www.google.com")

elem = driver.find_element(By.CSS_SELECTOR, '#APjFqb') # Buscamos el campo de texto de Google

elem.click() # Hacemos clic en el campo de texto de Google
elem.send_keys('Temperatura en Madrid') # Escribimos en el campo de texto de Google
elem.submit() # Enviamos el formulario

driver.back() # Volver a la página anterior
driver.forward() # Avanzar a la página siguiente

elem.clear() # Limpiar el campo de texto de Google

driver.refresh() # Refrescar la página
driver.quit() # Cerrar el driver de Firefox