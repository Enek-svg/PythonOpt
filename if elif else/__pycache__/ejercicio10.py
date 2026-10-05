#a
"""
edad = int(input("Cual es tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#b
nota = int(input("Dime tu nota del examen: "))

if nota >= 5:
    print("Has aprobado")
else:
    print("Has suspendido")

#c
contraseña = input("Cual es la contraseña: ")
contraseña2 = "Prueba123"

if contraseña == contraseña2:
    print("Es esa la contraseña")
else:
    print("Contraseña incorrecta")
"""
#d
nota1 = int(input("Dime tu primera nota: "))
nota2 = int(input("Dime tu segunda nota: "))
nota3 = int(input("Dime tu tercera nota: "))

notamedia = (nota1 + nota2 + nota3) / 3

if notamedia >= 5:
    print("Has aprobado")
else:
    print("Has suspendido")

#e
hora = float(input("Que hora es (00.00): "))

if hora < 12.00:
    print("Buenos días")
elif hora < 19.00:
    print("Buenas tardes")
elif hora >= 19.00:
    print("Buenas noches")
else:
    print("No es una hora aceptada.")