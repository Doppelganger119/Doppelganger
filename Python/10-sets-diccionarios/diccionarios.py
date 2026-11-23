"""
Diccionario es un tipo de dato que almacena un conjunto de
datos. En formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Víctor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

print(persona["apellidos"])
print(type(persona))

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Atonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]
contactos[0]['nombre'] = "Antoñito"
print(contactos[0]['nombre'])

print("\n Listado de contactos: ")
print("------------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------------------------------")