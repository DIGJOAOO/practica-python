import json

with open("numero_favorito.json", "r") as archivo:
    numero = json.load(archivo)

print(f"tu número favorito es {numero}.")