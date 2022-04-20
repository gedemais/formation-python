temps = 6.892
distance = 19.7
vitesse = distance / temps
print ('vitesse={}'.format(vitesse))



#ex 2 q1
#f=7.123 flottant
from math import sqrt
f = float (input('entrer un nombre flottant'))
if f >= 0 :
    print (sqrt (f))
else :
    print ("message d'erreur")

# ex2 q 2
print("entrez deux mots")
a = len(input("un premier mot"))
b = len(input("un deuxième mot"))
if a>b :
    print("b est le plus petit")
else :
    print("b est le plus grand")

#version compacte
print("entrez deux mots")
a = len(input("un premier mot"))
b = len(input("un deuxième mot"))
plus_petit = x if x < y else y

#2.3 sécuriser une enceinte pressurisée

seuil p = 2.3
seuil v = 7.41
p = float (input("pression courant " ))
v = float (input("volume courant "))
if (p > seuil p) and (c > seuil v) :
    print("arret immédiat")
elif p > seuil p :
    print("augmenter le volume de l'enceinte")
elif c > seuil v :
    print("diminuer le volume")
else print("tout va bien")

#2.4 boucle
a = 0
b = 10
while a < b :
    print("valeur de a", a)
    a = a + 1

while b > 0 :
    if b % 2 == 0 :
        print("valeur de b", b)
        b = b - 1












