def distance_haming(mot1, mot2):
    distance = 0
    for i in range(len(mot1)): # Recupère la longueur du premier mot
        if mot1[i] != mot2[i]: # Vérifie si la lettre du mot1 en position 'i' est la même ou non que celle du mot2
            distance = distance + 1 # SI ce n'est pas le cas un rajoute 1 à la distance
    return distance;

print(distance_haming("hache", "vache"))
print(distance_haming("savon","japon"))


