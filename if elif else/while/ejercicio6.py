# Suma hasta el cero. Pide números uno a uno y ve sumandolos. Cuando el usuario escriba 0, deja de pedir y muestra la suma total

suma = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma = suma + numero
    numero = int(input("Ingrese un número: "))
print("La suma total es", suma)