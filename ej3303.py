try:
    num1 = int(input("ingresá el primer número: "))
    num2 = int(input("ingresá el segundo número: "))
    
    suma = num1 + num2
    print("la suma es:", suma)

except ValueError:
    print("error: suma números.")
    print("no jodas")