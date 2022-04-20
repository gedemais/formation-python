n = int(input("entrez un entier [1 .. 10] : "))
while n < 0 or n > 10:
    n = int(input("entrez un entier [1 .. 10] : "))
    print("Valeur saisie :", n)