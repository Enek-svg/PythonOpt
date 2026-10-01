contraseña = "Naim67"
intentos = 0

while intentos <= 3:
    ingreso = input("Ingrese la contraseña: ")
    if ingreso == contraseña:
        print("Acceso concedido")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intentos restantes: {3 - intentos}")
else:
    print("Has agotado todos los intentos. Acceso denegado.")