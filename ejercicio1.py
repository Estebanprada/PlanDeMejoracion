class Animal:
    def hablar(self):
        pass

class Gallo(Animal):
    def hablar(self):
        return "Kikiriki!"

class Oveja(Animal):
    def hablar(self):
        return "Meee!"

class Vaca(Animal):
    def hablar(self):
        return "Moo!"

def hacer_hablar(animal):
    return animal.hablar()

gallo = Gallo()
oveja = Oveja()
vaca = Vaca()

print(hacer_hablar(gallo))  
print(hacer_hablar(oveja))   
print(hacer_hablar(vaca))    

###############################################################################################################
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"{self.marca} {self.modelo}"

    def conducir(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        return "¡Vroom, vroom!"

class Motocicleta(Vehiculo):
    def conducir(self):
        return "¡Rum, rum!"

def probar_conduccion(vehiculo):
    return f"Conduciendo {vehiculo.describir()}: {vehiculo.conducir()}"

coche = Coche("Toyota", "Corolla")
motocicleta = Motocicleta("Harley-Davidson", "Sportster")

print(probar_conduccion(coche))         
print(probar_conduccion(motocicleta))   
##############################################################################################################
# Clase base
class MultimediaItem:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def reproducir(self):
        pass

class Cancion(MultimediaItem):
    def __init__(self, titulo, artista, duracion):
        super().__init__(titulo, duracion)
        self.artista = artista

    def reproducir(self):
        return f"Reproduciendo la canción: {self.titulo} - {self.artista}"


class Pelicula(MultimediaItem):
    def __init__(self, titulo, director, duracion):
        super().__init__(titulo, duracion)
        self.director = director

    def reproducir(self):
        return f"Reproduciendo la película: {self.titulo} (Dirigida por {self.director})"


def reproducir_item(item):
    return item.reproducir()


cancion = Cancion("Bohemian Rhapsody", "Queen", 6)
pelicula = Pelicula("Inception", "Christopher Nolan", 148)


print(reproducir_item(cancion))  
print(reproducir_item(pelicula))  


