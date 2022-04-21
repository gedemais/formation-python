#3.3
def cube(x) :
    return x ** 3
def mafonction(x) :
    return 2 * cube(x) + x - 5
def tabuler(mafonction, borneinf, bornesup, nbpas) :
    borneinf=int(input('saisir borneinf '))
    bornesup=int(input('saisir bornesup '))
    nbpas=int(input('saisir nbpas '))
    while borneinf < bornesup:
        print('la fonction esr ')
tabuler(mafonction, borneinf, bornesup, nbpas)



