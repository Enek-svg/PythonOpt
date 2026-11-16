# Crea un diccionario con 3 contactos (nombre --> departamento) después pide un nombre y muestra su departamento. Si no existe, avísalo.

"""
personas = {
    "Carlos": "Ventas",
    "Juan": "Desarrollo",
    "Pablo": "Supervision"
}

# Modificación de un valor
personas["Juan"]= "Ventas"

# Añadir a una persona con su departamento
personas["Bob"]= "Supervision"

nombre = input("Escribe un nombre: ")

if nombre in personas:
    print(nombre, "trabaja en", personas[nombre])
else:
    print("Ese nombre no existe en la lista.")

print(personas)

"""
departamentos = {
    "Marketing": ["Iker", "Naroa", "Eneko"],
    "Ventas": ["Carlos", "Osuna"],
    "Analytics": "Asier"
}

departamentos["Marketing"].append("Alex")
# departamentos["Marketing"].inser(1, "Alex") Lo pone en el numero 1.
print(departamentos["Marketing"])