# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de una instancia de Persona
persona1 = Persona("Juan", 25)

# Imprimir información de la persona
print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")

# Llamar al método presentarse
persona1.presentarse()

#############################################+#################################################################
# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, altura):
        # Inicialización de las propiedades de la instancia
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = 0

    def obtenerInformacion(self):
        # Método para obtener información completa de la persona
        return f"{self.nombre}, {self.edad} años, {self.altura} cm, {self.peso} kg"

    def establecerPeso(self, peso):
        # Método para establecer el peso de la persona
        self.peso = peso
        print(f"{self.nombre} ahora pesa {self.peso} kg")

    def envejecer(self, anios):
        # Método para hacer que la persona envejezca
        self.edad += anios
        print(f"{self.nombre} ahora tiene {self.edad} años")

# Creación de una instancia de Persona llamada persona1
persona1 = Persona(nombre="Juan", edad=25, altura=175)

# Imprimir información de la persona utilizando el método obtenerInformacion
print(persona1.obtenerInformacion())

# Establecer el peso de la persona utilizando el método establecerPeso
persona1.establecerPeso(70)

# Hacer que la persona envejezca utilizando el método envejecer
persona1.envejecer(5)

################################################################################################################
# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, paginas, estado="No leído"):
        # Inicialización de las propiedades de la instancia
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.estado = estado

    def obtenerInformacion(self):
        # Método para obtener información completa del libro
        return f"Libro: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nEstado: {self.estado}"

    def marcarComoLeido(self):
        # Método para marcar el libro como leído
        self.estado = "Leído"
        print(f"Libro '{self.titulo}' marcado como leído.")

# Creación de una instancia de Libro llamada libro1
libro1 = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", paginas=432)

# Imprimir información del libro utilizando el método obtenerInformacion
print(libro1.obtenerInformacion())

# Marcar el libro como leído utilizando el método marcarComoLeido
libro1.marcarComoLeido()

# Imprimir información actualizada del libro
print(libro1.obtenerInformacion())







