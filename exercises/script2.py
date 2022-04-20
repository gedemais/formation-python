#QUEST3
Pseuil = 2.3
Vseuil = 7.41
Pression = float(input("valeur pression"))
Volume = float(input("valeur volume"))
if (Volume > Vseuil) and (Pression > Pseuil) :
    print ("arret immédiat")
if Pression > Pseuil :
    print ("augmentez le volume de l'enceinte")
if Volume > Vseuil :
    print ("diminuez le volume")
if (Volume < Vseuil) and (Pression < Pseuil) :
    print ("tout va bien")