while True:
    entrada1 = input("ingresá el primer número: ")

    try:
        num1 = int(entrada1)
        num2 = int(input("ingresá el segundo número: "))
        
        suma = num1 + num2
        print("la suma es:", suma, "➕")
    
    except ValueError:
        print("error: tenes q ingresar solo números.")
        print("xfa")