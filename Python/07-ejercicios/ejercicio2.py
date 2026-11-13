"""
Ejercicio 2. Escreibir un script que nos muestre por pantalla 
todos los numeros desde el 1 hasta 120

"""

contador = 1

for contador in range(1,121):
    if contador %2 == 0:
        print(f" {contador} es par")
    else:
        print(f"{contador} es impar")