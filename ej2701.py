class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto.")

r1 = Restaurante("La Parrilla Feliz", "Parrilla")
r2 = Restaurante("El sushi triste", "pescaderia")
r3 = Restaurante("mc donald meh", "comida rapida")

print(r1.nombre_restaurante)
print(r1.tipo_cocina)

r2.describir_restaurante()
r2.abrir_restaurante()

print(r2.nombre_restaurante)
print(r2.tipo_cocina)

r3.describir_restaurante()
r3.abrir_restaurante()

print(r3.nombre_restaurante)
print(r3.tipo_cocina)

r3.describir_restaurante()
r3.abrir_restaurante()