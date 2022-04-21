import math
import numpy as np
#1 procédure table 
"""""
def table(base,debut,fin,inc):
    n=debut
    while n<=fin:
        print(n,'x', base, "=", n*base)
        n=n+inc

table(8,2,11,3)
"""""
#2 Calculer le volume d'une sphère en utilisant une fonction cube et une fonction volumesphere
"""""
def cube(nombre):
    return nombre**3
def VolumeSphere(rayon):
    volume=(4/3)*math.pi*cube(rayon)
    print(volume)

#appel fonction volumesphere
VolumeSphere(3)
"""""
#3 maFonction doit retourner f(x)=2x^3+x-5
"""""
def maFonction(x):
    return 2*x**3+x-5

#procédure tabuler(fonction,borneInf,BorneSup,nbPas) doit respecter borneInf<BorneSup
def tabuler(fonction,BorneInf,BorneSup,nbPas):

    while BorneInf>BorneSup:
        BorneInf=float(input("Entrez la borne inférieure : "))
        BorneSup=float(input("Entrez la borne supérieure : "))

    while nbPas>BorneSup or nbPas==0:
        nbPas=int(input("Entrez le pas : "))

    for i in np.arange (BorneInf,BorneSup,nbPas):
        print(fonction(i))      

BorneInf=float(input("Entrez la borne inférieure : "))
BorneSup=float(input("Entrez la borne supérieure : "))
nbPas=int(input("Entrez le pas : "))

tabuler(maFonction,BorneInf,BorneSup,nbPas)
"""""
#4 fonction VolMasseEllipsoide retourne volume et masse grâce à un tuple. 

def VolMasseEllipsoide(a,b,c,rho):
    volume=4/3*math.pi*a*b*c
    masse= volume*rho
    print("Le volume est de : ",volume, " et la masse est de : ",masse)

VolMasseEllipsoide(1,2,3,4)
