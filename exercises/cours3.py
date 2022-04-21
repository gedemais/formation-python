#1
def table(base, debut, fin, inc):
    n=debut
    while n <= fin :
        print(n, 'x', base, '=', n * base)
        n = n + inc
print('la table est')
table(1,1,9,2)

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
def f(x):
    return 2 * cube(x) + x - 5
def tabuler (f, borneinf, bornesup, nbpas):
    for x in range(borneinf, bornesup, nbpas):
        print('la valeur de x est',x)
        print('f(x)=',f(x))
borneinf=int(input('quelle est la borne inf?'))
bornesup=int(input('quelle est la borne sup?'))
nbpas=int(input('quelle est le nb de pas?'))
while nbpas <= 0 or borneinf >= bornesup:
    print('error')
    borneinf=int(input('quelle est la borne inf?'))
    bornesup=int(input('quelle est la borne sup?'))
    nbpas=int(input('quelle est le nb de pas?'))
tabuler(f, borneinf, bornesup, nbpas)

#4
from math import pi
def  volumeEllipsoide(a, b, c):
    return (4/3) * pi * a * b * c
def  masseEllipsoide(a,b,c):
    return volume * rho
print('le volume est', volumeEllipsoide, 'et la masse est', masseEllipsoide)
volumeEllipsoide(1, 1, 1)
