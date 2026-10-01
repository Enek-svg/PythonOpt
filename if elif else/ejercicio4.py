numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime otro número: "))
simbolo = input("Que simbolo de operación quieres usar: ")
# Con .lower() no hace falta comprobar las opciones con mayúsculas y minúsculas.
# simbolo = simbolo.lower()

if simbolo == "suma" or simbolo=="Suma" or simbolo=="+":
    print("La suma es: ", numero1 + numero2)
elif simbolo == "resta" or simbolo=="Resta":
    print("La resta es: ", numero1 - numero2)
elif simbolo == "division" or simbolo=="Division":
    if numero2 == 0:
        print("No se puede dividir entre cero.")
    else:
        print("La division es: ", numero1 / numero2)
elif simbolo == "multiplicacion" or simbolo=="Multiplicacion":
    print("La multiplicacion es: ", numero1 * numero2)
else:
    print("Vuelve a escribir la operación no encontrada.")