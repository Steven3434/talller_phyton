# Solicitar al usuario tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Determinar cuál de los números es el mayor
if num1 >= num2 and num1 >= num3:
    print(f"El número {num1} es el mayor.")
elif num2 >= num1 and num2 >= num3:
    print(f"El número {num2} es el mayor.")
else:
    print(f"El número {num3} es el mayor.")