temps= 6.892
distance= 19.7
vitesse=distance / temps
print(vitesse)



# Ex 2 
# 1)
#f=10.555
from math import sqrt
f = float (input('entrez un nombre flottant'))
if f >= 0 :
    print (sqrt (f))
else:
    print("message d'erreur")

# 2) comparer deux mots
print("entrez deux mots")
a = len(input("un premier mot"))
b = len(input("un deuxieme mot"))
if a>b :
    print("b est le plus petit")
else :
    print("a est le plus petit")

    #3) 

pseuil = 2.3
vseuil = 7.41
pression = float(input("entrez une pression"))
volume = float(input("entrez un volume"))
if pression < pseuil :
    print("OK")
else :
    print("Arrêt immédiat") 
if volume < vseuil :
    print ("OK")
else :
    print("Arrêt immédiat")

    