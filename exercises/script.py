# affecter les variables
#temps = 6.892
#distance = 19.7
# définir la vitesse 
#vitesse = distance/temps
# afficher résultat de la vitesse
#print(vitesse)
#afficher un chiffre après la virgule
#print('vitesse={}'.format(vitesse))

#exercice 2
#1
#from math import sqrt
#f = float (input("entrer un nombre flottant"))
#if f >= 0:
#    print(sqrt(f))
#else:
#    print("erreur")


#2
#print("Entrer deux mots")
#a = len(input("a = "))
#b = len(input("b = "))

#if a < b:
#    print("le plus petit mot est a")
#else:
#    print("le plus petit mot est b")

#3
#p_seuil=2.3
#v_seuil=7.41
#p_courante = float(input("saisir la pression courante = "))
#v_courant= float(input("entrer le volume courant = "))
#if (p_courante > p_seuil) and (v_courant > v_seuil):
#    print("arrêt immédiat")
#elif p_courante > p_seuil:
#    print("augmenter le volume de l'enveinte")
#elif v_courant > v_seuil:
#    print("diminuer le volume de l'enceinte")
#else:
#    print("tout va bien")

#4
#a = 0
#b = 10
#while a < b :
#    print("a a pour valeur", a)
#    a = a + 1
#print("fin")

#b=10
#while b !=0 :
#    b= b-1
#    if b%2 ==1: ou if b%2 !=0:
#        print("b = ", b)
#print("fin")

#5
#n=int(input("entrer un entier compris dans [1;10]: "))
#while not (1<=n<=10):
#    n=int(input("entrer un entier compris dans [1;10]: "))
#print("valeur saisie", n)

#6
#for lettre in "maison":
#    print(lettre)
#print("fin")

#for i in range(10):
#    print(i)
#print("fin")

#7
#for i in range (1,14,3):
#    print(i)
#print("fin")

#8
#for i in range (1,11):
#    print(i)
#    if i == 5:
#        break
#print("fin")

#9
#for i in range (1,11):
#    if i ==5:
#        continue
#    print(i)
#print("fin")

#cours3
#1
#def table(base, debut, fin, inc):
#    n= debut
#    while n <= fin:
#        print(base, "x", n, "=", n*base)
#        n= n + inc

#table(6,1,10,1)

#2
from math import pi
def cube(n):
    return n**3
def volume_sphere(r):
    return 4 / 3 * (pi) * cube(r)
r = float(input("entrer la valeur du rayon: "))
print("le volume de cette sphere vaut", volume_sphere(r))
