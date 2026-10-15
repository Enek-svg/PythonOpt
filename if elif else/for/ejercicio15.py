# Notas de la clase. Pregunta cuanto alumnos hay y pide la nota de cada uno. Si la nota no esta entre 0 y 10, vuelve a pedirla. al final muestra la media y el numero de aprobados.

cantidad = int(input("Cuantos alumnos hay: "))
notas = []
aprobados = 0
suma = 0

for i in range(cantidad):
    nota = float(input("Introduce la nota del alumno: "))
    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        nota = float(input("Introduce la nota del alumno: "))
    notas.append(nota)
    suma = suma + nota
    if nota >= 5:
        aprobados = aprobados + 1

if cantidad > 0:
    print("La media de la clase es:", suma / cantidad)
    print("Numero de alumnos aprobados:", aprobados)
else:
    print("No hay alumnos.")
