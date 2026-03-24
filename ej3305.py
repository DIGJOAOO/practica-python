archivos = ["gatos.txt", "perros.txt"]

for nombre_archivo in archivos:
    try:
        with open(nombre_archivo, "r") as archivo:
            print(f"\nContenido de {nombre_archivo}:")
            print(archivo.read())
    
    except FileNotFoundError:
        print(f"no se encontró el archivo {nombre_archivo}.")