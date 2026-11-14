"""

Una función es un conjunto de instruccionesx
agrupadas bajo un nombre concreto que pueden reutilizarse 
invocando a la función tantas veces como sea necesário

def nombreDeMiFunción(parametros)
    #cONJUNTO DE INSTRUCCIONES

    nombreDeMiFunción(MI_PARAMETRO)

"""

# Ejemplo uno

print("####### EJEMPLO 1 #########")

# Definir función

def muestraNombre():
    print("Victor")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")

# Invocar función

muestraNombre()

#Ejemmplo 2: parámetros

print("####### EJEMPLO 1 #########")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Eres menor de edad")
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)