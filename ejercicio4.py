# Solicitar al usuario un número entero
numero = int(input("Por favor, ingresa un número entero: "))

# Verificar si el número es divisible por 3 y por 5
if numero % 3 == 0 and numero % 5 == 0:
    print(f"El número {numero} es divisible tanto por 3 como por 5.")
else:
    print(f"El número {numero} no es divisible por 3 y 5 simultáneamente.")