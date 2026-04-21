# cloudwatch-logs

## Zweck

Dieser Ordner enthält aus AWS CloudWatch exportierte Rohdaten sowie die zur Auswertung verwendeten Analyse-Skripte.

## Rohdaten (CSV)

Die CSV-Dateien enthalten CloudWatch-Logzeilen in folgender Form:

- `@timestamp`
- `@message` (mit `Duration`, `Max Memory Used`, `Init Duration`)

Beispielhafte Felder innerhalb einer REPORT-Zeile in `@message`:

- `Duration: ... ms`
- `Max Memory Used: ... MB`
- `Init Duration: ... ms`

## Dateinamensschema

Messdateien folgen diesem Muster:

`<sprache>-<benchmark>-<otel?>-<temperatur>.csv`

Beispiele:

- `java-invoke-cold.csv` (ohne OTel, cold)
- `java-invoke-otel-cold.csv` (mit OTel, cold)
- `python-post-request-hot.csv`

Dimensionen:

- Sprachen: `java`, `nodejs`, `python`
- Benchmarks: `invoke`, `get-request`, `post-request`, `dynamodb-read`, `dynamodb-write`
- Varianten: mit OTel (`-otel-`) und ohne OTel
- Temperaturen: `cold`, `hot`

## Analyse-Skripte

Der Ordner enthält Python-Skripte für Bootstrap-Analysen:

- `bootstrap_tests_cold.py`
- `bootstrap_tests_hot.py`

Diese Skripte extrahieren Metriken aus `@message` und vergleichen OTel- mit Nicht-OTel-Ergebnissen pro Sprache und Benchmark.

