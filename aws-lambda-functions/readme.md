# aws-lambda-functions

## Zweck

Dieser Ordner enthält die AWS-Lambda-Implementierungen für alle Microbenchmarks.

Enthalten sind:

- 5 Benchmarks
- 3 Sprachen (Java, Node.js, Python)
- Insgesamt 15 Implementierungen

Wichtig: Im Benchmark Function Invocation ist der Aufruf asynchron (Fire-and-Forget), daher wartet der Aufrufer nicht auf das Ergebnis der zweiten Lambda-Funktion.

## Ordnerstruktur

- `java/`: Java-Implementierungen aller 5 Benchmarks
- `nodejs/`: Node.js-Implementierungen aller 5 Benchmarks
- `python/`: Python-Implementierungen aller 5 Benchmarks

## Benchmark-Abdeckung pro Sprache

Für jede Sprache sind die folgenden Funktionen verfügbar:

1. `Invoke_Lambda` (asynchron)
2. `GET_Request`
3. `POST_Request`
4. `DynamoDB_Read`
5. `DynamoDB_Write`

## Konfiguration der AWS-Lambda-Umgebung

Um Vergleichbarkeit sicherzustellen, wurden alle Funktionen mit festen Konfigurationsparametern ausgeführt.

| Parameter | Wert |
|---|---|
| Region | `eu-central-1` (Frankfurt) |
| Speicher | `1024 MB` |
| Ephemeral Storage | `512 MB` |
| Timeout | `15 Sekunden` |
| Reserved Concurrency | `200` |
| Runtime | `Java 21`, `Python 3.13`, `Node.js 22.x` |
| IAM-Rolle | Minimal erforderliche Berechtigungen |

### IAM-Berechtigungen (minimal)

- `lambda:InvokeFunction` (Benchmark 1)
- `dynamodb:GetItem` (Benchmark 4)
- `dynamodb:PutItem` (Benchmark 5)
- Logs in CloudWatch schreiben

### Instrumentierung

Die Instrumentierung erfolgt über ADOT-Lambda-Layer (sprach- und regionsspezifisch), referenziert per ARN.

## Verwendete Bibliotheken und SDKs

Die Implementierungen nutzen offizielle AWS-SDKs sowie Standard-HTTP-Bibliotheken.

### Java

| Benchmark | Verwendete Bibliotheken / SDKs |
|---|---|
| 1. Lambda Invocation | AWS Lambda Runtime, AWS SDK v2 für Lambda (`LambdaClient`, `InvokeRequest`, `InvocationType`, `SdkBytes`) |
| 2. HTTP GET | AWS Lambda Runtime, Java HTTP Client (`java.net.http.HttpClient`, `HttpRequest`, `HttpResponse`) |
| 3. HTTP POST | AWS Lambda Runtime, Java HTTP Client, Gson |
| 4. DynamoDB Read | AWS Lambda Runtime, AWS SDK v2 für DynamoDB (`DynamoDbClient`, `AttributeValue`, `GetItemRequest`, `GetItemResponse`) |
| 5. DynamoDB Write | AWS Lambda Runtime, AWS SDK v2 für DynamoDB (`DynamoDbClient`, `PutItemRequest`, `DynamoDbException`), `java.util.UUID` |

### Python

| Benchmark | Verwendete Bibliotheken / Module |
|---|---|
| 1. Lambda Invocation | `boto3`, `json` |
| 2. HTTP GET | `urllib3` |
| 3. HTTP POST | `urllib3`, `json` |
| 4. DynamoDB Read | `boto3`, `json` |
| 5. DynamoDB Write | `boto3`, `uuid`, `json` |

### Node.js

| Benchmark | Verwendete Bibliotheken / Module |
|---|---|
| 1. Lambda Invocation | `@aws-sdk/client-lambda` (`LambdaClient`, `InvokeCommand`) |
| 2. HTTP GET | Keine zusätzliche Bibliothek (Runtime-`fetch`) |
| 3. HTTP POST | Keine zusätzliche Bibliothek (Runtime-`fetch`) |
| 4. DynamoDB Read | `@aws-sdk/client-dynamodb` (`DynamoDBClient`, `GetItemCommand`) |
| 5. DynamoDB Write | `@aws-sdk/client-dynamodb` (`DynamoDBClient`, `PutItemCommand`), `crypto.randomUUID` |

