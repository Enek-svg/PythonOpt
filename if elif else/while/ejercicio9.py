# Adivina el numero, numero fijo y tienen 3 intentos para adivinarlo.
# Si acierta felicita y termina juego, si su numero es menor que el secreto,
# se le dice "El numero es mayor", si es mayor "el número menor" Si agota los 3 intentos se le dice el numero.

numero_secreto = 7
intentos = 3


while intentos > 0:
    numero = int(input("Adivina el número secreto: "))
    if numero == numero_secreto:
        print("Felicidades, has adivinado el numero")
        break 
    elif numero < numero_secreto:
        print("El numero es mayor")
        intentos = intentos - 1
    elif numero > numero_secreto:
        print("El numero es menor")
        intentos = intentos - 1
else:
    print("Has gastado ya tus 3 intentos")
