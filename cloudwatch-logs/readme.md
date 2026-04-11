# cloudwatch-logs

## Purpose

This folder contains raw data exported from AWS CloudWatch and the analysis scripts used for evaluation.

## Raw Data (CSV)

The CSV files contain CloudWatch log lines in the form:

- `@timestamp`
- `@message` (mit `Duration`, `Max Memory Used`, `Init Duration`)

Example fields inside a REPORT line in `@message`:

- `Duration: ... ms`
- `Max Memory Used: ... MB`
- `Init Duration: ... ms`

## File Naming Scheme

Measurement files follow this pattern:

`<language>-<benchmark>-<otel?>-<temperature>.csv`

Examples:

- `java-invoke-cold.csv` (without OTel, cold)
- `java-invoke-otel-cold.csv` (with OTel, cold)
- `python-post-request-hot.csv`

Dimensions:

- Languages: `java`, `nodejs`, `python`
- Benchmarks: `invoke`, `get-request`, `post-request`, `dynamodb-read`, `dynamodb-write`
- Variants: with OTel (`-otel-`) and without OTel
- Temperatures: `cold`, `hot`

## Analysis Scripts

The folder includes Python scripts for significance tests and bootstrap analyses:

- `t_tests_otel_cold.py`
- `t_tests_otel_hot.py`
- `bootstrap_tests_cold_with_means.py`
- `bootstrap_tests_cold_with_medians.py`
- `bootstrap_tests_hot_with_means.py`
- `bootstrap_tests_hot_with_medians.py`

These scripts extract metrics from `@message` and compare OTel vs. non-OTel results per language and benchmark.

