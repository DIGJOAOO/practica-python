import json

numero = input("ingrese su número favorito:")

with open("numero_favorito.json", "w") as archivo:
    json.dump(numero, archivo)

print("número guardado .")