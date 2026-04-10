import csv
import re
from collections import defaultdict
from pathlib import Path

import numpy as np

LANGUAGES = {"java", "nodejs", "python"}
OUTPUT_FILE = Path("cold_bootstrap_comparisons_with_means.txt")


FILENAME_RE = re.compile(r"^(java|nodejs|python)-(.+?)-(otel-)?cold\.csv$")
DURATION_RE = re.compile(r"Duration:\s*([0-9]+(?:\.[0-9]+)?)\s*ms")
MAX_MEMORY_RE = re.compile(r"Max Memory Used:\s*([0-9]+)\s*MB")
INIT_DURATION_RE = re.compile(r"(?:Init|Initialization) Duration:\s*([0-9]+(?:\.[0-9]+)?)\s*ms")


def parse_metrics(csv_path: Path) -> dict[str, list[float]]:
    """Extrahiert Metriken aus der @message Spalte."""
    metrics = {
        "duration_ms": [],
        "init_duration_ms": [],
        "max_memory_mb": [],
    }
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            message = row.get("@message", "")
            if not message:
                continue

            duration_match = DURATION_RE.search(message)
            init_duration_match = INIT_DURATION_RE.search(message)
            memory_match = MAX_MEMORY_RE.search(message)

            if duration_match:
                metrics["duration_ms"].append(float(duration_match.group(1)))
            if init_duration_match:
                metrics["init_duration_ms"].append(float(init_duration_match.group(1)))
            if memory_match:
                metrics["max_memory_mb"].append(float(memory_match.group(1)))
    return metrics

def bootstrap_overhead(without: list[float], with_otel: list[float], n_iter: int = 100000) -> np.ndarray:
    """
    Erzeugt n_iter Bootstrap-Schätzungen des prozentualen Overheads.
    """
    ohne_arr = np.array(without)
    mit_arr = np.array(with_otel)
    overheads = []
    n_ohne = len(ohne_arr)
    n_mit = len(mit_arr)
    
    for _ in range(n_iter):
        boot_ohne = np.random.choice(ohne_arr, size=n_ohne, replace=True)
        boot_mit = np.random.choice(mit_arr, size=n_mit, replace=True)
        
        mean_ohne = np.mean(boot_ohne)
        mean_mit = np.mean(boot_mit)
        
        overhead = (mean_mit - mean_ohne) / mean_ohne
        overheads.append(overhead)
        
    return np.array(overheads)

def main() -> None:
    base_dir = Path(".")
    all_cold_files = sorted(base_dir.glob("*-cold.csv"))

    grouped: dict[tuple[str, str], dict[str, Path]] = defaultdict(dict)
    for file_path in all_cold_files:
        match = FILENAME_RE.match(file_path.name)
        if not match:
            continue
        language, benchmark, otel_group = match.groups()
        if language not in LANGUAGES:
            continue
        key = (language, benchmark)
        variant = "with_otel" if otel_group else "without_otel"
        grouped[key][variant] = file_path

    metric_keys = ["duration_ms", "init_duration_ms", "max_memory_mb"]
    metric_labels = {
        "duration_ms": "Duration (ms)",
        "init_duration_ms": "Init Duration (ms)",
        "max_memory_mb": "Max Memory Used (MB)",
    }

    language_pairs = [("java", "python"), ("java", "nodejs"), ("python", "nodejs")]

    results_lines = []
    results_lines.append("============================================================")
    results_lines.append("BOOTSTRAP-ANALYSE: RELATIVER OVERHEAD (COLD STARTS)")
    results_lines.append(f"Wiederholungen pro Test: 100.000")
    results_lines.append("============================================================\n")

    for metric_key in metric_keys:
        results_lines.append(f"\n>>> METRIK: {metric_labels[metric_key].upper()} <<<")
        results_lines.append("-" * 60)

        overhead_data: dict[tuple[str, str], np.ndarray] = {}
        language_summaries = []

        all_benchmarks = sorted({b for (l, b) in grouped.keys()})
        
        for language in sorted(LANGUAGES):
            for benchmark in all_benchmarks:
                files = grouped.get((language, benchmark), {})
                without_file = files.get("without_otel")
                with_file = files.get("with_otel")
                
                if not without_file or not with_file:
                    continue

                without_metrics = parse_metrics(without_file)
                with_metrics = parse_metrics(with_file)
                
                without_vals = without_metrics[metric_key]
                with_vals = with_metrics[metric_key]

                if len(without_vals) < 2 or len(with_vals) < 2:
                    continue

                avg_without = np.mean(without_vals)
                avg_with = np.mean(with_vals)

                overheads = bootstrap_overhead(without_vals, with_vals, n_iter=100000)
                overhead_data[(language, benchmark)] = overheads
                
                mean_oh = np.mean(overheads)
                std_oh = np.std(overheads)

                unit = "MB" if "memory" in metric_key else "ms"

                language_summaries.append(
                    f"{language.upper():7} | {benchmark:15} | "
                    f"Ohne: {avg_without:7.2f}{unit} | Mit: {avg_with:7.2f}{unit} | "
                    f"Overhead: {mean_oh:7.2%} (std={std_oh:.4f})"
                )

        results_lines.append("\n[EINZELWERTE ÜBERSICHT]")
        results_lines.extend(sorted(language_summaries))
        results_lines.append("")

        results_lines.append("[STATISTISCHE PAARVERGLEICHE]")
        for lang_a, lang_b in language_pairs:
            results_lines.append(f"--- {lang_a} vs. {lang_b} ---")
            for benchmark in all_benchmarks:
                key_a = (lang_a, benchmark)
                key_b = (lang_b, benchmark)
                
                if key_a not in overhead_data or key_b not in overhead_data:
                    continue

                dist_a = overhead_data[key_a]
                dist_b = overhead_data[key_b]

                p_value = np.mean(dist_a <= dist_b)
                signif = "SIGNIFIKANT HÖHER" if p_value < 0.00067 else "nicht signifikant"

                results_lines.append(
                    f"  {benchmark:15}: {lang_a}={np.mean(dist_a):.4f} vs {lang_b}={np.mean(dist_b):.4f} "
                    f"(p={p_value:.5f}) -> {signif}"
                )
            results_lines.append("")

    OUTPUT_FILE.write_text("\n".join(results_lines), encoding="utf-8")
    print(f"Analyse abgeschlossen. Cold-Start Ergebnisse in: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()