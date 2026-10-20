# Media de notas. Pide notas al usuario una a una (hasta que escriba -1), guárdalas en una lista y al final muestra: cuántas notas hay, 
# la suma y la media. 

nota = float(input("Introduce una nota: "))
lista= []

while nota != -1:
    nota = float(input("Introduce una nota: "))
    lista.append(nota)
print(lista)



