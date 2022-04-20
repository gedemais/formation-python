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
a = 0
b = 10
while a<b :
    print("a a pour valeur",a)
    a = a + 1

#while b>0 :
    #if b % 2 != 0 :
        #print("b pour valeur", b)        
        #b = b - 1

#exercice 5
n = int(input("Entrez un entier [1 .. 10] : "))
while n<0 or n>10 :
    n = int(input("Entrez un entier [1 .. 10], : "))
    print("\nValeur saisie :", n)

#exercice6

print(" Exemple 1 ".center(40, '-'))
for lettre in "Bonjour":
    print(lettre)
    print()
for i in [0, 1, 2, 3]:
    print("i a pour valeur", i)


#3 Les fonctions

#def table(base , début , fin , inc)
    #Affichez la table

def table(base, debut, fin, inc):
    """Affiche la table des <base>, de <debut> a <fin>, de <inc> en <inc>."""
    n = debut
    while n <= fin:
        print(n, 'x', base, '=', n*base)
        n = n + inc



#fonction cube

def cube(x):
    """Calcule le cube de l'argument."""
    return x**3
def volumeSphere(r):
    """Calcule le volume d'une sphere de rayon <r>."""
    return 4 * pi * cube(r) / 3

  











