#Exercice 2
#1 flottant
from math import sqrt
a=float(input('entrer le flottant '))
if a >= 0:
    print (sqrt (a))
else:
    print('erreur')

#2 mots (à refaire)
print('saisir deux valeurs ')
valeur1=int(input('valeur1='))
valeur2=int(input('valeur2= '))
if valeur1 < valeur2 :
    print('la plus petite est valeur1')
else :
    print('la plus petite est valeur2')


#3 enceinte pressurisée
pSeuil= 2.3
vSeuil = 7.41
pression=float(input('entrer la pression courante '))
volume=float(input('entrer le volume courant '))
if pression > pSeuil and volume > vSeuil :
    print('arrêt immédiat')
elif pression > pSeuil and volume < vSeuil :
    print('augmenter le volume de lenceinte')
elif volume > vSeuil and pression < pSeuil :
    print('diminuer le volume de lenceinte')
else :
    print('tout va bien')

#4
a = 0
b = 10
while a < b :
    print(a , end=" ")
    a = a+1 
print ('boucle de a et b') 
while b:
    b = b-1
    if b % 2 != 0:
        print( b , end=" ")
print('boucle de b')

#5 
n = int(input('Entrez un entier entre 1 et 10 [1 .. 10] : '))
print ('la valeur saisie est ',n)

#6 
for lettre in 'mardi':
    print (lettre)
print('element liste')
for n in [1, 'a', 8]:
    print(n)

#7
for n in range(0, 15, 3):
    print(n)

#8
for n in range(1, 11):
    if n == 5:
        break 
    print (n)

#9
for n in range(1, 11):
    if n == 5:
        continue
    print (n)

#10
from math import sin
for n in range(-3, 4):
    try:
        print (math.sin(n)/n)
    except :
        print('résultat non disponible')