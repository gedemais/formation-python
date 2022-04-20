# ex2 q 2
print("entrez deux mots")
a = len(input("un premier mot"))
b = len(input("un deuxième mot"))
if a>b :
    print("b est le plus petit")
else :
    print("b est le plus grand")

# version compacte
print("entrez deux mots")
a = len(input("un premier mot"))
b = len(input("un deuxième mot"))
plus_petit = x if x < y else y