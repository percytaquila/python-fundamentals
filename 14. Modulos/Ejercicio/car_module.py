class Car:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def display_info(self):
        return f"{self.marca} {self.modelo}, {self.anio}"