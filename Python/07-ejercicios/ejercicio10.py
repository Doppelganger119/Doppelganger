"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantosa han aprobado y cúantos han suspendido

"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuamtos alumnos tienes?:"))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno{contador}\"?: "))
    
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    
    
    contador += 1

print (f"Alumnos aprobados: {aprobados}")
print (f"Alumnos aprobados: {suspendidos}")