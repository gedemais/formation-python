"""
Cours 2

import math
from multiprocessing.connection import Listener
from operator import length_hint;

"""
1
"""
a = float(input("Entrer un float : "))
racine = 0
if a >= 0.0 :
    racine = round(math.sqrt(a), 2)
    print(racine)
else : print("Le chiffre est négatif")

"""
2
"""
b = input("Entrer un mot : ")
c = input("Entrer un mot : ")
len_b = len(b)
len_c = len(c)
if len_b > len_c:
    print("Le premier mot est plus long")
else :
    print("Le deuxieme mot est plus long")

"""
3
"""
def check_status(Pression:float, Volume:float):
    pSeuil = 2.3
    vSeuil = 7.41
    if (Pression > pSeuil and Volume > vSeuil):
        print("Arret immediat")
    elif (Pression > pSeuil and Volume <= vSeuil):
        print("Augmenter le volume")
    elif (Pression <= pSeuil and Volume > vSeuil):
        print("Diminuez le volume")
    else :
        print("Tout va bien")
check_status(float(input("Pression ? ")), float(input("Volume ? ")))

"""
4
"""
A = 0
B = 10
while A<B : 
    A = A + 1
    print(A)
while B != 0:
    if B%2 == 1:
        print(B)
    B = B - 1

"""
5
"""

n = int(input("Entrez un nombre entre 1 et 10 : "))
while (n < 1 or n > 10) :
    n = int(input("Essaye encore :"))
print(n)


6
"""

Phrase = input("Entrer une phrase : ")
Liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in Phrase :
    if n == "\o":
        break
    print(n)
for n in Liste :
    if n == "\o":
        break
    print(n)
