import random

def tiene_cumple_repetido(n):
    cumpleaños = []
    for _ in range(n):
        dia = random.randint(1, 365)
        cumpleaños.append(dia)
    return len(cumpleaños) != len(set(cumpleaños))


def experimento(n, repeticiones=10000):
    coincidencias = 0
    for _ in range(repeticiones):
        if tiene_cumple_repetido(n):
            coincidencias += 1
    return coincidencias / repeticiones


for n in range(5, 101, 5):
    probabilidad = experimento(n)
    print(f"si hay {n:3d} personas la probabilidad ≈ {probabilidad:.2%}")