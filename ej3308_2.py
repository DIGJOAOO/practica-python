import json
import os

archivo_nombre = "numero_favorito.json"

if os.path.exists(archivo_nombre):
    with open(archivo_nombre, "r") as archivo:
        numero = json.load(archivo)
    print(f"tu número favorito es {numero}.")
else:
    numero = input("cual es tu número favorito: ")
    
    with open(archivo_nombre, "w") as archivo:
        json.dump(numero, archivo)
    
    print("guarda2 tu número favorito.")