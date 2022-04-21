from math import sqrt


def cube(x) :
    return x ** 3

def mafonction(x) :
    return 2 * cube(x) + x - 5

def tabuler(mafonction, borneinf, bornesup, nbpas) :
    for x in range(borneinf, bornesup, nbpas):
        print(x)
        print(mafonction(x))

borneinf = int(input('saisir borneinf '))
bornesup = int(input('saisir bornesup '))
nbpas = int(input('saisir nbpas '))

while borneinf >= bornesup or nbpas <=0 :
        print('la fonction est ')
tabuler(mafonction, borneinf, bornesup, nbpas)


