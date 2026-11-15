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

print("####### EJEMPLO 2 #########")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Eres menor de edad")
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)

# Ejemplo 3

print("####### EJEMPLO 3 #########")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)

# Ejemplo 3.1

print("-----------------------------------")

for numero_tabla in range(1, 11):
    tabla(numero_tabla)


# Ejemplo 4

print("####### EJEMPLO 4 #########")

# Parámetros opcionales

def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Juan Carlos Álvarez Pazos", "7142267E")

# Ejemplo 5: parámetros opcionales y return o devolver datos

print("####### EJEMPLO 5 #########")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print (saludame("Juan Carlos"))

# Ejemplo 6 

print("####### EJEMPLO 6 #########")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas !=False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " +str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación" + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(5, 5))

# Ejeplo 7
print("\n####### EJEMPLO 7 #########")

def getNombre(nombre):
    texto =f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto =f"El apellido es: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Juan Carlos", "Álvarez"))

# Ejemplo 8: Funciones Lambda
print("\n####### EJEMPLO 8 ########")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2026))