# Pedir al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")