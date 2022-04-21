def cube(x):
    """Calcule le cube de l'argument."""
    return x**3
x = int (input ("saisir un nombre"))
print("le cube de", x , "est" , cube(x))

from math import pi 

def volumesphere(r) :
    v = 4 / 3 * pi * cube(r)
    """formule de la fonction qui permet de calculer le volume d'une sphère"""
    return (v)
r = int(input("saisir un nombre : "))
print("le volume de la sphere ", volumesphere(r)) 

