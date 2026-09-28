numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime otro número: "))
simbolo = input("Que simbolo de operación quieres usar: ")

if simbolo == "suma" or simbolo=="Suma":
    print("La suma es: ", numero1 + numero2)
elif simbolo == "resta" or simbolo=="Resta":
    print("La resta es: ", numero1 - numero2)
elif simbolo == "division" or simbolo=="Division":
    print("La division es: ", numero1 / numero2)
elif simbolo == "multiplicacion" or simbolo=="Multiplicacion":
    print("La multiplicacion es: ", numero1 * numero2)
else:
    print("Nada")