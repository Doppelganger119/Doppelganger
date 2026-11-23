"""
Ejercicio 5 Crear una LISTA CON EL CONTENIDO DE ESTA TABLA:


"""

tabla = [
    {
        "categoría": "ACCIÓN",
        "juegos": ["GTA", " Call of Duty", "PUGB"]
    },
    {
        "categoría": "AVENTURA",
        "juegos": ["ASSASINS", "Crash Bandicoot", "Pince of persia"]
    },
    {
        "categoría": "DEPORTES",
        "juegos": ["FIFA21", "PES 21", "MOTO GP 21"]
    }

]

for categoria in tabla:
    print(f"-------------{categoria['categoría']}------------")
    for juego in categoria['juegos']:
        print(juego)