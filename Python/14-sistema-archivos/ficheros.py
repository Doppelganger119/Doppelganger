from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
print(ruta)
archivo = open(ruta,"+a")

# Escribir dentro de un archivo
archivo.write("*********Soy un texto metido desde python*********\n")

# Cerrar archivo
archivo.close()


# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
print(ruta)
archivo_lectura = open(ruta,"r")

# Leer contenido
#contenido =archivo_lectura.read()

# print(contenido)

# Leer contenido y guardar en lista
lista  = archivo_lectura.readline()
archivo_lectura.close()

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)
   # print("- " + frase)

# Copiar
ruta_original = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/ficheros_copiado88.txt"
#shutil.copyfile(ruta_original, ruta_alternativa)

"""

# Mover archivo y renombrarlo
ruta_original = str(pathlib.Path().absolute()) + "/ficheros_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/ficheros_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

# Eliminar
import  os

# os.remove(ruta_nueva)

# Comprobar si existe
import os.path

# print(os.path.abspath("../"))
ruta_comprobar = os.path.abspath("./") + "/ficheros_texto.txt"
print(ruta_comprobar)


if os.path.isfile(ruta_comprobar):
    print("El archivo existe ")
else:
    print("El archivo no existe")