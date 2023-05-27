class Perro:
    # Defino atributos con valores definidos
    #nombre = "Dori"
    #color = "Negro"
    #tamaño = "Mediano"
    
    # Si no quiero que los atributos tengan esos valores por defecto (mejor):
    
    def __init__(self,nombre, color, tamaño):
        self.nombre = nombre
        self.color = color
        self.tamaño = tamaño
    
    # Defino métodos
    def _dormir (self):
        print ("Estoy durmiendo")
    def hablar (self):
        print (f"Hola, mi nombre es {self.nombre}. Mi pelo es {self.color} y soy de tamaño {self.tamaño}")
    def dar_pata (self):
        print ("Te doy la patita")
        
        
# Instanciando la clase Perro en un objeto

perro_1 = Perro("Dori","negro","chico")


""" Ahora veamos un ejemplo de herencia """

class Mascota:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def saludar (self):
        print(f"Hola, mi nombre es {self.nombre}")
        
# Ahora creo una clase y hago que HEREDE características de la clase padre

class Gato(Mascota):
    pass

gato = Gato ("Señor gato")   # gato.saludar()