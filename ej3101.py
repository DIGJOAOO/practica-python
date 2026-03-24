import random
from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        numero = randint(1, self.sides)
        print(numero)


dado6 = Die()

print("Dado de 6 caras:")
for i in range(10):
    dado6.roll_die()

dado10 = Die(10)

print("Dado de 10 caras:")
for i in range(10):
    dado10.roll_die()

dado20 = Die(20)

print("Dado de 20 caras:")
for i in range(10):
    dado20.roll_die()