from math import sqrt
f = float (input("entrez un nombre flottant"))
if f>=0 : 
    print (sqrt(f))
else : 
    print ("erreur")

#QUEST2
print ("entrez deux mots")
a = input("un premier mot")
b = input("un deuxieme mot")
if a>b :
    print ("b est le plus petit")
else : 
    print ("b est le plus grand")