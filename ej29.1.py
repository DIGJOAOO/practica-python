class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.sabores = sabores

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")
        print(f"Sabores disponibles:")
        for i in self.sabores:
            print(f"- {i}")

    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto.")


rest = Restaurante("heladeria", "heladeria", ["crema del cielo", "dulce de leche", "vainilla"])

rest.describir_restaurante()
rest.abrir_restaurante()