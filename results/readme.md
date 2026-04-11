# results

## Purpose

This folder contains processed result artifacts from the statistical analysis.

## Interpretation Note (One-Sided Tests)

Some comparisons are based on one-sided hypothesis tests.
Because the test only checks one predefined direction, a result can be labeled as not significant even when there is a clear difference in the opposite direction.
A difference is considered significant if the significance value p is less or equal to   α = 0,00067. In the case of one sided tests (in this work) the p-value shoud be <= 0,00067 or >= 0,99933. Due to a Bonferroni correction for 75 tests, the significance level was adjusted from $\alpha = 0.05$ to $\alpha = 0.00067$ for both Welch's t-Tests and the bootstrap tests. 

## Contents

1. Statistical summaries per benchmark and start temperature

- `invoke_cold_stats.txt`, `invoke_hot_stats.txt`
- `get-request_cold_stats.txt`, `get-request_hot_stats.txt`
- `post-request_cold_stats.txt`, `post-request_hot_stats.txt`
- `dynamodb-read_cold_stats.txt`, `dynamodb-read_hot_stats.txt`
- `dynamodb-write_cold_stats.txt`, `dynamodb-write_hot_stats.txt`

These files contain summary statistics such as count, min/max, mean, median, percentiles, standard deviation, and IQR for:

- Runtime (Duration)
- Max Memory Used
- Initialization Duration

2. Bootstrap comparisons between languages

- `cold_bootstrap_comparisons_with_means.txt`
- `cold_bootstrap_comparisons_with_medians.txt`
- `hot_bootstrap_comparisons_with_means.txt`
- `hot_bootstrap_comparisons_with_medians.txt`

These reports contain pairwise comparisons (Java/Python, Java/Node.js, Python/Node.js) based on relative overheads.

3. Language ranking overview

- `language-ranking.md`

This file gives an overview of how often Java, Node.js, and Python ranked 1st, 2nd, or 3rd in the comparisons in terms of overhead and absolute metrics values.
It is a compact summary of the cross-language ranking results and helps to read the comparison tables at a glance.

4. Significance reports (Welch's t-tests)

- `cold_stats_significance.txt`
- `hot_stats_significance.txt`

These reports summarize significance testing results for OTel vs. non-OTel comparisons per language, benchmark, and metric.

5. Visualizations

For each benchmark and temperature, plot files are provided for OTel-vs.-non-OTel comparisons, for example:

- `invoke-cold-otel-comparison.png`
- `get-request-hot-otel-comparison.png`
- `dynamodb-read-cold-otel-comparison.png`

## Role in the Workflow

`cloudwatch-logs` provides raw data, while `results` contains derived, publication-ready outputs.