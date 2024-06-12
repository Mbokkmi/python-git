# Écrire un programme qui demande à l’utilisateur de donner une somme en CFA, puis
# détermine et affiche sa correspondance en DOLLAR $ et en LIVRE STERLING £.
somme_en_cfa=float(input("Entrer la somme en en CFA : "))
dollard=somme_en_cfa/610
livre_sterling=somme_en_cfa/782
print(f"{somme_en_cfa} est egale a {dollard} Dollard et {livre_sterling} livre Sterling")

