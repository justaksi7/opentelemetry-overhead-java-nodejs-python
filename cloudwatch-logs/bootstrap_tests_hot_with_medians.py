import csv
import re
from collections import defaultdict
from pathlib import Path
import numpy as np

LANGUAGES = {"java", "nodejs", "python"}
OUTPUT_FILE = Path("hot_bootstrap_comparisons_with_medians.txt")
FILENAME_RE = re.compile(r"^(java|nodejs|python)-(.+?)-(otel-)?hot\.csv$")

DURATION_RE = re.compile(r"Duration:\s*([0-9]+(?:\.[0-9]+)?)\s*ms")
MAX_MEMORY_RE = re.compile(r"Max Memory Used:\s*([0-9]+)\s*MB")

def parse_metrics(csv_path: Path) -> dict[str, list[float]]:
    metrics = {"duration_ms": [], "max_memory_mb": []}
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            msg = row.get("@message", "")
            d_m = DURATION_RE.search(msg)
            m_m = MAX_MEMORY_RE.search(msg)
            if d_m: metrics["duration_ms"].append(float(d_m.group(1)))
            if m_m: metrics["max_memory_mb"].append(float(m_m.group(1)))
    return metrics

def bootstrap_overhead_median(without: list[float], with_otel: list[float], n_iter: int = 100000) -> np.ndarray:
    ohne_arr, mit_arr = np.array(without), np.array(with_otel)
    n_ohne, n_mit = len(ohne_arr), len(mit_arr)
    overheads = []

    for _ in range(n_iter):
        med_ohne = np.median(np.random.choice(ohne_arr, size=n_ohne, replace=True))
        med_mit = np.median(np.random.choice(mit_arr, size=n_mit, replace=True))
        overheads.append((med_mit - med_ohne) / med_ohne)
    return np.array(overheads)

def main():
    base_dir = Path(".")
    all_hot_files = sorted(base_dir.glob("*-hot.csv"))
    grouped = defaultdict(dict)
    for f in all_hot_files:
        m = FILENAME_RE.match(f.name)
        if m:
            lang, bench, otel = m.groups()
            grouped[(lang, bench)]["with_otel" if otel else "without_otel"] = f

    metrics = {"duration_ms": "Duration (ms)", "max_memory_mb": "Max Memory (MB)"}
    results = ["=== BOOTSTRAP MEDIAN ANALYSE (HOT STARTS) ===\n"]

    for m_key, m_label in metrics.items():
        results.append(f"\n>>> {m_label} <<<" + "\n" + "-"*50)
        ov_data = {}
        summaries = []
        all_bench = sorted({b for (l, b) in grouped.keys()})

        for lang in sorted(LANGUAGES):
            for bench in all_bench:
                f_pair = grouped.get((lang, bench), {})
                if "without_otel" in f_pair and "with_otel" in f_pair:
                    v_wo = parse_metrics(f_pair["without_otel"])[m_key]
                    v_wi = parse_metrics(f_pair["with_otel"])[m_key]
                    if len(v_wo) > 1 and len(v_wi) > 1:
                        ovs = bootstrap_overhead_median(v_wo, v_wi)
                        ov_data[(lang, bench)] = ovs
                        summaries.append(f"{lang.upper():7} | {bench:15} | Med-Ohne: {np.median(v_wo):7.2f} | Med-Mit: {np.median(v_wi):7.2f} | OH: {np.mean(ovs):7.2%}")

        results.append("\n[OVERHEAD ÜBERSICHT (MEDIAN)]\n" + "\n".join(sorted(summaries)))
        results.append("\n[PAARVERGLEICHE DER MEDIAN-OVERHEADS]")
        for l1, l2 in [("java", "python"), ("java", "nodejs"), ("python", "nodejs")]:
            for bench in all_bench:
                if (l1, bench) in ov_data and (l2, bench) in ov_data:
                    p = np.mean(ov_data[(l1, bench)] <= ov_data[(l2, bench)])
                    results.append(f"{bench:15} {l1} vs {l2}: p={p:.5f} -> {'SIGNIFIKANT' if p < 0.00067 else 'nicht sig.'}")

    OUTPUT_FILE.write_text("\n".join(results))
    print(f"Median-Analyse abgeschlossen! Ergebnisse in {OUTPUT_FILE}")

if __name__ == "__main__": main()