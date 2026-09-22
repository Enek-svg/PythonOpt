# (a) Muestra tu nombre
print("Enek")

# (b) Muestra tu edad y tu ciudad
print("Edad: 17")
print("Ciudad: Barakaldo")

# (c) Pide el nombre y saluda
nombre = input("Dime tu nombre: ")
print("Hola", nombre)

# (d) Pide dos números y muestra su suma
numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime otro número: "))
print("La suma es:", numero1 + numero2)

# (e) Pide el año de nacimiento y calcula la edad aproximada
edad = int(input("¿En qué año naciste? "))
actual = int(input("¿En qué año estamos? "))
edad2 = 2026 - edad
print("Tienes aproximadamente", edad2, "años")
print("Tienes aproximadamente", actual - edad, "años")

# (f) Escribe una frase y muéstrala en mayúsculas
frase = input("Escribe una frase: ")
print(frase.upper())

# (g) Pide una palabra y muestra su primera letra, su última letra y su longitud
palabra = input("Dime una palabra: ")
print("Primera letra:", palabra[0])
print("Última letra:", palabra[-1])
print("Longitud:", len(palabra))

# (h) Pide una frase y muestra cuántos caracteres tiene
frase = input("Escribe una frase: ")
print("Tiene", len(frase), "caracteres")

# (i) Pide un número y muestra su cuadrado y su cubo
numero = int(input("Dime un número: "))
print("Cuadrado:", numero ** 2)
print("Cubo:", numero ** 3)

# (j) Pide un precio y un descuento, y calcula el precio final
precio = float(input("Dime el precio: "))
descuento = float(input("Dime el descuento (%): "))
precio_final = precio - (precio * descuento / 100)
print("Precio final:", precio_final)

# (k) Convierte una cantidad de segundos en minutos y segundos
segundos = int(input("Dime los segundos: "))
minutos = segundos // 60
resto = segundos % 60
print(segundos, "segundos son", minutos, "minutos y", resto, "segundos")
