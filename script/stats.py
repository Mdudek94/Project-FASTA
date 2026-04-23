# Statistiques globales du fichier FASTA
def stats_sequences(sequences):
    #ÉTAPE 1 — Extraire les longueurs de chaque séquence → liste de nombres
    lengths = []
    for r in sequences:
        lengths.append(r["length"]) #length provient de la liste sequences de load_fasta
    #ÉTAPE 2 — Calculer les stats sur cette liste
    count = len(lengths) #nombre total de séquences
    max_length = max(lengths) #longueur de la plus longue séquence
    min_length = min(lengths) #longueur de la plus courte séquence

    mean_length = sum(lengths)/count #longueur moyenne des séquences

    total = sum(lengths) #somme de toutes les longueurs
    cumul = 0
    N50 = 0 # longueur de la sequence pour laquelle la somme cumulée des longueurs est à 50% du total
    for l in sorted(lengths,reverse =True): #parcours liste triée de la plus longue à la plus courte
     cumul += l # ajoute a chaque iteration une sequence a la somme cumulée
     if cumul >= total/2: # test si la somme cumulée dépasse la moitié du total
        N50 = l
        break

    #ÉTAPE 3 — Stocker les résultats dans un dict et le retourner
    stats ={"count": count, #nombre total de séquences
             "min_length" : min_length, #longueur de la plus courte séquence
             "max_length" : max_length, #longueur de la plus longue séquence
             "mean_length" : mean_length,
             "std" : (sum((x - mean_length)**2 for x in lengths) / count) ** 0.5,
             # somme de l'ecart a la moyenne au carré divisé par l'effectif de la série
             "N50" : N50
    }  
    return stats