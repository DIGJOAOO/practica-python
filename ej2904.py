class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir_auuto(self):
        return f"{self.año} {self.marca} {self.modelo}"


class Bateria:
    def __init__(self, capacidad_bateria=40):
        self.capacidad_bateria = capacidad_bateria

    def describir_bateria(self):
        print(f"Este auto tiene una batería de {self.capacidad_bateria} kWh.")

    def obtener_autonomia(self):
        print(f"bateria: {self.capacidad_bateria}")
        if self.capacidad_bateria >= 65:
            pass
        else:
            print("menor a 65, actualizando autonomia")
            self.capacidad_bateria = 65
class AutoElectrico(Auto):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()


mi_leaf = AutoElectrico('nissan', 'leaf', 2024)

print(mi_leaf.describir_auuto())
mi_leaf.bateria.describir_bateria()
mi_leaf.bateria.obtener_autonomia()
mi_leaf.bateria.obtener_autonomia()

