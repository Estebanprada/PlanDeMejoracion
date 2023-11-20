class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


persona1 = Persona("Juan", 25)


print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")


persona1.presentarse()
#############################################+#################################################################
class Persona:
  
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = 0

    
    def obtener_informacion(self):
        return f"{self.nombre}, {self.edad} años, {self.altura} cm, {self.peso} kg"
    
    def establecer_peso(self, peso):
        self.peso = peso
        print(f"{self.nombre} ahora pesa {self.peso} kg")

    def envejecer(self, anios):
        self.edad += anios
        print(f"{self.nombre} ahora tiene {self.edad} años")

persona1 = Persona(nombre="Juan", edad=25, altura=175)

print(persona1.obtener_informacion())

persona1.establecer_peso(70)

persona1.envejecer(5)
################################################################################################################
class Libro:
    def __init__(self, titulo, autor, paginas, estado="No leído"):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.estado = estado

    
    def obtener_informacion(self):
        return f"Libro: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nEstado: {self.estado}"


    def marcar_como_leido(self):
        self.estado = "Leído"
        print(f"Libro '{self.titulo}' marcado como leído.")

libro1 = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", paginas=432)


print(libro1.obtener_informacion())


libro1.marcar_como_leido()

print(libro1.obtener_informacion())






