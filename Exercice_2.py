# Exercice 2
# Écrire un programme qui demande à l’utilisateur de donner une mesure en dm
# puis détermine et affiche la correspondance en m, mm, cm, hm.
a=int(input("Donner une mesure en dm : "))
m=a/10
mm=a*100
cm=a*10
hm=a/100
print(a, " dm egale : ", m, "m")
print(a, " dm egale : ", mm, "mm")
print(a, " dm egale : ", cm, "cm" )
print(a, "dm  egale : ",  hm , "hm")