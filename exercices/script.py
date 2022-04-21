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

#2.5 
n = int(input ("entrez un entier [1 .. 10]: "))
while not(1 <= n <= 10) :
    n = int(input ("entrez un entier [1 .. 10], SVP :"))
print("valeur saisie :", n)



#2.6
print("exemple 1")
for lettre in "bonjour":
    print(lettre)
print()

print("exemple 2")
for element in [1, 2, 3, 4, 5, 6, 7] :
    print(element)

#2.7
print(range(5))
print(range(3, 10))
print(range(0, 10, 2))
for i in range(0, 15, 3):
    print(i)
print()
  
#2.8
liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for element in liste :
    if element == "5":
        break
    print (element)

#2.9
liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for element in liste :
    if element == "5":
        continue
    print (element)


#3.1
def table(base, debut, fin, inc) :
    n = debut
    base = 2
    while n <= fin :
        print(n, 'x', base, '=', n * base )
        n = n + inc
table(2, 4, 8, 1)

#3.2    
from math import pi
def cube(x) :
    return x**3

def volumeSphere(r) :
    return 4* pi * cube(r) / 3
rayon = float(input("rayon : "))
print(volumeSphere)

#3.3
from math import sqrt


def cube(x) :
    return x ** 3

def mafonction(x) :
    return 2 * cube(x) + x - 5

def tabuler(mafonction, borneinf, bornesup, nbpas) :
    for x in range(borneinf, bornesup, nbpas):
        print(x)
        print(mafonction(x))

borneinf = int(input('saisir borneinf '))
bornesup = int(input('saisir bornesup '))
nbpas = int(input('saisir nbpas '))

while borneinf >= bornesup or nbpas <=0 :
        print('la fonction est ')
tabuler(mafonction, borneinf, bornesup, nbpas)

