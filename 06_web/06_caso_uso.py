from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install())) # Iniciamos el driver de Firefox

driver.get("https://ventas27122020.bubbleapps.io/version-test")

# Selector de Comercial
selector = 'div.bubble-r-line:nth-child(2) > div:nth-child(1) > input:nth-child(1)'

elem = driver.find_element(By.CSS_SELECTOR, selector) # Buscamos el campo de texto de Comercial

elem.click() # Hacemos clic en el campo de texto de Comercial
elem.send_keys('Marc') # Escribimos en el campo de texto de Comercial

# Buscamos todos los selectores de todos los campos de texto para rellenarlos

elemComercial = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(2) > div:nth-child(1) > input:nth-child(1)') 
elemLineaProducto = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(2) > div:nth-child(2) > input:nth-child(1)')
elemUnidades = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(3) > div:nth-child(1) > input:nth-child(1)') 
elemFecha = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(4) > div:nth-child(1) > input:nth-child(1)') 
elemCodigoProducto = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(4) > div:nth-child(2) > input:nth-child(2)') 
elemPais = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(4) > div:nth-child(2) > input:nth-child(1)') 
elemPrecioUnitario = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(5) > div:nth-child(1) > input:nth-child(2)') 
elemVentaTotal = driver.find_element(By.CSS_SELECTOR, 'div.bubble-r-line:nth-child(5) > div:nth-child(1) > input:nth-child(1)') 

elemGuardar = driver.find_element(By.CSS_SELECTOR, '.clickable-element') # Botón de Guardar

# Importamos la librería pandas para leer el archivo de Excel con el dataset de ventas
import pandas as pd
df_ventas = pd.read_excel("C:\Users\artha\OneDrive\Escritorio\AKKODIS\python-rda\06_web\Ventas_productos_automóvil.xlsx")
df_ventas.head()

# Insertamos los datos del primer registro de df_ventas en los campos de texto de la página web
elemComercial.send_keys(str(df_ventas['Comercial'][0]))
elemLineaProducto.send_keys(str(df_ventas['Línea de Producto'][0]))
elemUnidades.send_keys(str(df_ventas['Unidades'][0]))
elemFecha.send_keys(str(df_ventas['Fecha'][0])) 
elemCodigoProducto.send_keys(df_ventas['Código de Producto'][0])
elemPais.send_keys(df_ventas['País'][0])
elemPrecioUnitario.send_keys(df_ventas['Precio Unitario'][0])
elemVentaTotal.send_keys(str(df_ventas['Total Venta'][0]))
elemGuardar.click() # Guardamos el registro en la página web

elemComercial.clear() # Limpiamos el campo de texto de Comercial
elemLineaProducto.clear() # Limpiamos el campo de texto de Línea de Producto
elemUnidades.clear() # Limpiamos el campo de texto de Unidades
elemFecha.clear() # Limpiamos el campo de texto de Fecha
elemCodigoProducto.clear() # Limpiamos el campo de texto de Código de Producto
elemPais.clear() # Limpiamos el campo de texto de País
elemPrecioUnitario.clear() # Limpiamos el campo de texto de Precio Unitario
elemVentaTotal.clear() # Limpiamos el campo de texto de V

elemGuardar.click() # Guardamos el registro en la página web

#  Iteramos sobre todos los registros de df_ventas para insertarlos en la página web

for i in range(len(df_ventas)):
    elemComercial.send_keys(str(df_ventas['Comercial'][i]))
    elemLineaProducto.send_keys(str(df_ventas['Línea de Producto'][i]))
    elemUnidades.send_keys(str(df_ventas['Unidades'][i]))
    elemFecha.send_keys(str(df_ventas['Fecha'][i])) 
    elemCodigoProducto.send_keys(df_ventas['Código de Producto'][i])
    elemPais.send_keys(df_ventas['País'][i])
    elemPrecioUnitario.send_keys(df_ventas['Precio Unitario'][i])
    elemVentaTotal.send_keys(str(df_ventas['Total Venta'][i]))
    elemGuardar.click() # Guardamos el registro en la página web

    elemComercial.clear() # Limpiamos el campo de texto de Comercial
    elemLineaProducto.clear() # Limpiamos el campo de texto de Línea de Producto
    elemUnidades.clear() # Limpiamos el campo de texto de Unidades
    elemFecha.clear() # Limpiamos el campo de texto de Fecha
    elemCodigoProducto.clear() # Limpiamos el campo de texto de Código de Producto
    elemPais.clear() # Limpiamos el campo de texto de País
    elemPrecioUnitario.clear() # Limpiamos el campo de texto de Precio Unitario
    elemVentaTotal.clear() # Limpiamos el campo de texto de V

    elemGuardar.click() # Guardamos el registro en la página web

driver.quit() # Cerrar el driver de Firefox
