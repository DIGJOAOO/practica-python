import random

invitados = ["LIL J","FELIX","ROBERT DOWNEY JR."]
indice_no_viene = random.randint(0, len(invitados)-1)

def invitar_personas():
    for i in range(len(invitados)):
        print(f'{invitados[i]} estas invita3')
    print(f"oh no... {invitados[indice_no_viene]} no puede venir")
    reinvitar_personas()

def reinvitar_personas():
    nuevo_invitado = input("Nuevo invitado: ")
    invitados[indice_no_viene] = nuevo_invitado
    for i in range(len(invitados)):
        print(f'{invitados[i]} estas REinvita3')
def main():
    invitar_personas()

main()