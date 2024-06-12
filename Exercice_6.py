#Exercice 6
# Écrire un algorithme qui demande de saisir deux heures (heure, minute et seconde). 
# Le programme affiche le nombre de secondes qui sépare ces deux heures.
heure = int(input("Entrez l'heure (0-23) : "))
minute = int(input("Entrez les minutes (0-59) : "))
seconde = int(input("Entrez les secondes (0-59) : "))
convertion=( heure * 3600) +( minute * 60) + seconde
print(f" {heure} heure {minute} minute {seconde} secondes est egale a {convertion} secondes" )