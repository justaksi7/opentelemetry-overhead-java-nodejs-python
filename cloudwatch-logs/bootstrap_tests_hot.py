import csv
import re
from collections import defaultdict
from pathlib import Path

import numpy as np


LANGUAGES = {"java", "nodejs", "python"}
OUTPUT_FILE = Path("hot_bootstrap_comparisons.txt")

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


def fmt_mean_std(values: list[float]) -> str:
	if not values:
		return "n=0"
	return f"n={len(values)} mean={np.mean(values):.2f} std={np.std(values):.2f}"

def bootstrap_overhead(without: list[float], with_otel: list[float], n_iter: int = 100000) -> np.ndarray:
	"""
	Erzeugt n_iter Bootstrap-Schätzungen des prozentualen Overheads.
	overhead = (mean_mit - mean_ohne) / mean_ohne
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

	metric_keys = ["duration_ms", "init_duration_ms", "max_memory_mb"]
	metric_labels = {
		"duration_ms": "Duration (ms)",
		"init_duration_ms": "Init Duration (ms)",
		"max_memory_mb": "Max Memory Used (MB)",
	}

	language_pairs = [("java", "python"), ("java", "nodejs"), ("python", "nodejs")]

	results_lines = []
	results_lines.append("Bootstrap-Vergleich der relativen Overheads (Warmstarts/Hot)")
	results_lines.append("Vergleich: Overhead in Sprache A > Overhead in Sprache B?")
	results_lines.append("Bootstrap-Wiederholungen pro Test: 100.000")
	results_lines.append("")

	for metric_key in metric_keys:
		results_lines.append(f"\n{'='*60}")
		results_lines.append(f"Metrik: {metric_labels[metric_key]}")
		results_lines.append(f"{'='*60}\n")

		overhead_data: dict[tuple[str, str], np.ndarray] = {}

		for language in LANGUAGES:
			for benchmark in sorted({b for (l, b) in grouped.keys() if l == language}):
				files = grouped[(language, benchmark)]
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

				overheads = bootstrap_overhead(without_vals, with_vals, n_iter=100000)
				overhead_data[(language, benchmark)] = overheads

		for lang_a, lang_b in language_pairs:
			results_lines.append(f"\n--- Vergleich: {lang_a} vs. {lang_b} ---")
			for benchmark in sorted({b for (l, b) in grouped.keys()}):
				key_a = (lang_a, benchmark)
				key_b = (lang_b, benchmark)
				if key_a not in overhead_data or key_b not in overhead_data:
					continue

				overhead_a = overhead_data[key_a]
				overhead_b = overhead_data[key_b]

				p_value = np.mean(overhead_a <= overhead_b)

				mean_a = np.mean(overhead_a)
				mean_b = np.mean(overhead_b)
				std_a = np.std(overhead_a)
				std_b = np.std(overhead_b)

				signif = "signifikant" if p_value < 0.05 else "nicht signifikant"
				results_lines.append(
					f"  {benchmark}: {lang_a}={mean_a:.4f}±{std_a:.4f}, "
					f"{lang_b}={mean_b:.4f}±{std_b:.4f}, "
					f"p={p_value:.6f} -> {signif}"
				)
			results_lines.append("")

	OUTPUT_FILE.write_text("\n".join(results_lines), encoding="utf-8")
	print(f"Analyse abgeschlossen. Ergebnisse in: {OUTPUT_FILE}")


if __name__ == "__main__":
	main()
