# aws-lambda-functions

## Purpose

This folder contains the AWS Lambda implementations for all microbenchmarks.

It includes:

- 5 Benchmarks
- 3 languages (Java, Node.js, Python)
- 15 implementations in total

Important: In the Function Invocation benchmark, the invocation is asynchronous (fire-and-forget), so the caller does not wait for the result of the second Lambda function.

## Folder Structure

- `java/`: Java implementations of all 5 benchmarks
- `nodejs/`: Node.js implementations of all 5 benchmarks
- `python/`: Python implementations of all 5 benchmarks

## Benchmark Coverage per Language

For each language, the following functions are available:

1. `Invoke_Lambda` (asynchron)
2. `GET_Request`
3. `POST_Request`
4. `DynamoDB_Read`
5. `DynamoDB_Write`

## Konfiguration der AWS Lambda-Umgebung

To ensure comparability, all functions were executed with fixed configuration parameters.

| Parameter | Wert |
|---|---|
| Region | `eu-central-1` (Frankfurt) |
| Memory | `1024 MB` |
| Ephemeral Storage | `512 MB` |
| Timeout | `15 seconds` |
| Reserved concurrency | `200` |
| Runtime | `Java 21`, `Python 3.13`, `Node.js 22.x` |
| IAM role | Minimal required permissions |

### IAM Permissions (Minimal)

- `lambda:InvokeFunction` (Benchmark 1)
- `dynamodb:GetItem` (Benchmark 4)
- `dynamodb:PutItem` (Benchmark 5)
- Write logs to CloudWatch

### Instrumentation

Instrumentation is applied via ADOT Lambda Layers (language- and region-specific), referenced by ARN.

## Libraries and SDKs Used

The implementations use official AWS SDKs and standard HTTP libraries.

### Java

| Benchmark | Libraries / SDKs Used |
|---|---|
| 1. Lambda Invocation | AWS Lambda Runtime, AWS SDK v2 for Lambda (`LambdaClient`, `InvokeRequest`, `InvocationType`, `SdkBytes`) |
| 2. HTTP GET | AWS Lambda Runtime, Java HTTP Client (`java.net.http.HttpClient`, `HttpRequest`, `HttpResponse`) |
| 3. HTTP POST | AWS Lambda Runtime, Java HTTP Client, Gson |
| 4. DynamoDB Read | AWS Lambda Runtime, AWS SDK v2 for DynamoDB (`DynamoDbClient`, `AttributeValue`, `GetItemRequest`, `GetItemResponse`) |
| 5. DynamoDB Write | AWS Lambda Runtime, AWS SDK v2 for DynamoDB (`DynamoDbClient`, `PutItemRequest`, `DynamoDbException`), `java.util.UUID` |

### Python

| Benchmark | Libraries / Modules Used |
|---|---|
| 1. Lambda Invocation | `boto3`, `json` |
| 2. HTTP GET | `urllib3` |
| 3. HTTP POST | `urllib3`, `json` |
| 4. DynamoDB Read | `boto3`, `json` |
| 5. DynamoDB Write | `boto3`, `uuid`, `json` |

### Node.js

| Benchmark | Libraries / Modules Used |
|---|---|
| 1. Lambda Invocation | `@aws-sdk/client-lambda` (`LambdaClient`, `InvokeCommand`) |
| 2. HTTP GET | No additional library (runtime `fetch`) |
| 3. HTTP POST | No additional library (runtime `fetch`) |
| 4. DynamoDB Read | `@aws-sdk/client-dynamodb` (`DynamoDBClient`, `GetItemCommand`) |
| 5. DynamoDB Write | `@aws-sdk/client-dynamodb` (`DynamoDBClient`, `PutItemCommand`), `crypto.randomUUID` |

