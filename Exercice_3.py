# Écrire un programme qui demande à l’utilisateur de donner le rayon d’un cercle et lui
# retourne sa surface et son périmètre.
rayon=float(input("Donner le rayon de cercle "))
perimetre= (2*3.14)*rayon
surface=3.14*(rayon**rayon)
print(f"la surface du cercle est {surface } et le perimetre est {perimetre}" )
