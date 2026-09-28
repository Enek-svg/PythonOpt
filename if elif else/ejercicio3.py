primero = int(input("Ingrese el primer número: "))
segundo = int(input("Ingrese el segundo número: "))
tercero = int (input("Ingrese el tercer número: "))
#Muestra cual es el numero mas grande de los tres
if primero >= segundo and primero >= tercero:
    print("El numero mas grande es el primero con el numero", primero)
elif segundo >= primero and segundo >= tercero:
    print("El numero mas grande es el segundo con el numero", segundo)
else:
    print("El numero mas grande es el tercero con el numero", tercero)
