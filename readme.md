# OpenTelemetry Overhead in AWS Lambda (Java, Node.js, Python)

Dieses Repository begleitet eine Bachelorarbeit zur Bewertung des Overheads durch OpenTelemetry-Instrumentierung in AWS-Lambda-Workloads mit Java, Node.js und Python.

## Inhalt

- [Projektüberblick](#projektueberblick)
- [Microbenchmarks](#microbenchmarks)
- [Repository-Struktur](#repository-struktur)
- [Ordnerdokumentation](#ordnerdokumentation)

## Projektueberblick

Untersucht werden Unterschiede zwischen nicht instrumentierten und instrumentierten Lambda-Funktionen in drei Sprachen und fünf Benchmark-Szenarien.

Verglichene Metriken:

- Duration
- Init Duration
- Max Memory Used

## Microbenchmarks

<img src="gfx/Microbenchmarks.png" width=400>

Die Benchmarks decken folgende Zugriffsmuster ab:

1. Function Invocation (asynchrones Lambda-zu-Lambda)
2. HTTP GET Request
3. HTTP POST Request
4. AWS DynamoDB Read Operation
5. AWS DynamoDB Write Operation

Jeder Benchmark wird als Baseline (ohne Tracing) und als instrumentierte Variante (mit Tracing) ausgefuehrt.

## Repository-Struktur

- `aws-http-server/`: Minimaler HTTP-Testserver fuer GET/POST-Benchmarks
- `aws-lambda-functions/`: Lambda-Implementierungen in Java, Node.js und Python
- `cloudwatch-logs/`: Exportierte Rohdaten (CSV) und Auswerte-Skripte
- `dynamo-db/`: Dokumentation der verwendeten DynamoDB-Tabellenstruktur
- `gfx/`: Grafiken fuer die Dokumentation
- `lambda-invocation-script/`: Last-/Invocation-Skript fuer den Lambda-Aufruf-Benchmark
- `results/`: Aufbereitete Ergebnisdateien und Visualisierungen

## Ordnerdokumentation

- [aws-http-server/readme.md](aws-http-server/readme.md)
- [aws-lambda-functions/readme.md](aws-lambda-functions/readme.md)
- [cloudwatch-logs/readme.md](cloudwatch-logs/readme.md)
- [dynamo-db/readme.md](dynamo-db/readme.md)
- [gfx/readme.md](gfx/readme.md)
- [lambda-invocation-script/readme.md](lambda-invocation-script/readme.md)
- [results/readme.md](results/readme.md)
