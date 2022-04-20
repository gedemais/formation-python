seuil_p = 2.3
seuil_v = 7.41
p = float (input("pression courant " ))
v = float (input("volume courant "))
if (p > seuil_p) and (c > seuil_v) :
    print("arret immédiat")
elif p > seuil_p :
    print("augmenter le volume de l'enceinte")
elif v > seuil_v :
    print("diminuer le volume")
else : 
    print("tout va bien")