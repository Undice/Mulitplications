def afficherTable(valeur, min, max):
    if min > max :
        temp = max
        max = min
        min = temp

    for i in range(min, max+1):
        print(f"{i} x {valeur} = {i*valeur}")
        i+=1

valeur = input("De quel nombre voulez-vous connaitre la table ? ")
min = input("A partir de combien voulez-vous commencer la table ? ")
max = input("A partir de combien voulez-vous arreter la table ? ")
afficherTable(int(valeur), int(min), int(max))