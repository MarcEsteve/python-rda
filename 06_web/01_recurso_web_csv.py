import pandas as pd # Permite la lectura de archivos CSV
# URL del recurso web
url='https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
df=pd.read_csv(url, delimiter=';')
df
