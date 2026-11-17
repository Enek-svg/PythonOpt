#  Inventario de una tienda. Gestiona el inventario de una tienda con un diccionario {producto: cantidad}. El programa muestra un menu en bucle 1) Añadir producto y cantidad (si ya existe suma cantidad) 2) Consultar cuantas unidades hay de un producto; 3) Listar todo el inventario 4) salir

tienda = {
    
}
while True:
    print("Menu")
    print("1 Añadir producto")
    print("2 Consultar unidades")
    print("3 Listar todo")
    print("4 Salir")

    menu = input("Que quieres hacer?")
    if menu == "1":
        producto = input("Que producto quieres añadir: ")
        cantidad = int(input("Cuantas unidades quieres añadir: "))
        if producto in tienda:
            tienda[producto] = tienda[producto] + cantidad
        else:
            tienda[producto] = cantidad
    elif menu == "2":
        consultar = input("Que producto quieres consultar? ")
        if consultar in tienda:
            print("Hay", tienda[consultar],"unidades de", consultar)
        else: 
            print("No hay ese producto")
    elif menu == "3":
        if len(tienda) == 0:
            print("La tienda esta vacia")
        else:
            print(tienda)
    elif menu == "4":
       print("Hasta luego.")
       break
    else:
        print("Opcion no valida")