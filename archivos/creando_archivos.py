# Voy a llamar a un archivo de texto, abrirlo y leerlo mostrándolo por consola


archivo_de_texto = open ("archivos\\texto.txt", "r+",encoding="UTF-8") 

# archivo_de_texto.write ("\n Que onda esta es una nueva linea") sobreescribe todo el archivo

#print (archivo_de_texto.read())


import json

json_file = open ("archivos\\my_file.json" , "w+")

json_de_prueba = {
    "nombre" : "Ima", 
    "Apellido" : "S",
    "Lenguaje" : "Python"
}

json.dump(json_de_prueba,json_file)

json_file.close()

json_diccionario = json.load (open ("archivos\\my_file.json") ) # Quito el w+, sino me arroja error

print (json_diccionario) # Parseamos de un JSON a un diccionario en Python print (type(json_diccionario)) Entonces:
print (json_diccionario["nombre"])


#      --------------------------------------------------------        #





