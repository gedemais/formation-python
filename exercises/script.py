from math import sqrt
f = float (input("entrez un nombre flottant"))
if f>=0 : 
    print (sqrt(f))
else : 
    print ("erreur")

#QUEST2
print ("entrez deux mots")
a = len(input("un premier mot"))
b = len(input("un deuxieme mot"))
if a>b :
    print ("b est le plus petit")
else : 
    print ("b est le plus grand")

#QUEST3
Pseuil = 2.3
Vseuil = 7,41
Pression = float(input("valeur pression"))
Volume = float(input("valeur volume"))
if (Volume > Vseuil) and (Pression > Pseuil) :
    print ("arret immédiat")
