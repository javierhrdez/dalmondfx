
import pandas as pd
from pandas.io.json import json_normalize
import requests
token = "627bee6f-aec0-47bb-b369-c058e32ec406"


lat , lon = 19.3878814,-99.179302
radio = 250 #mts
condicion = "restaurante"


url = f'https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/{condicion}/{lat},{lon}/{radio}/{token}'

r = requests.get(url)
denue = pd.DataFrame()
datos = r.json()
for dato in datos:
    print(dato)
    dato = json_normalize(dato)
    denue = denue.append(dato , ignore_index=True)

print(denue.head())
denue.to_csv('denue.csv')