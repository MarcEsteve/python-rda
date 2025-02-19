import pandas as pd
import requests # Importamos la librería requests que sirve para hacer peticiones a la web
url='https://es.wikipedia.org/wiki/Poblaci%C3%B3n_mundial'
r = requests.get(url) # Hacemos la petición a la web
r.status_code # Si devuelve 200 es que la petición ha ido bien

html_doc = r.text # Guardamos el contenido de la web en una variable
df_lista = pd.read_html(html_doc) # Leemos las tablas de la web 
df_lista
df=df_lista[0] # Seleccionamos la tabla que queremos
df

