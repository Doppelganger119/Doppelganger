"""

# For
for variable in elemento iterable (LISTAS,RANGOS, ETC)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el número: " + str(contador))

    resultado += contador

print(f"El resultado de la suma es: {resultado}")

# EJEMPLO CON TABLAS DE MULTIPLICAR

print("\nTABLA DE MULTIPLICAR")

numero_usuario = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar del {numero_usuario}")

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("No se puede mostrar la tabla del 45")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")