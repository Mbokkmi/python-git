# Écrire un programme qui demande à l’utilisateur de donner la longueur et la largeur d’un
# rectangle puis affiche son périmètre, sa surface et la longueur d’un des diagonales.
longueur= float(input("Donner la longueur : "))
largeur= float(input("Donner la largeur : "))
perimetre=(longueur+largeur)*2
surface=(longueur*largeur)
print(f"le perimetre est {perimetre} est la surface est {surface}")