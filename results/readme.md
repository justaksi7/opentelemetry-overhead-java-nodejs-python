# results

## Zweck

Dieser Ordner enthält aufbereitete Ergebnisartefakte aus der statistischen Analyse.

## Inhalt

1. Statistische Zusammenfassungen pro Benchmark und Starttemperatur

- `invoke_cold_stats.txt`, `invoke_hot_stats.txt`
- `get-request_cold_stats.txt`, `get-request_hot_stats.txt`
- `post-request_cold_stats.txt`, `post-request_hot_stats.txt`
- `dynamodb-read_cold_stats.txt`, `dynamodb-read_hot_stats.txt`
- `dynamodb-write_cold_stats.txt`, `dynamodb-write_hot_stats.txt`

Diese Dateien enthalten zusammenfassende Statistiken wie Anzahl, Min/Max, Mittelwert, Median, Perzentile, Standardabweichung und IQR für:

- Laufzeit (Duration)
- Max Memory Used
- Initialisierungsdauer

2. Bootstrap-Berichte

- `bootstrap-tests-cold.txt`
- `bootstrap-tests-hot.txt`

Diese Berichte enthalten sprachuebergreifende Bootstrap-Auswertungen fuer Cold- und Hot-Starts.

3. Visualisierungen

Für jeden Benchmark und jede Temperatur sind Plot-Dateien für OTel-vs.-Nicht-OTel-Vergleiche vorhanden, zum Beispiel:

- `invoke-cold-otel-comparison.png`
- `get-request-hot-otel-comparison.png`
- `dynamodb-read-cold-otel-comparison.png`

## Rolle im Workflow

`cloudwatch-logs` stellt Rohdaten bereit, während `results` die daraus abgeleiteten Ausgaben enthält.
