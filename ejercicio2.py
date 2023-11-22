# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtenerInformacion(self):
        return f"{self.marca} {self.modelo}"

# Definición de la clase derivada Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, numPuertas):
        # Llamada al constructor de la clase base usando super()
        super().__init__(marca, modelo)
        self.numPuertas = numPuertas

    # Implementación del método obtenerInformacion específico para Auto
    def obtenerInformacion(self):
        return f"Auto: {super().obtenerInformacion()}, Puertas: {self.numPuertas}"

# Definición de la clase derivada Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        # Llamada al constructor de la clase base usando super()
        super().__init__(marca, modelo)
        self.tipo = tipo

    # Implementación del método obtenerInformacion específico para Bicicleta
    def obtenerInformacion(self):
        return f"Bicicleta: {super().obtenerInformacion()}, Tipo: {self.tipo}"

# Creación de instancias de Auto y Bicicleta
miAuto = Auto("Toyota", "Camry", 4)
miBicicleta = Bicicleta("Giant", "Defy", "De carretera")

# Llamadas al método obtenerInformacion con las instancias y muestra los resultados
print(miAuto.obtenerInformacion())
print(miBicicleta.obtenerInformacion())

##############################################################################################################-+
# Definición de la clase base Empleado
class Empleado:
    def __init__(self, nombre, salarioBase):
        self.nombre = nombre
        self.salarioBase = salarioBase

    def calcularSalario(self):
        return self.salarioBase

# Definición de la clase derivada EmpleadoAsalariado que hereda de Empleado
class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, salarioBase, bonoAnual):
        # Llamada al constructor de la clase base usando super()
        super().__init__(nombre, salarioBase)
        self.bonoAnual = bonoAnual

    # Implementación del método calcularSalario específico para EmpleadoAsalariado
    def calcularSalario(self):
        return super().calcularSalario() + self.bonoAnual

# Definición de la clase derivada EmpleadoPorHoras que hereda de Empleado
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, salarioPorHora, horasTrabajadas):
        # Llamada al constructor de la clase base usando super()
        super().__init__(nombre, 0)  
        self.salarioPorHora = salarioPorHora
        self.horasTrabajadas = horasTrabajadas

    # Implementación del método calcularSalario específico para EmpleadoPorHoras
    def calcularSalario(self):
        return self.salarioPorHora * self.horasTrabajadas

# Creación de instancias de EmpleadoAsalariado y EmpleadoPorHoras
empleadoAsalariado = EmpleadoAsalariado("Juan", 50000, 10000)
empleadoPorHoras = EmpleadoPorHoras("Maria", 15, 40)

# Imprimir salarios totales
print(f"{empleadoAsalariado.nombre}: Salario Total - {empleadoAsalariado.calcularSalario()}")
print(f"{empleadoPorHoras.nombre}: Salario Total - {empleadoPorHoras.calcularSalario()}")

#############################################################################################################
# Definición de la clase base FormaGeometrica
class FormaGeometrica:
    def __init__(self, color):
        self.color = color

    def obtenerInfo(self):
        return f"Forma de color {self.color}"

# Definición de la clase derivada Circulo que hereda de FormaGeometrica
class Circulo(FormaGeometrica):
    def __init__(self, color, radio):
        # Llamada al constructor de la clase base usando super()
        super().__init__(color)
        self.radio = radio

    # Implementación del método obtenerInfo específico para Circulo
    def obtenerInfo(self):
        return f"Círculo de color {self.color} con radio {self.radio}"

# Definición de la clase derivada Rectangulo que hereda de FormaGeometrica
class Rectangulo(FormaGeometrica):
    def __init__(self, color, largo, ancho):
        # Llamada al constructor de la clase base usando super()
        super().__init__(color)
        self.largo = largo
        self.ancho = ancho

    # Implementación del método obtenerInfo específico para Rectangulo
    def obtenerInfo(self):
        return f"Rectángulo de color {self.color} con largo {self.largo} y ancho {self.ancho}"

# Creación de instancias de Circulo y Rectangulo
circuloRojo = Circulo("rojo", 5)
rectanguloAzul = Rectangulo("azul", 8, 4)

# Imprimir información de las formas geométricas
print(circuloRojo.obtenerInfo())
print(rectanguloAzul.obtenerInfo())
