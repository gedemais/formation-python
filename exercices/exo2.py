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

a=0
b=10
while(a<b):
    a+=1
while b!=0:
    b-=1
    if b%2==1: print(b)