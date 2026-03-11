pizzas = ["fugazzeta rellena", "pepperoni", "muzzarela"]

def mostrar_pizzas():
    for i in pizzas:
        if i == "fugazzeta rellena":
            print(f'la{i} es mi pizza favorita')
        else:
            print(f"no me gusta la{i}")
    print("no me gusta mucho la pizza")
def main():
    mostrar_pizzas()
main()