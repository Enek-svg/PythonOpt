# Cuenta atrás. Pide un número N y haz una cuenta atrás desde N hasta 1. Al final, muestra "¡Despegue!".

numero = int(input("Ingrese un número: "))

while numero >= 0:
    print(numero)
    numero -= 1 # Resta 1 al número en cada iteración hasta llegar a 0
    # o numero = numero - 1
print("¡Despegue!")