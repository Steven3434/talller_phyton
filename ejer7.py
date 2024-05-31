# Solicitar al usuario un número entero
numero = int(input("Por favor, ingresa un número entero: "))

# Validar si el número es positivo, negativo o cero
if numero > 0:
    print("El número ingresado es positivo.")
elif numero < 0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es cero.")

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"Además, el número {numero} es par.")
else:
    print(f"Además, el número {numero} es impar.")