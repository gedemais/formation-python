temps = 6.892
distance = 19.7
vitesse = distance / temps
print ('vitesse{}' .format(vitesse))



from math import sqrt







#3) les fonctions
#1) 
#def table(base, debut, fin, inc) :
#  ""affiche la table des <base>, de <debut> a <fin>, de <inc>.""
 # n = debut
  # while n <= fin :
   #    print(n, 'x', base, '=', n*base)
    #   n = n + inc
#table (2, 1, 10, 2)

#2)
from math import pi
def cube (x) :
    """calcule le cube d'un nombre."""
    return x**3
x = int(input("Veuillez saisir un nombre: "))
print ("le cube de" , x , "est :" ,cube(x))

from math import pi
def Volumesphere(r) :
    v = 4 / 3 * pi * cube(r)
    return (v)
r = int(input("veuillez saisir un nombre :"))
print("le volume de la sphere est" ,Volumesphere(r))  
