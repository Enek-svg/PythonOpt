# Mi top de películas. Crea una lista con tus 5 películas favoritas y muéstralas numeradas así: "TOP 1: ...", "TOP 2: ..."

lista = ["La bola Negra", "Clayface", "Leones en invierno", "la invitacion", "Heart of the beast"]

for numero, pelicula in enumerate(lista, 1):
    print("TOP ", str(numero), ": ", pelicula)