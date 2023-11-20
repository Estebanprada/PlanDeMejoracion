class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_informacion(self):
        return f"{self.marca} {self.modelo}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
       
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def obtener_informacion(self):
        return f"Auto: {super().obtener_informacion()}, Puertas: {self.num_puertas}"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def obtener_informacion(self):
        return f"Bicicleta: {super().obtener_informacion()}, Tipo: {self.tipo}"


mi_auto = Auto("Toyota", "Camry", 4)
mi_bicicleta = Bicicleta("Giant", "Defy", "De carretera")


print(mi_auto.obtener_informacion())
print(mi_bicicleta.obtener_informacion())
############################-+-+##################################################################################-+
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, salario_base, bono_anual):
        super().__init__(nombre, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario(self):
        return super().calcular_salario() + self.bono_anual

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, 0)  
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.salario_por_hora * self.horas_trabajadas

empleado_asalariado = EmpleadoAsalariado("Juan", 50000, 10000)
empleado_por_horas = EmpleadoPorHoras("Maria", 15, 40)

print(f"{empleado_asalariado.nombre}: Salario Total - {empleado_asalariado.calcular_salario()}")
print(f"{empleado_por_horas.nombre}: Salario Total - {empleado_por_horas.calcular_salario()}")
#############################################################################################################
class FormaGeometrica:
    def __init__(self, color):
        self.color = color

    def obtener_info(self):
        return f"Forma de color {self.color}"

class Circulo(FormaGeometrica):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def obtener_info(self):
        return f"Círculo de color {self.color} con radio {self.radio}"

class Rectangulo(FormaGeometrica):
    def __init__(self, color, largo, ancho):
        super().__init__(color)
        self.largo = largo
        self.ancho = ancho

    def obtener_info(self):
        return f"Rectángulo de color {self.color} con largo {self.largo} y ancho {self.ancho}"

circulo_rojo = Circulo("rojo", 5)
rectangulo_azul = Rectangulo("azul", 8, 4)

print(circulo_rojo.obtener_info())     
print(rectangulo_azul.obtener_info())  

