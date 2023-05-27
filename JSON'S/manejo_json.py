import json 
"""
json_str = '{"nombre":"ima","edad":21,"ciudad":"cordoba"}'

#          Creo un diccionario a partir de un json

json_dict = json.loads(json_str)

# print (json_dict)   

# print (json_dict['edad'])
# print (json_dict['ciudad'])

"""

data = {"usuario": "usuario1",
        "nombre" : "Im",
        "edad" : 21
        }

#         Creo un objeto json a partir de un diccionario de Python
data_json = json.dumps(data) # print (type(data_json))

"""
Tambien se puede usar algo del tipo:  json_data = json.JSONEncoder().encode({......})   y:
json.JSONDecoder().decode(json_data)

"""
