
"""
Modulos: Son funcionalidades ya hechas para reutilizar
https://docs.python.org/es/3/tutorial/modules.html

Podemos conseguir módulos que ya vienen en el lenguaje,
módulos en internet, y también podemos crear nustros m,ódulos
"""
# Importar módulo propio
#  import mimodulo
# from mimodulo import holaMundo

from mimodulo import *

#print(mimodulo.holaMundo("Victor Robles WEB"))
#print(mimodulo.calculadora)

print(holaMundo("Victor Robles WEB"))
print(calculadora(3, 5, True))

# Módulo fechas
import datetime

print(datetime.date.today()) 

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)
print(datetime.datetime.now().time())

# Módulo matemáticas
import math
print("Raiz cuadrada de 10", math.sqrt(10))
print("Número pi: ", float(math.pi))
print("Redondear: ", math.ceil(6.56789))
print("Redondear: ", math.floor(6.56789))

#Módulo random

import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))
