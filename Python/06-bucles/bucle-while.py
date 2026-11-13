"""
#Bucle While
Estructura de control que itera o repite una
serie de instrucciones tantas veces como sea necesario mientras se cumpla una 
condición.

wile condición:
    BLOQUE DE INSTRUCCIONES
    actualización de contador
"""

contador = 1

while contador <= 100:
    print(f"Voy por el número: {contador}")
    contador += 1

print("-----------------")



contador = 1
muestrame = str(0)



while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

# Ejemplo while con tablas de multiplicar

numero_usuario = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar del {numero_usuario}")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("Tabla finalizada")