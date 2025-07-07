# 🛠️ Programa: Sistema de Reparación Electrónica
# Autor: Jordy Quispe
# Descripción: Aplicación de POO usando herencia, encapsulación y polimorfismo

# Clase base que representa un dispositivo electrónico
class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        return f"Dispositivo: {self.marca} {self.modelo}"


# Clase derivada que representa una Laptop (hereda de Dispositivo)
class Laptop(Dispositivo):
    def __init__(self, marca, modelo, ram):
        super().__init__(marca, modelo)
        self.ram = ram

    # Polimorfismo: sobrescribimos el método mostrar_info
    def mostrar_info(self):
        return f"Laptop: {self.marca} {self.modelo} - RAM: {self.ram}GB"


# Clase derivada que representa un Celular (también hereda de Dispositivo)
class Celular(Dispositivo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__estado = "Nuevo"  # Encapsulación: atributo privado

    def reparar(self):
        self.__estado = "Reparado"

    def obtener_estado(self):
        return self.__estado

    # Polimorfismo: sobrescribimos el método mostrar_info
    def mostrar_info(self):
        return f"Celular: {self.marca} {self.modelo} - Estado: {self.__estado}"


# Función que utiliza polimorfismo al aceptar distintos tipos de dispositivos
def mostrar_detalles(dispositivo):
    print(dispositivo.mostrar_info())


# ⚙️ Crear instancias de las clases
laptop1 = Laptop("HP", "Pavilion", 8)
celular1 = Celular("Xiaomi", "Redmi Note 10")

# Usar los métodos
mostrar_detalles(laptop1)
mostrar_detalles(celular1)

# Reparar el celular y mostrar el nuevo estado
celular1.reparar()
mostrar_detalles(celular1)  # Mostrará estado "Reparado"