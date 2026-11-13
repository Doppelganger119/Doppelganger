"""
Una variable es un contenedor de información que dentro guarda un dato,
se pueden crear muchas variables y que cada una tenga un dato distinto
"""

#Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "Con Victor Robles"
numero = 45
decimal = 6.7

#Mostrar el valor de las variables
print (texto)
print (texto2)
print (numero)
print (decimal)

print("-----------------------------------")

# Sustituir el valor de algunas variables / reaasignando valores

numero = 77
decimal = 8.9

print (numero)
print (decimal)

print("-----------------------------------")

#Concatenación

nombre = "Victor"
apellidos = "Robles"
web = "victorroblesweb.es"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}") #Otra forma de concatenar
print("Hola me llamo {} {} y mi web es {}".format (nombre, apellidos,web))
print(nombre, apellidos, web)