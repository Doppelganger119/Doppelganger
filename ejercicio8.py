"""
Ejercicio 8. ¿Cuanto es el x por ciento de x numero

20% de 150 por ejemplo

"""

numero = int(input("Introduce el número: "))
porcentaje = int(input(f"¿Qué porcentaje quieres sacar de {numero}: "))

operación = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operación}")