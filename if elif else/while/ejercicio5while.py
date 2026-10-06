# Tabla de multiplicar del 1 al 10 usando while
numero = int(input("Ingrese un numero: "))

contador = 1
while contador <= 10:
    print(numero, "x", contador, "=", numero * contador)
    contador += 1