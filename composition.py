from math import log2

def analyze_composition(sequences):
    composition = []
    for r in sequences:
        seq = r["sequence"]

        gc_percent = (seq.count("G") + seq.count("C")) / len(seq) * 100
        n_percent  = seq.count("N") / len(seq) * 100

        freq_a = seq.count("A") / len(seq)
        freq_t = seq.count("T") / len(seq)
        freq_g = seq.count("G") / len(seq)
        freq_c = seq.count("C") / len(seq)

        entropy = 0
        for freq in [freq_a, freq_t, freq_g, freq_c]:
            if freq > 0:                        #if freq > 0 Si une base est absente (fréquence = 0), log2(0) plante.
                
                entropy -= freq * log2(freq)

        composition.append({
            "id":         r["id"],
            "gc_percent": gc_percent,
            "n_percent":  n_percent,
            "entropy":    entropy
        })

    return composition