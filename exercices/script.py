temps = 6.892
distance = 19.7
vitesse = distance / temps
print ('vitesse={}'.format(vitesse)) 
Roundvitesse = round(vitesse , 1)
print (Roundvitesse)

#2
#f=3.123
from math import sqrt
f = float (input('entrez un nombre flottant'))
if f >= 0 :
    print (sqrt (f))
else: 
    print ("message d'erreur")

#2-1
a = "Bonjour"

b = "après"
print ("selon l'ordre lexicographique")
if a<b :
    print("a est situé avant b")
if a == b:
    print("a est égale à b")
if a>b :
    print("a est situé apès b")

    #2-1
    print ("entrez deux mots")
    a = len (input("un premier mot"))
    b = len(input("un deuxième mot"))
if a>b :
    print ("b est le plus petit")
else :
    print ("b est plus petit")

#3
a = 5
b = 10
while a<b :
    print("a a pour valeur",b)
    a = a + 1

#while b>0 :
    #print("b a pour valeur", b)        







