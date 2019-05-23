import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from math import ceil
import pandas as pd
from pandas.io.json import json_normalize


page = 1
pageSize = 100
profeco = pd.DataFrame()
while True:

    r = requests.get("https://datos.profeco.gob.mx/quejas/consulta.php?ESTADO_PROCESAL=Conciliada&ESTADO_UA=DISTRITO FEDERAL&page={}&pageSize={}".format(page,pageSize))
    #print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = str(soup)[417:]
    json_data = json.loads(data)

    ### paginacion

    pagination = json_data['pagination']
    total =  pagination.get('total')
    
    print(json_data['pagination'])
    print(total)

    print("*****************")
    page += 1
    #paginas = ceil(total/pageSize)
    paginas = 5
    if page> paginas:
        break

    results = json_data['results']
    #pprint(results)
    datos = json_normalize(results)
    profeco = profeco.append(datos , ignore_index=True)
    pprint(datos)


#https://datos.profeco.gob.mx/quejas/catalogo.php?catalogo=GIRO&pageSize=100

#r = requests.get("https://datos.profeco.gob.mx/quejas/catalogo.php?catalogo=ESTADO_UA")
#print(r.text)
print(profeco.head())
profeco.to_csv('profeco.csv')