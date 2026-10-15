# Cajero. Parte de un saldo de 1000$. Muestra un menú (1.Consultar 2.Ingresar 3.retirar 4.Salir) que se repirta hasta que el usuario elija salir. No se puede retirar mas dinero del que hay.

saldo = 1000

while True:
    print("\n--- Cajero ---")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    operacion = input("Que operacion quieres hacer: ")

    if operacion == "1":
        print("Tu saldo es", saldo)
    elif operacion == "2":
        cantidad = float(input("Cuanto dinero quieres ingresar: "))
        saldo = saldo + cantidad
        print("Has ingresado", cantidad, "euros.")
        print("Tu saldo ahora es", saldo)
    elif operacion == "3":
        cantidad = float(input("Cuanto dinero quieres retirar: "))
        if cantidad > saldo:
            print("No puedes retirar más dinero del que tienes.")
        else:
            saldo = saldo - cantidad
            print("Has retirado", cantidad, "euros.")
            print("Tu saldo ahora es", saldo)
    elif operacion == "4":
        print("Hasta luego.")
        break
    else:
        print("Opcion no valida.")
