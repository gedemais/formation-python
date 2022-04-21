#Écrire une fonction cube qui retourne le cube de son argument
import math 

def cube(x) :
    """fonction calculant le cube d'un nombre"""
    return x ** 3
x = int(input("Veuillez saisir un nombre : "))
print ("le cube de", x , "est :", cube(x))

from math import pi

def VolumeSphere(r) : 
    x == r
    V = 4 / 3 * pi * cube(r)
    """fonction permettant de calculer le volume d'une sphere avec le rayon r"""
    return (V)
r = int(input("veuillez saisir un nombre : "))
print("le volume de la sphere est ", VolumeSphere(r))