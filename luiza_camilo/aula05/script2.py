import os
import json

file_path = "C:/Users/fabio.classo/Downloads/fabio/"\
"aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/"\
    "9.3_Dicionarios/2021/json"

os.chdir(file_path)

with open('person.json', 'r') as json_reader:
    data = json.load(json_reader, indent=4) # objeto json
    print(data)
