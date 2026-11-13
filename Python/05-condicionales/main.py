"""
# Condicional if

Si se cumple esta condiución entonces se ejecuta el bloque de código que está dentro del if
Si no se cumple la condición entonces se ejecuta el bloque de código que está dentro del else

if condicion:
    # Bloque de código que se ejecuta si la condición es verdadera
else:
    # Bloque de código que se ejecuta si la condición es falsa

    
    # Operadores de comparación 

    == igual
    != diferente
    > mayor que
    < menor que
    >= mayor o igual que
    <= menor o igual que

    # Operadores logicos

    and = y
    or = o
    ! negación
    not = no
"""

# Ejemplo uno 
print("*************Ejemplo uno*************")

# color = "verde"

color = input("Introduce un color: ")

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")


# Ejemplo dos 
print("\n*************Ejemplo dos*************")

year = int(input("Introduce un año: "))

if year >= 2021:
    print("Estamos en el año 2021 o en adelante")
else:
    print("No estamos en el año 2021 ni en adelante")

# Ejemplo tres
print("\n*************Ejemplo tres*************") 

nombre = input("Introduce tu nombre: ")
ciudad = input("Introduce tu ciudad: ")
continente = input("Introduce tu continente: ")
edad = int(input("Introduce tu edad: "))
mayoria_de_edad = 18

if edad >= mayoria_de_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print("No Es europeo")
    else:
        print(f"Es europeo y es de {ciudad}")
else:
        print(f"{nombre} no es mayor de edad")


# Ejemplo cuatro
print("\n*************Ejemplo cuatro*************")

dia = int(input("Introduce un número de día de la semana (1-7): "))

"""

if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miércoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miércoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")


# Ejemplo cinco
print("\n*************Ejemplo cinco*************")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Está en edad de trabajar!!")
else:
    print("No está en edad de trabajar!!")

# Ejemplo seis
print("\n*************Ejemplo seis*************")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")

# Ejemplo siete
print("\n*************Ejemplo siete*************")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un país de habla hispana")
else:
    print(f"{pais} si es un país de habla hispana")


# Ejemplo ocho
print("\n*************Ejemplo ocho*************")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un país de habla hispana")
else:
    print(f"{pais} si es un país de habla hispana")