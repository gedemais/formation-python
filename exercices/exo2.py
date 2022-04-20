import math
import easygui

#print('Entrer un nombre relatif:')
#nb=float(input())
#if nb>=0:
#    print('la racine du nombre est',nb**(0.5))
#else:
#    print('Racine impossible à calculer')

#mot1=input('Comparateur:Entrer un mot:')
#mot2=input('Comparateur:Entrer un 2eme mot:')
#res= mot1 if mot1<mot2 else mot2
#print('le mot le plus petit est',res)

#pSeuil=2.3
#vSeuil=7.41
#print('Entrer la pression:')
#p=float(input())
#print('Entrer le volume:')
#v=float(input())
#if p>pSeuil and v>vSeuil:
#    print('Arret immédiat')
#elif p>pSeuil:
#    print('Augmenter le volume de l\'enceinte')
#elif v>vSeuil:
#    print('Diminuer le volume de l\'enceinte')
#else:
#    print('Tout va bien')

#a=0
#b=10
#while(a<b):
#    a+=1
#while b!=0:
#    b-=1
#    if b%2==1: print(b)

#n = int(input('Entrez un entier entre 1 et 10 : '))
#while not(1 <= n <= 10) :
#    n = int(input('Entrez un entier entre 1 et 10, S.V.P. : '))

#ch='Hello world!'
#l= [1,2,4,5,8,9,15,51,35,96]
#for lettre in ch:
#    print(lettre)
#for chiffre in l:
#    print(chiffre)

#for c in range(0,15,3):
#    print(c)

#for c in range(11):
#    if c == 5:
#        break
#    print(c)

#for c in range(11):
#    if c == 5:
#        continue
#    print(c)

#for c in range (-3,3):
#    try:
#        print(math.sin(c)/c)
#    except ZeroDivisionError as err:
#        print('calcul impossible')

i1=easygui.integerbox("Entrer votre 1er entier","selection")
i2=easygui.integerbox("Entrer votre 2eme entier","selection")
i3=easygui.integerbox("Entrer votre 3eme entier","selection")
i4=easygui.integerbox("Entrer votre 4eme entier","selection")
i5=easygui.integerbox("Entrer votre 5eme entier","selection")
li=[i1,i2,i3,i4,i5]
slt=easygui.integerbox("Entrer l'entier à trouver","selection")
trouve=0
for i in li:
    if i==slt:
        trouve=i
        break

if trouve==0:
    easygui.msgbox("entier non trouvé")
else:
    easygui.msgbox("entier trouvé:")

#slt2=integerbox("Entrer l'entier à trouver","selection",0,0)
