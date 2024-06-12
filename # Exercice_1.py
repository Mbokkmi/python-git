# Exercice 1
# Écrire un programme qui permet de saisir deux entiers a et b, 
# calcule et affiche le quotient
# entier, le reste de la division, le ratio (quotient réel) et modulo.
a = int(input("entrer la valeur de a : "))
b = int(input("entrer la valeur de b : "))
if b == 0:
    print("Erreur : Division par zéro n'est pas autorisée.")
else:
    # Calcul du quotient entier
    quotient_entier = a // b
    # Calcul du reste de la division
    reste = a % b
    # Calcul du ratio (quotient réel)
    ratio = a / b
    # Calcul du modulo
    modulo = a % b

    # Affichage des résultats
    print(f"Quotient entier de {a} divisé par {b} : {quotient_entier}")
    print(f"Reste de la division de {a} par {b} : {reste}")
    print(f"Ratio (quotient réel) de {a} divisé par {b} : {ratio}")
    print(f"Modulo de {a} par {b} : {modulo}")
print("Fin")
