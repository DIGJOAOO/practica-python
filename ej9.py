locaciones = ["PR", "isla de las cobras", "isla sentinel del norte", "bosque de Agokigahra"]

def ordenar_locaciones(locaciones):
    locaciones = locaciones.reverse()
def print_Locaciones(locaciones):
    for i in range(len(locaciones)):
        print(locaciones[i])
def main(locaciones):
    ordenar_locaciones(locaciones)
    print_Locaciones(locaciones)
main(locaciones)