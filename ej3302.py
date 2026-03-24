nombres = []

while True:
    nombre = input("Ingresa tu nombre (salir para terminar): ")
    
    if nombre.lower() == "salir":
        break
    
    nombres.append(nombre)

with open("guest_book.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Los nombres se guardaron en guest_book.txt")