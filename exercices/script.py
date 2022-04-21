#temps= 6.892
#distance= 19.7
#vitesse=distance / temps
#print(vitesse)



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

#n = int(input("entrez un entiercompris dans [1;10] : "))
#while not (1<=n<=10) :
 #   n = int(input("entrez un entier compris dans[1;10] : "))
  #  print("valeur saisie :", n)

#print("caractère d'une chaine")
#for lettre in "Hello" :
  #    print(lettre)

#3) les fonctions
#1)table de multiplication

#def table(base, debut, fin, inc) :
 #   """affiche la table des <base>, de <debut> a <fin>, de <inc> en <inc>."""
  #  n = debut
   # while n <= fin : 
    #    print(n, 'x', base, '=', n*base)
     #   n = n + inc
#table (2, 1, 10, 2)

#2) calcule de volume d'une sphère 

def cube(x) : 
  """fonction calculant le cube d'un nombre"""
  return x ** 3
x = int(input("entrez un nombre :"))
print("le cube de", x, "est :", cube(x))

from math import pi

def volumesphere(rayon):
    x == r
    volume = 3 / 4 * pi * cube(rayon)
    """fonction permettant de calculer le volume d'une sphere avec le rayon r"""
    return (volume)
r = int(input("saisir un nombre :"))
print("volume de la sphere est", volumesphere(r))

#3) fonction tabuler avec quatre paramètres

def cube(x):
    return x ** 3
      

def f(x):
    return 2 * cube(x) + x - 5


def tabuler(function, borne_inferieure, borne_superieure, nb_pas):
    if nb_pas <= 0 or borne_inferieure >= borne_superieure:
        print("erreur in parametres")
        exit()

borne_superieure = int(input("entrez une borne superieure"))
borne_inferieure = int(input("entrez une borne inferieure"))


tabuler(f, borne_inferieure, borne_superieure, 1)






