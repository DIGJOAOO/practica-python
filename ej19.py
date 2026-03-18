def ingresar_ingredientes():
    ingredientes = []
    ans = ""
    while ans.lower() != "salir":
        ans = (input("Ingrese un ingrediente //SALIR para cerrar el programa: "))
        if ans.lower() != "salir":
            ingredientes.append(ans)
        print("LISTA DE INGREDIENTES")
        for i in ingredientes:
            print(f"- {i}")
    exit()
def main():
    ingresar_ingredientes()
main()