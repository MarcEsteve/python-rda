import pandas as pd # Importamos la librería pandas y sirve para trabajar con datos
import requests # Importamos la librería requests que sirve para hacer peticiones a la web
from io import StringIO  # Necesario para convertir el string en un objeto legible
#pip install requests
#pip install pandas
#pip install StringIO

url='https://es.wikipedia.org/wiki/Poblaci%C3%B3n_mundial'
r = requests.get(url) # Hacemos la petición a la web
r.status_code # Si devuelve 200 es que la petición ha ido bien

html_doc = r.text # Guardamos el contenido de la web en una variable
df_lista = pd.read_html(html_doc) # Leemos las tablas de la web "deprecated"

#Breakpoint
# Simulación de HTML con una tabla
html_doc = """
<table>
    <tr><th>Nombre</th><th>Edad</th></tr>
    <tr><td>Ana</td><td>25</td></tr>
    <tr><td>Juan</td><td>30</td></tr>
</table>
"""

# Convertir el string HTML en un objeto StringIO
html_buffer = StringIO(html_doc)
df_lista = pd.read_html(html_buffer)
print(df_lista[0])



# df_lista
# df=df_lista[0] # Seleccionamos la tabla que queremos
# df

