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
p_seuil = 2.3
v_seuil = 7.41
print("Pression seuil :", p_seuil, "Volume seuil :", v_seuil)
p_courante = float(input("Pression courante = "))
v_courante = float(input("Volume courant = "))
if (p_courante > p_seuil) and (v_courante > v_seuil):
    print("Arret immediat")
elif p_courante > p_seuil:
    print("Augmenter le volume de l'enceinte") 
elif v_courante > v_seuil:
    print("Diminuer le volume de l'enceinte") 
else:
    print("Tout va bien !") 
