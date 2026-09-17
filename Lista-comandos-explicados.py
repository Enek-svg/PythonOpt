# LISTA
# str : cadenas de texto
# int : números enteros
# float : números decimales
# bool : valores booleanos (True o False)
# == : comparar valores
# = : Asignar valor a una variable

# >---------<

# Lo normal adentro de un print es poner texto entre comillas ya que si no lo pones entre comillas, el programa lo va a interpretar como si fuera una variable.
# Ejemplo: print("Hola mundo") # esto es un texto, por eso va entre comillas
# Ejemplo2: print(Hola mundo) # esto es un error, ya que el programa lo interpreta como una variable y no existe, entonces daria error ya que no hay ninguna variable con ese nombre.

# >---------<

# Variables 
# hola = "Hola mundo" # esto es una variable de tipo str, ya que es un texto (En este caso la variable se llama hola y su valor es "Hola mundo")
# Hola_2 = "Hola mundo 2" Las variables pueden tener _ que se usa como espacio.
# Como saber que tipo de variable es?
# print(type(hola)) # esto nos dice que tipo de variable es. La lista de la linea 1 es los tipos de variables que existen en python.

# >---------<

# Para que haya espacios bien hechos
# print(f"Hola {nombre2}, tienes {edad} años.")
# adentro de este print para que ponga esas variables en la pantalla, se pone el nombre de la variable y al principio coma, y si es un número entero o decimal al final tambien coma, y ademas se pone str() para que lo convierta a cadena de texto y lo pueda mostrar en pantalla.
# ejemplo: print("Hola ",nombre, " tienes ", str(edad), " años") # las comas hacen que funcione como un espacio entre las palabras, si no se ponen las comas, se juntan todas las palabras y no se entiende nada.

# OPERADORES ARITMÉTICOS
# Son matematicas básicas que se pueden hacer con números, como sumar, restar, multiplicar, dividir, etc.

# print (2 + 2) # suma
# print (2 - 2) # resta
# print (2 * 2) # multiplicación
# print (2 / 2) # división y para division entera se usa // y con el // se redondea hacia abajo
# print (9 % 2) # módulo (el resto de la división)
# print (2 ** 3) # potencia (2 elevado a 3)

# OPERACIONES MATEMATICAS CON STR
# SUMA --> Concadenar ejemplo: "nombre" + "apellido" = "nombreapellido" (sin espacio)
# RESTA --> Repetir ejemplo: "nombre" * 3 = "nombrenombrenombre" (repite el texto todas las veces que le digas)


# OPERADORES COMPARATIVOS
# Son operadores que comparan valores y devuelven un valor booleano (True o False)
# print(4 < 8) # menor que
# print(4 > 8) # mayor que
# print(4 <= 8) # menor o igual que
# print(4 >= 8) # mayor o igual que
# print(4 == 8) # igual que
# print(4 != 8) # diferente que
# = asignar
# == comparar
# ejemplo: print(5==5) # esto devuelve True ya que 5 es igual a 5
# ejemplo: print(5!=7) # esto devuelve False ya que 5 no es igual a 7

# SEPARAR MENSAJE
# con /n haces que el mensaje se vaya a la siguiente linea

# nombre ="Monica"
# print(nombre[2]) # esto imprime lo que esta en la posicion 2 de la variable
