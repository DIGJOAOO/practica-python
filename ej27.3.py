class User:
    def __init__(self, nombre, apellido, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
    def describe_user(self):
        print(f"Nombre: {self.nombre}")
        print(f"apellido: {self.apellido}")
        print(f"mail: {self.mail}")
    def welcome_user(self):
        print(f"hola {self.nombre}")

user1 = User("Santiago", "Chaparro", "CarlitosGameplay845@gmail.com")
print(user1.describe_user())