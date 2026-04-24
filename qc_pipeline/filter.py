def apply_filters(sequences, composition):
    CONFIG = {
        "min_length":  50,
        "max_length":  600,
        "min_gc":      40.0,
        "max_gc":      75.0,
        "max_n":       5.0,
        "min_entropy": 1.0
    }

    passed      = []
    failed      = []
    flag_counts = {}

    for r, c in zip(sequences, composition):
        flags = []

        if r["length"] < CONFIG["min_length"]:  flags.append("too_short")
        if r["length"] > CONFIG["max_length"]:  flags.append("too_long")
        if c["gc_percent"] < CONFIG["min_gc"]:  flags.append("gc_low")
        if c["gc_percent"] > CONFIG["max_gc"]:  flags.append("gc_high")
        if c["n_percent"]  > CONFIG["max_n"]:   flags.append("n_high")
        if c["entropy"]    < CONFIG["min_entropy"]: flags.append("low_entropy")

        # compter chaque flag
        for flag in flags:
            flag_counts[flag] = flag_counts.get(flag, 0) + 1

        # trier la séquence
        seq_result = {"id": r["id"], "flags": flags}
        if flags:
            failed.append(seq_result)
        else:
            passed.append(seq_result)

    return {
        "passed":      passed,
        "failed":      failed,
        "flag_counts": flag_counts
    }