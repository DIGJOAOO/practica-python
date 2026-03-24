class User:
    def __init__(self, nombre, apellido, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
    def describir_user(self):
        print(f"Nombre: {self.nombre}")
        print(f"apellido: {self.apellido}")
        print(f"mail: {self.mail}")
    def welcome_user(self):
        print(f"hola {self.nombre}")

class Administrador(User):

    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)
        self.privilegios = [
            "puede agregar publicaciones",
            "puede eliminar publicaciones",
            "puede bloquear usuarios"
        ]

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(privilegio)

user = User("Joao", "Cabrera", "Joao@gmail.com")
admin = Administrador("Joao", "Cabrera", "joao@mail.com")

user.describir_user()
admin.mostrar_privilegios()
