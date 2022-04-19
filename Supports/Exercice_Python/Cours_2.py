"""
Cours 2
"""
import math;

a = float(input("Entrer un float : "))
racine = 0
if a >= 0.0 :
    racine = math.sqrt(a)
    print(racine)
else : print("Le chiffre est négatif")