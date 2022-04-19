"""
Cours 2
"""
import math
from operator import length_hint;

a = float(input("Entrer un float : "))
racine = 0
if a >= 0.0 :
    racine = round(math.sqrt(a), 2)
    print(racine)
else : print("Le chiffre est négatif")

b = input("Entrer un mot : ")
c = input("Entrer un mot : ")
len_b = len(b)
len_c = len(c)
if len_b > len_c:
    print("Le premier mot est plus long")
else :
    print("Le deuxieme mot est plus long")