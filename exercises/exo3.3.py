import math

def cube(x):
    return x ** 3

def f(x) : 
    return 2 * cube(x) + x - 5

def tabuler(fonction, bornInf, borneSup, nbPas) : 
    for x in range (bornInf, borneSup, nbPas): 
        print("la valeur de x est" , x)
        print("f(x)=", f(x))

        
bornInf = int(input("Entrez une borne inferieure ->"))
borneSup = int(input("Entrez une borne superieure ->"))
nbPas = int(input("Entrez un nombre de pas ->"))

while nbPas <= 0 or bornInf >= borneSup: 
    print("Error in parameters !")
    bornInf = int(input("Entrez une borne inferieure ->"))
    borneSup = int(input("Entrez une borne superieure ->"))
    nbPas = int(input("Entrez un nombre de pas ->"))
tabuler(f, bornInf, borneSup, nbPas)

