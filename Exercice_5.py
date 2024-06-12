# Écrire un programme qui demande à l’utilisateur de donner la longueur et la largeur d’un
# rectangle puis affiche son périmètre, sa surface et la longueur d’un des diagonales.
longueur= float(input("Donner la longueur : "))
largeur= float(input("Donner la largeur : "))
perimetre=(longueur+largeur)*2
surface=(longueur*largeur)
diagonal=(longueur*longueur)+(largeur*largeur)
racine_diagonal = diagonal**0.5
print(f"le perimetre est : {perimetre} et la surface est : {surface} et le diagonale est : {racine_diagonal}  ")
