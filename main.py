from qc_pipeline.parser      import load_fasta
from qc_pipeline.stats       import stats_sequences
from qc_pipeline.composition import analyze_composition
from qc_pipeline.filter      import apply_filters

def main():
    file_path = "/Users/Matthieududek/Desktop/Projet_professionel/projet-qc-16s/data/sequences.fasta"
    sequences = load_fasta(file_path)
    stats = stats_sequences(sequences)
    composition = analyze_composition(sequences)
    results = apply_filters(sequences, composition)

    # ✅ DANS main() — indentés de 4 espaces
    print("=== STATISTIQUES GLOBALES ===")
    print(f"Nombre de séquences: {stats['count']}")
    print(f"Longueur min: {stats['min_length']}")
    print(f"Longueur max: {stats['max_length']}")
    print(f"Longueur moyenne: {stats['mean_length']:.2f}")
    print(f"Écart-type: {stats['std']:.2f}")
    print(f"N50: {stats['N50']}")

    print("\n=== RÉSULTATS DE FILTRAGE ===")
    print(f"Séquences passées: {len(results['passed'])}")
    print(f"Séquences échouées: {len(results['failed'])}")

    print("\n=== DÉTAILS DES ÉCHECS ===")
    for flag, count in results["flag_counts"].items():
        print(f"{flag}: {count}")

if __name__ == "__main__":
    main()