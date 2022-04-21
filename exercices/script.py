import math

#Cours n°1 premiers pas python

#1
#création variable temps = 6,892 et distance = 19,7
"""""
temps=6.892
distance=19.7

#calcul vitesse
vitesse=distance/temps

print("{:.1f}".format(vitesse))


#2
#input nom, prénom, âge
prenom=input("Votre prénom : ")
nom=input("Votre nom : ")
age=input("Votre âge : ")
age=int(age)
print(prenom,"\t", nom,"\t", age ,"\t ans")
"""""
#Cours n°2 Contrôle du flux d'instruction
#1 saisir un flottant. S'il est positif ou nul, afficher sa racine, sinon message d'erreur
"""""
nombre=float(input("Insérez un nombre : "))
if (nombre >= 0) :
    racine=nombre**(1/2)
    print(racine)
else:
    print("Nombre négatif ! ")  
"""""
#2 Saisir deux mots et les comparer pour trouver le plus petit (ordre lexicographique), afficher le résultat

mot1=input("Entrez le premier mot : ")
mot2=input("Entrez le deuxième mot : ")
if mot1>mot2:
    print("Le mot le plus petit est \t",mot2)
else: 
    print("Le mot le plus petit est \t",mot1)
"""""
#refaire en utilisant res = a if cdt else b

mot1=input("Entrez le premier mot : ")
mot2=input("Entrez le deuxième mot : ")
resultat= mot1 if mot1<mot2 else mot2
print("Le mot le plus petit est \t",resultat)
"""""
#3 sécuriser une enceinte pressurisée
"""""
pSeuil=2.3 #pression de seuil
vSeuil=7.41 #volume de seuil

#capturer pression et volume à un instant t
pression=float(input("Pression : "))
volume=float(input("Volume : "))

if pression>pSeuil and volume>vSeuil:
    print("Arrêt immédiat")
elif pression>pSeuil and volume<=vSeuil:
    print("Augmenter le volume de l'enceinte")
elif pression<=pSeuil and volume>vSeuil:
    print("Diminuer volume de l'enceinte")
else:
    print("Tout va bien")
"""""

#4 
"""""
a=0
b=10
# ecrire une boucle affichant et incrémentant la valeur de a=0  tant qu'elle reste inférieur à b=10
for a in range(a,b):
    if a<b:
        print(a)
"""""

# écrire une boucle décrémentant la valeur de b et affichant sa valeur si elle est impaire,
# boucler tant que b n'est pas nul
"""""
a=0
b=10
for b in range (b,a,-1):
    if (b % 2)>0:
        print(b)
"""""

#5 écrire une saisie filtrée d'un entier dans l'intervalle 1 à 10, borne comprises. 
# Afficher la saisie
"""""
entier=int(input("Entrez un entier entre 1 et 10 :"))
while not (1<=entier<=10):
    entier=int(input("Entrez un entier entre 1 et 10 :"))
print(entier)
"""""
#6 affichier chaque caractère d'une chaîne en utilisant une boucler for
"""""
chaine=input("Entrez une chaîne de caractère : ")
for character in chaine:
    print(character)
"""""

#afficher chaque élément d'une liste en utilisant une boucle for
"""""
liste=["Pierre", "Paul", "Jacques", "Louis"]
for character in liste:
    print(character)
"""""
#7 Afficher les entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for
#et l'instruction range
"""""
for i in range(0,15,3):
    print(i)
"""""
#8 Utiliser l'instruction break pour interromptre une boucle for d'affichage des entiers de 
# 1 à 10 compris lorsque la variable de boucle vaut 5
"""""
for i in range (0,10):
    print(i)
    if i==5:
        break
"""""
#9 utiliser l'nstruction continue pour modifier une boucle for d'affichage de tous entiers 
# de 1 à 10 compris sauf lorsque la variable de boucle vaut 5
"""""
for i in range (0,10):
    if i==5:
        continue
    else:
        print(i)
"""""

#10 utiliser une exception pour calculer, dans une boucle évoluant de -3 à 3 compris
#la valeur de sin(x)/x
"""""
for i in range (-3,3):
    try:    
        print(math.sin(i)/i)
    except Exception:
        print("Division par 0")
"""""

#11 Effectuer les saisies avec integerbox et affichages avec msgbox (module easygui). 
#Initialiser une liste avec 5 entiers au choix, puis saisir un entier
#Dans une boucle for, parcourir la liste. Si l'entier saisi appartient à la liste, le sauver
#et interrompre la boucle. Si la boucle est terminée, utiliser else pour afficher un message
#l'annonçant.
"""""
from easygui import * #je n'arrive pas à installer le module sur ma machine

text="Entrez un entier"
title = "Liste d'entier"
liste = [0,1,2,3,4,5,6,8,9,10]

n=integerbox(text,title)

for liste in range:
    if liste==n:
       print("Le nombre existe dans la liste")
       break
msg=msgbox("Liste terminée",title)
"""""