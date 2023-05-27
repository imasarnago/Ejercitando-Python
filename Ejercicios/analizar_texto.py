""" 
Crear un programa que analice texto y obtenga:

-Número total de palabras.   hecho :) 
-Longitud media de las palabras.  hecho :) 
-Número de oraciones del texto (cada vez que aparece un punto).   hecho :)
-Encuentre la palabra más larga.   hecho :) 

Todo esto utilizando un único bucle.

"""
prueba = "Esto es un texto de prueba. Debe ser largo para que sea interesante analizarlo."

lista_palabras = prueba.split()

import re
caracteres_todas_las_palabras  = 0
palabra_mas_larga = ''
total_oraciones = 0
for palabra in lista_palabras:
    

    caracteres_todas_las_palabras += len(palabra)
    
    if '.' in palabra:
        caracteres_todas_las_palabras -=1    
        total_oraciones += 1
    
    total_palabras = len (lista_palabras)
    
    if len(palabra)>len(palabra_mas_larga):
        palabra_mas_larga = palabra
        
    longitud_media = caracteres_todas_las_palabras / total_palabras
        
print (f"Cantidad palabras: {total_palabras}\nLongitud media: {longitud_media}\nCantidad oraciones: {total_oraciones}\nPalabra más larga: {palabra_mas_larga}")
    




class Texto:
    def __init__(self) -> int:
        self.cantidad_palabras = 0
        self.cantidad_oraciones = 0
        self.palabra_mas_larga = ''
        self.longitud_media = 0 
            
    
    def contar_las_palabras(self,texto):
        lista_palabras = texto.split()
        self.cantidad_palabras = len(lista_palabras) 
        return self.cantidad_palabras
    

    def contar_las_oraciones(self,texto):
        for palabra in texto:
            if palabra == '.':
                self.cantidad_oraciones += 1
        return self.cantidad_oraciones
    
    
    def palabra_larga (self,texto):
        lista = texto.split()
        for palabra in lista:
            if len(palabra)> len(self.palabra_mas_larga):
                self.palabra_mas_larga = palabra
        return self.palabra_mas_larga
    
    
    def longitud_medias(self,texto):
        lista = texto.split()
        contador = 0
        for palabra in lista:
            contador += len (palabra)
        self.longitud_media = contador/ self.cantidad_palabras
        return self.longitud_media
    

                
    

ejemplo = Texto()

cantidad_palabras  = ejemplo.contar_las_palabras(prueba)

longitud_m = ejemplo.longitud_medias(prueba)

cantidad_oraciones = ejemplo.contar_las_oraciones(prueba)

palabra_larga = ejemplo.palabra_larga(prueba)

# print (f"\n\nCantidad palabras: {cantidad_palabras}\nLongitud media: {longitud_m}\nCantidad oraciones: {cantidad_oraciones}\nPalabra más larga: {palabra_larga}")

    
