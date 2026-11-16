#  Inventario de una tienda. Gestiona el inventario de una tienda con un diccionario {producto: cantidad}. El programa muestra un menu en bucle 1) Añadir producto y cantidad (si ya existe suma cantidad) 2) Consultar cuantas unidades hay de un producto; 3) Listar todo el inventario 4) salir

inventario = {
    "Ratones": 1,
    "Placas": 3
}

while
    print("Menu")
    print("1 Añadir producto")
    print("2 Consultar unidades")
    print("3 Listar todo")
    print("4 Salir")

menu = input("Que quieres hacer?")
if menu == "1":
    