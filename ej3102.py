import random
from random import sample

elementos = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

ganadores = [sample(elementos, 4)]
mi_bombo = [sample(elementos, 4)]
intentos = 0
jugar = True
def sacar_ganadores():
    print(f"los numeros ganadores son:")
    for i in ganadores:
        pass

def checkear_ganadores():
    global ganadores, intentos, jugar
    if ganadores == mi_bombo:
        print(f"ganaste la loteria")
        print(f"cantidad de intentos: {intentos}")
        jugar = False
    else:
        print(f"segui intentando")
        ganadores = sample(elementos, 4)
        intentos += 1

def main():
    while jugar:
        sacar_ganadores()
        checkear_ganadores()
main()
#estuvo 2 horas y no gane la loteria 


#triste