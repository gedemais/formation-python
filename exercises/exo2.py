#Exercice 2
#1 flottant
from math import sqrt
a=float(input('entrer le flottant '))
if a >= 0:
    print (sqrt (a))
else:
    print('erreur')
#2 mots
print('saisir deux mots ')
mot1=(input('mot1='))
len(mot1)
mot2=(input('mot2= '))
len(mot2)
if mot1 < mot2 :
    print('le mot le plus petit est le mot1')
else :
    print('le mot le plus petit est le mot2')
#2eme partie de la question2 avec res if else
mot1=court
mot2=long
if mot1 < mot2:
    print('le mot le plus petit est le mot1')
else :
    print('le mot le plus petit est le mot2')
#3 enceinte pressurisée
pSeuil= 2.3
vSeuil = 7.41
pression=input('entrer la pression courante ')
volume=input('entrer le volume courant ')
if pression > pSeuil and volume > vSeuil :
    print('arrêt immédiat')
elif pression > pSeuil and volume < vSeuil :
    print('augmenter le volume de lenceinte')
elif volume > vSeuil and pression < pSeuil :
    print('diminuer le volume de lenceinte')
else :
    print('tout va bien')
