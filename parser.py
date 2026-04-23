from Bio import SeqIO

file_path = "/Users/Matthieududek/Desktop/Projet_professionel/projet-qc-16s/data/sequences.fasta"
def load_fasta(file_path):
    """
    Charge un fichier FASTA et retourne une liste de dictionnaires.
    Chaque dictionnaire contient les infos d'une séquence.
    """

    sequences = []

    with open(file_path, "r") as f: # Ouvre le fichier en mode lecture mais fonctionne sans
        for record in SeqIO.parse(f, "fasta"): # Utilise SeqIO pour parser le fichier FASTA, chaque record correspond à une séquence

            seq_str = str(record.seq).upper() # Convertit la séquence en majuscules pour uniformiser
#str permet de convertir l'objet Seq en une chaîne de caractères classique
#upper() met tout en majuscules pour éviter les problèmes de casse (A vs a)
            sequences.append({ 
                "id": record.id,
                "description": record.description,
                "sequence": seq_str,
                "length": len(seq_str)
            })

    return sequences    