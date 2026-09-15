numero = input("Dime el precio del producto: ")
cantidad = input("Cuanta cantidad de este producto has comprado: ")

calculo = int(numero) * int(cantidad)
iva = int(calculo) * 1.21

print(f"El subtotal es {calculo} y el coste total es: {iva} ")