"""
Cours 3
"""

import math

# 1

def table (base:int, debut:int, fin:int, inc:int):
    while debut <= fin:
        print(debut*base)
        debut = debut + inc


# 2

def cube(nb:float):
    return(nb**3)

def volumeSphere(r:float):
    Volume = (4 * math.pi * cube(r)) / 3
    print(round(Volume, 2))

# 3

def maFonction(x:float):
    return(2*cube(x) + x - 5)

def tabuler(fonction, borneInf:float, borneSup:float, nbPas:float):
    if borneInf >= borneSup:
        print("Problemes de bornes !")
    while borneInf < borneSup:
        fonction = maFonction(borneInf)
        print(round(fonction, 2))
        borneInf = borneInf + nbPas

# 4

DA_1 = 10
DA_2 = 8
DA_3 = 6
MV = 18

def volMasseEllipsoide(DA_1, DA_2, DA_3, MV):
    Volume = ((4*math.pi)/3)*DA_1*DA_2*DA_3
    VM = (round(Volume, 2), MV)
    print(VM)
    return(VM)


# 5

def somme_tuple(liste:tuple):
    total = 0
    for n in liste :
        total = total + n
    print(total)
    return(total)

# 6

tup_a = (1, 10, 3)
def somme(a, b, c):
    print(a+b+c)
    return (a+b+c)
somme(*tup_a)