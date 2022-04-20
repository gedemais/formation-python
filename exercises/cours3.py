#1
def table(base, debut, fin, inc):
    x = debut
    y = fin
    while x < fin:
        print(x,y)
        x = x + inc
table(1, 2, 3, 4)

#2
from math import pi
def cube(x):
    return x**3
def volumeSphere(r):
    return 4 * pi * (cube(r) / 3)
r=float(input('introduire le rayon '))
print('pour un rayon de') 
print(r)
print('le volume est de') 
print(volumeSphere(r))

#3
def cube(x):
    return x**3
def mafonction(x):
    return 2 * cube(x) + x - 5
def tabuler(fonction, borneinf, bornesup, nbpas):
    while borneinf < bornesup:
    print(mafonction(x))


