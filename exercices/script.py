temps= 6.892
distance= 19.7
vitesse=distance / temps
print(vitesse)



# Ex 2 
# 1)
#f=10.555
#from math import sqrt
#f = float (input('entrez un nombre flottant'))
#if f >= 0 :
  #  print (sqrt (f))
#else:
 #   print("message d'erreur")

# 2) comparer deux mots
#print("entrez deux mots")
#a = len(input("un premier mot"))
#b = len(input("un deuxieme mot"))
#if a>b :
 #   print("b est le plus petit")
#else :
  #  print("a est le plus petit")

    #3) 

# pseuil = 2.3
# vseuil = 7.41
# pression = float(input("entrez une pression"))
# volume = float(input("entrez un volume"))
# if pression < pseuil and volume < vseuil :
  #  print("OK")
# else :
  #  print("Arrêt immédiat !") 



# 4)
#a = 0
#b = 10
#while a < b : 
  #  print("valeur de a", a)
   # a = a + 1

#while b>0 :
#    if b % 2 != 0 :
    #    print("valeur de b" , b)
  #  b = b- 1 

n = int(input("entrez un entier [1 . . 10] : "))
while n<0 or n>10 :
    n = int(input("entrez un entier [1 . . 10], S.V.P. : "))
    print("valeur saisie :", n)

