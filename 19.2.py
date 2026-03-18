def cobrar_entradas():
    precios = {"menores": 0, "niños": 10, "mayores": 15}
    ans = ""
    total = 0
    while ans.lower() != "salir":
        ans = input("Ingrese la edad// salir para cerrar: ")
        if ans.lower() == "salir":
            break
        if int(ans) < 3:
            total += precios["menores"]
        elif 3 < int(ans) < 12:
            total += precios["niños"]
        elif int(ans) >= 12:
            total += precios["mayores"]
        else:
            print("E")
    print(f"precio final -{total}dls")
    exit()    
def main():
    cobrar_entradas()
main()