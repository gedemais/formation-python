#1
#temps = 6.892
#distance = 19.7
#vitesse = distance/temps
#2 print(vitesse)
#print('vitesse={}'.format(vitesse))

# Cours 2

# 1
#x = 1.5
#if x >= 0 :
    #print(x**(0.5))
#else:
    #print("Erreur")

# print(pow(x,0.5))


#from math import sqrt
#x = float(input("Entrez un nombre flottant "))
#if x >= 0 :
    #print(sqrt(x))
#else :
    #print("Erreur")


# 2
#print("Entrer deux mots")
#a = len(input("a = "))
#b = len(input("b = "))

#if a < b:
    #print("Le plus petit mot est a")
#else:
    #print("Le plus petit mot est b")


#3
#p_seuil = 2.3
#v_seuil = 7.41
#print("Pression seuil :", p_seuil, "Volume seuil :", v_seuil)
#p_courante = float(input("Saisir la pression courante = "))
#v_courant = float(input("Saisir le volume courant = "))
#if (p_courante > p_seuil) and (v_courant > v_seuil):
    #print("Arret immediat")
#elif p_courante > p_seuil:
    #print("Augmenter le volume de l'enceinte") 
#elif v_courant > v_seuil:
    #print("Diminuer le volume de l'enceinte") 
#else:
    #print("Tout va bien !") 

#4
#a = 0
#b = 10

#while a < b:
    #print("a =", a)
    #a = a + 1
#print("fin)")

#while b != 0:
    #b = b - 1
    #if b%2 == 1:
        #print("b =", b)
#print("fin")

#5
#n = int(input("Entrez un entier entre 1 et 10 : "))
#while not (1<= n <= 10):
    #n = int(input("Entrez un entier entre 1 et 10 : "))
#print("Valeur saisie = ", n)

#6
#for lettre in "maison":
    #print(lettre)
#print("fin")

#for i in range(10):
    #print(i)
#print("fin")

#7
for i in range (1, 14, 3):
    print(i)
print ("fin")