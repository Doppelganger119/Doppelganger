"""

Ejercicio 5. Hacer un progama que muestre todos los números 
entre dos números qie diga el usuario

"""

numero1 = int(input("Introuce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 < numero2:

    for contador in range(numero1, (numero2 + 1)):
        print(contador)

else:
    print("El numero 1 debe ser menor al número 2")
