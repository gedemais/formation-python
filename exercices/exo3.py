import math
def table(base, debut, fin, inc):
    for i in range(debut, fin, inc):
        print(base[i])

#table([1,2,3,4,5,6,7,8,9,10],4,9,2)
def cube(nb):
    return math.pow(nb, 3)

def VolumeSphere(r):
    return 4*math.pi*cube(r)/3

#print(VolumeSphere(2))

def maFonction(x):
    return 2*math.pow(x,3)+x-5

def tabuler(fonction, borneInf, borneSup, nbPas):
    if borneInf > borneSup:
        print("Erreur la borne inférieur doit etre inferieur a la borne suppérieur")
    else:
        for i in range(borneInf, borneSup, nbPas):
            print("la valeur de la fonction pour", i, "est de", fonction(i))

#tabuler(maFonction,0,5,2)

def volMasseEllipsoide(axe1=2,axe2=2,axe3=2,MVolumique=30):
    volume = 4/3*math.pi*axe1*axe2*axe3
    masse = volume*MVolumique
    print("volume=",volume)
    print("masse=",masse)
    return [volume,masse]

#volMasseEllipsoide(1,1,1,5)

def somme(*args):
    total=0
    for i in args:
        total+=i
    return total

#print(somme(1,2,3,5,9))

def somme (n1,n2,n3):
    return somme(n1,n2,n3)

def unDictionnaire(dic):
    for item in dic.items():
        print("un couple du dic est",item)

dic = {"Mcdo":"burger","kfc":"poulet","vi long":"chinois"}
unDictionnaire(dic)