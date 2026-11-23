"""
Set es un tipo de dato, para tener una colleción de valores,
pero no tiene ni índice ni orden

"""

personas = {
"Victor", "Manolo", "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")

print(personas)
print(type(personas))