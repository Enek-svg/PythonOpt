# Crea un diccionario con 3 contactos (nombre --> departamento); después pide un nombre y muestra su departamento. Si no existe, avísalo.

personas = {
    "Carlos": "Ventas",
    "Juan": "Desarrollo",
    "Pablo": "Supervision"
}

nombre = input("Escribe un nombre: ")

if nombre in personas:
    print(nombre, "trabaja en", personas[nombre])
else:
    print("Ese nombre no existe en la lista.")