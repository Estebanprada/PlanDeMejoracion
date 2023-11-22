# Definición de la clase base Animal
class Animal:
    def hablar(self):
        pass

# Definiciones de clases derivadas Gallo, Oveja, Vaca que heredan de Animal
class Gallo(Animal):
    def hablar(self):
        return "Kikiriki!"

class Oveja(Animal):
    def hablar(self):
        return "Meee!"

class Vaca(Animal):
    def hablar(self):
        return "Moo!"

# Definición de la función hacerHablar que toma un objeto Animal y llama a su método hablar
def hacerHablar(animal):
    return animal.hablar()

# Creación de instancias de Gallo, Oveja y Vaca
gallo = Gallo()
oveja = Oveja()
vaca = Vaca()

# Llamadas a la función hacerHablar con las instancias y muestra los resultados
print(hacerHablar(gallo))
print(hacerHablar(oveja))
print(hacerHablar(vaca))


###############################################################################################################
# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"{self.marca} {self.modelo}"

    def conducir(self):
        pass

# Definición de las clases derivadas Coche, Motocicleta que heredan de Vehiculo
class Coche(Vehiculo):
    def conducir(self):
        return "¡Vroom, vroom!"

class Motocicleta(Vehiculo):
    def conducir(self):
        return "¡Rum, rum!"

# Función probarConduccion que toma un objeto Vehiculo, llama a describir y conducir, y retorna un mensaje
def probarConduccion(vehiculo):
    return f"Conduciendo {vehiculo.describir()}: {vehiculo.conducir()}"

# Creación de instancias de Coche y Motocicleta
coche = Coche("Toyota", "Corolla")
motocicleta = Motocicleta("Harley-Davidson", "Sportster")

# Llamadas a la función probarConduccion con las instancias y muestra los resultados
print(probarConduccion(coche))
print(probarConduccion(motocicleta))

 
##############################################################################################################
# Definición de la clase base MultimediaItem
class MultimediaItem:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def reproducir(self):
        pass

# Definición de la clase derivada Cancion que hereda de MultimediaItem
class Cancion(MultimediaItem):
    def __init__(self, titulo, artista, duracion):
        # Llamada al constructor de la clase base usando super()
        super().__init__(titulo, duracion)
        self.artista = artista

    # Implementación del método reproducir específico para Cancion
    def reproducir(self):
        return f"Reproduciendo la canción: {self.titulo} - {self.artista}"

# Definición de la clase derivada Pelicula que hereda de MultimediaItem
class Pelicula(MultimediaItem):
    def __init__(self, titulo, director, duracion):
        # Llamada al constructor de la clase base usando super()
        super().__init__(titulo, duracion)
        self.director = director

    # Implementación del método reproducir específico para Pelicula
    def reproducir(self):
        return f"Reproduciendo la película: {self.titulo} (Dirigida por {self.director})"

# Definición de la función reproducirItem que toma un objeto MultimediaItem y llama a su método reproducir
def reproducirItem(item):
    return item.reproducir()

# Creación de instancias de Cancion y Pelicula
cancion = Cancion("Bohemian Rhapsody", "Queen", 6)
pelicula = Pelicula("Inception", "Christopher Nolan", 148)

# Llamadas a la función reproducirItem con las instancias y muestra los resultados
print(reproducirItem(cancion))
print(reproducirItem(pelicula))



