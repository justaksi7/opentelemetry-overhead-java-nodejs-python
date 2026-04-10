import csv
import re
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import ttest_ind


LANGUAGES = {"java", "nodejs", "python"}
OUTPUT_FILE = Path("hot_stats_significance.txt")

FILENAME_RE = re.compile(r"^(java|nodejs|python)-(.+?)-(otel-)?hot\.csv$")
DURATION_RE = re.compile(r"Duration:\s*([0-9]+(?:\.[0-9]+)?)\s*ms")
MAX_MEMORY_RE = re.compile(r"Max Memory Used:\s*([0-9]+)\s*MB")
INIT_DURATION_RE = re.compile(r"(?:Init|Initialization) Duration:\s*([0-9]+(?:\.[0-9]+)?)\s*ms")


def parse_metrics(csv_path: Path) -> dict[str, list[float]]:
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


def run_welch_ttest(without_otel: list[float], with_otel: list[float]) -> tuple[float, float] | None:
    if len(without_otel) < 2 or len(with_otel) < 2:
        return None
    t_stat, p_value = ttest_ind(with_otel, without_otel, equal_var=False)
    return float(t_stat), float(p_value)


def fmt_mean_std(values: list[float]) -> str:
    if not values:
        return "n=0"
    return f"n={len(values)} mean={np.mean(values):.2f} std={np.std(values):.2f}"


def main() -> None:
    base_dir = Path(".")
    all_hot_files = sorted(base_dir.glob("*-hot.csv"))

    grouped: dict[tuple[str, str], dict[str, Path]] = defaultdict(dict)

    for file_path in all_hot_files:
        match = FILENAME_RE.match(file_path.name)
        if not match:
            continue

        language, benchmark, otel_group = match.groups()
        if language not in LANGUAGES:
            continue

        key = (language, benchmark)
        variant = "with_otel" if otel_group else "without_otel"
        grouped[key][variant] = file_path

    results_lines: list[str] = []
    results_lines.append("Signifikanzanalyse hot-Starts (Welch t-Test)")
    results_lines.append("Vergleich: mit OTel vs. ohne OTel")
    results_lines.append("")
    results_lines.append(f"Gefundene *-hot.csv Dateien: {len(all_hot_files)}")
    results_lines.append(f"Erkannte Sprach/Benchmark-Gruppen: {len(grouped)}")
    results_lines.append("")

    processed_pairs = 0
    metric_labels = {
        "duration_ms": "Duration (ms)",
        "init_duration_ms": "Init Duration (ms)",
        "max_memory_mb": "Max Memory Used (MB)",
    }

    for language in sorted(LANGUAGES):
        for benchmark in sorted({bench for lang, bench in grouped.keys() if lang == language}):
            files = grouped[(language, benchmark)]
            without_file = files.get("without_otel")
            with_file = files.get("with_otel")

            results_lines.append(f"=== {language} / {benchmark} ===")

            if not without_file or not with_file:
                results_lines.append("  Paar unvollständig: mit/ohne OTel-Datei fehlt.")
                results_lines.append("")
                continue

            processed_pairs += 1
            results_lines.append(f"  ohne OTel Datei: {without_file.name}")
            results_lines.append(f"  mit OTel Datei:  {with_file.name}")

            without_metrics = parse_metrics(without_file)
            with_metrics = parse_metrics(with_file)

            for metric_key in ("duration_ms", "init_duration_ms", "max_memory_mb"):
                values_without = without_metrics[metric_key]
                values_with = with_metrics[metric_key]
                test_result = run_welch_ttest(values_without, values_with)

                results_lines.append(f"  - {metric_labels[metric_key]}")
                results_lines.append(f"    ohne OTel: {fmt_mean_std(values_without)}")
                results_lines.append(f"    mit OTel:  {fmt_mean_std(values_with)}")

                if test_result is None:
                    results_lines.append("    t-Test: nicht möglich (zu wenige Werte, mindestens 2 pro Gruppe)")
                else:
                    t_stat, p_value = test_result
                    signif = "signifikant" if p_value < 0.00067 else "nicht signifikant"
                    results_lines.append(f"    t-Test: t={t_stat:.6f}, p={p_value:.6g} -> {signif} (alpha=0.00067)")

            results_lines.append("")

    results_lines.append(f"Ausgewertete vollständige Paare: {processed_pairs}")

    OUTPUT_FILE.write_text("\n".join(results_lines), encoding="utf-8")
    print(f"Analyse abgeschlossen. Ausgabe gespeichert in: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()