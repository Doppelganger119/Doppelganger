"""
Ejercicio 4. crear un script que tenga 4 variables, una
lista, un string, un entero y un booleano y que imprima
un mensaje según el tipo de dato de cada variable. Usar funciones


"""

def traducirTipo(tipo):
    result= None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Número entero"
    elif tipo == bool:
        result = "Booleano"
    return result


def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = (f"Este dato es del tipo {traducirTipo(tipo)}")
    else:
        result = "El tipo de dato no es correcto"
    return result

mi_lista = ["Hola mundo", 77]
titulo = "Master en Python"
numero = 100
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))

