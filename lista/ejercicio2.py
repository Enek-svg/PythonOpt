# ¿Está en Bizkaia? Crea una lista de pueblos de Bizkaia. Pide al usuario un pueblo y dile si está o no en la lista.

lista = ["Bermeo", "Getxo", "Lekeitio", "Plentzia", "Ea", "Gorliz", "Mundaka", "Balmaseda", "Gernika", "Elantxobe"]

pueblo = input("Dime un pueblo: ")

if pueblo in lista:
    print("Esta en la lista")
else:
    print("No esta en la lista")