"""
Variables locales: SE DEFINEN DENTRO DE LA FUNCIÓN Y 
NO SE PUEDE USAR FUERA DE ELLA, SOLO EESTÁN DISPONIBNLES DENTRO.
a NO SER QUE HAGAMOS UN RETURN

VARIABLES GLOBALES: SON LAS QUE SE DECLARAN FUERA DE UNA FUNCIÓN
Y ESTÁN DISPONIBLES DENTRO Y FUERA DE ELLAS

"""

# Variable global

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola Mundo"    # Si comentas esta variable tomara la variable global anterior
    print("Dentro de la función: ")
    print(frase)

    year = 2021
    print(year)
    global website
    website = "victorroblesweb.es"
    print("Dentro: ",website)

    return "Dato devuelto" +" "+ str(year)

print(holaMundo())
print("Fuera: ", website)