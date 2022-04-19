#Cours n°1 premiers pas python

#1
#création variable temps = 6,892 et distance = 19,7

temps=6.892
distance=19.7

#calcul vitesse
vitesse=distance/temps

print("{:.1f}".format(vitesse))
""""
#2
#input nom, prénom, âge
prenom=input("Votre prénom : ")
nom=input("Votre nom : ")
age=input("Votre âge : ")
age=int(age)
print(prenom,"\t", nom,"\t", age ,"\t ans")
"""""

#raw input
name = raw_input("Votre nom et prénom : ")
age = raw_input("Votre âge : ")
age=int(age)
print(name, "\t", age)