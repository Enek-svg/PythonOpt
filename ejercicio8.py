nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
correo = input("Ingrese su correo electrónico: ")

# Ejercicio 8. El programa pedirá: nombre, apellido, edad, ciudad y correo. Con esos datos debe mostrar una ficha ordenada, incluyendo un campo Usuario generado automáticamente: la primera letra del nombre + el apellido en minúsculas ejemplo: (Ane Gil → agil). 

print("=============================== \n CARNÉ DIGITAL \n===============================")
print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Edad: " + edad)
print("Ciudad: " + ciudad)
print("Correo electrónico: " + correo)
print("Usuario: " + nombre[0].lower() + apellido.lower())
print("===============================")