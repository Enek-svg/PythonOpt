# Ejercicios cortos de listas.
# (a) Crea una lista con 5 colores y muestra el primero y el último.
# (b) Crea una lista con 5 números y muestra su suma.
# (c) Añade un elemento con append().
# (d) Elimina un elemento con remove().
# (e) Recorre una lista de nombres y saluda a cada persona.
# (f) Pide 5 números al usuario y guárdalos en una lista.
# (g) Cuenta cuántas veces aparece un número dentro de una lista (método .count()).
# (h) Ordena una lista de números con .sort().

# a)
listacolores = ["Rojo", "Azul", "Rosa", "Verde", "Negro"]

for i, color in enumerate(listacolores):
    if i == 0:
        print("El primer color es:", listacolores[0])
    if i == len(listacolores) -1:
        print("El ultimo color es:", listacolores[4])

# b)
listanumeros = [5, 7, 9, 3, 4]

suma = 0
for numero in listanumeros:
    suma += numero

print("La suma de todo es:", suma)

# c)
lista = ["Test1","Test2","Test3"]

for i in range(1):
    añadir = input("Que quieres añadir?: ")
    lista.append(añadir)
print(lista)

# d
listaeliminar = ["Prueba1", "Prueba2", "Prueba3"]
print("Lista original:", listaeliminar)
borrar = input("Dime que elemento quieres borrar: ")
borrar = borrar.capitalize()
listaeliminar.remove(borrar)
print("Lista después de eliminar:", listaeliminar)

print("-------------------")

# e)
listanombres = ["Ana", "Luis", "Marta"]

for nombre in listanombres:
    print("Hola,", nombre)

print("-------------------")

# f)
numerosusuario = []

for i in range(5):
    numero = int(input("Introduce un número: "))
    numerosusuario.append(numero)

print("Los números introducidos son:", numerosusuario)

print("-------------------")

# g)

listacontar = [2, 5, 2, 8, 2, 9]
print(listacontar)
numeroabuscar = int(input("¿Qué número quieres contar?: "))
cantidad = listacontar.count(numeroabuscar)

print("El número aparece", cantidad, "veces.")

print("-------------------")

# h)
listaordenar2 = [7, 3, 9, 1, 5]
listaordenar2.sort()
print("Lista ordenada:", listaordenar2)