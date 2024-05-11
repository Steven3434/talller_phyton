# Solicitar al usuario ingresar la calificación numérica
calificacion = int(input("Ingresa la calificación numérica del estudiante (entre 0 y 100): "))

# Asignar la letra correspondiente a la calificación
if calificacion >= 90 and calificacion <= 100:
    letra = 'A'
elif calificacion >= 80 and calificacion <= 89:
    letra = 'B'
elif calificacion >= 70 and calificacion <= 79:
    letra = 'C'
elif calificacion >= 60 and calificacion <= 69:
    letra = 'D'
else:
    letra = 'F'

# Mostrar la calificación en letra
print(f"La calificación {calificacion} equivale a una letra: {letra}")