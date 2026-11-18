"""
Listas o arrayz:
Son colecciones p cpnjuntos de datos, bajo un único nombre.
Para acceder a esos datos podemos usar un indice numérico.

"""

pelicula = "Batman"

#Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]

cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))

years = list(range(2020, 2050))

variada = ["Victor", 30, 4.4, True, "Texto"]

"""
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
# Índices
peliculas[1] = "Gran Torino"
peliculas[2] = "El Hobbit"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:3])
print(peliculas[0:])
print(peliculas)

# Añadir elementos a las listas

cantantes.append("Kase O")
cantantes.append("Natos y Waor")
print(cantantes)

# Recorrer lista

"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva película: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n***********Listado Películas**************")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} . {pelicula}")

# Listas multidimensionales
"""
print("\n***************Listado de contactos*******************")

contactos = [
    [
        'Antonio','antonio@antonio.com'
    ],
    [
      'Luis',
      'luis@luis.com'  
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre:" + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
# print(contactos[1][1])