temps = 6.892
distance = 19.7
vitesse = distance/temps
print('vitesse={}'.format(vitesse))

#2.1
from math import sqrt
a = float(input('saisir un nombre flottant'))

if a >= 0:
    print (sqrt (a))
else: 
    print ("erreur")


    #2.2

mot1 = 'soleil'

mot2 = 'plenete'

if len(mot1) > len(mot2):
    print (mot2)
elif len(mot1) == len(mot2):
    print ('les mots ont la meme longueur')
else:
    print (mot1)

    #2.3

    pSeuil = 2.3
    vSeuil = 9.3

    if pSeuil > 2.3 and vSeuil > 7.41:
        print ('arret immediat')
    elif pSeuil > 2.3 and vSeuil <= 7.41:
        print ('augmenter le volume')
    elif pSeuil <= 2.3 and vSeuil > 7.41:
        print ('diminuer le volume')
    else:
        print('tout va bien')