espacio = 10
ocupado = 0
vehiculo = []
while True:
    print("==== MENU ====")
    print("Opcion 1. Entrada de Vehiculo")
    print("Opcion 2. Salida del Vehiculo")
    print("Opcion 3. Estado de Parking")
    print("Opcion 4. Cancelar y salir")
    operacion = input("Introduce el numero de la operacion que deseas realizar: ")

    if operacion == "1":
        vehiculos = input("Introduce la matricula de tu coche: ")
        vehiculo.append(vehiculos)
        print("Todavia quedan espacios en el Parking puedes entrar")
        espacio = espacio - 1
        if espacio < ocupado:
            print("No hay espacio de sobra en el Parking")
    elif operacion == "2":
        print("Adios gracias por usar el Parking")
        espacio = espacio + 1
        if espacio > ocupado:
            print("El Parking esta vacio")
    elif operacion == "3":
        print("En este parking estan los vehiculos con estas matriculas", vehiculo ,"dentro")
        print("En el parking todavia quedan", espacio ,"libres")
    elif operacion == "4":
        print("Hasta luego.")
        break
    else:
        print("Opcion no valida.")
