# OPERACIONES
""""
print(5+3)
print(5-3)
print (3-5)
print(5*3)
print(5**3) 
print(5/3)
print(5//3)
"""

base = input("Dame una base: ")
altura = input("Dame una altura: ")
print("El area es: " + str(int(base) * int(altura)))
print("El perimetro es: " + str(2 * int(base) + 2 * int(altura))) 

base2 = float(input("Dame una base: "))
altura2 = float(input("Dame una altura: "))

area2= base2*altura2
print(f"El area es: {area2}")
perimetro2 = 2*base2 + 2*altura2
print(f"El perimetro es: {perimetro2}")