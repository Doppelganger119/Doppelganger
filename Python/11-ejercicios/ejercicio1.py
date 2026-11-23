"""
Ejercicio uno. Hacerun programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
-Recorrer la lista y mostrarla
-Hacer una función que  recorra listas de numeros y devuelva un string
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar un elemento que el usuario pida por teclado
"""

# Crear la lista

numeros = [13, 64,52, 73, 21, 7, 91, 63]

# Crear función que recorra lista y devuelva un string
def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado

# Recorrer y mostrar

print("####### Recorrer y mostrar #######")
"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))
print(mostrarLista(["Victor", "Juan", "Pepe"]))

# Ordenar y mostrar

print("####### Ordenar y mostrar #######")

numeros.sort()
print(mostrarLista(numeros))

# Mostrar su longitud
print("####### Mostrar su longitud #######")

print(len(numeros))

# Búsqueda en la lista
print("####### Búsqueda en la lista #######")

busqueda = int(input("Introduce el número: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <=0:
    busqueda = int(input("Introduce el número: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"###### Buscar en la lista el número {busqueda}")

search = numeros.index(busqueda)
print(f"El número buscado existe en la lista, es el índice : {search}")