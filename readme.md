# OpenTelemetry Overhead in AWS Lambda (Java, Node.js, Python)

*This repository is accompanying my bachelor thesis "Evaluation des durch die Instrumentierung
mit OpenTelemetry verursachten Overheads
in Java-, Python- und NodeJS-basierten
Serverless-Umgebungen". The goal of this work is a comparative performance evaluation of OpenTelemetry overhead in AWS Lambda functions across Java, Node.js, and Python. The benchmark suite covers five microbenchmarks and compares uninstrumented vs. instrumented executions for cold and hot starts. The goal is to quantify relative overhead in runtime, memory usage, and initialization behavior.*

**Content:**

- [Project Overview](#project-overview)
- [Microbenchmarks](#microbenchmarks)
- [Repository Structure](#repository-structure)
- [Results](#results)

## Project Overview

The project evaluates the overhead introduced by OpenTelemetry instrumentation in serverless workloads.

For each language (Java, Node.js, Python), 12.000 instrumented and 12.000 non-instrumented function invocations (2.000 cold starts and 10.000 hot starts) were observed and the results were evaluated. The differences in performance between the instrumented and non-instrumented versions were tested for statistical significance in all 3 languages across all 3 metrics (Duration, Init Duration and Max Memory Used) using Welch's t-tests. All of the performance differences were statistically significant. Additionally to the differences between the instrumented and non-instrumented versions of the functions, the performance differences across all 3 languages were tested for statistical significance using bootstrap tests based on the means and medians as well. All of the differences were statistically significant based on the medians. In the case of means the only statistical insignificance occured between Python and NodeJS for the microbenchmark HTTP GET request (for hot starts only).
## Microbenchmarks

The benchmark suite includes five microbenchmarks:

1. Lambda function invocation
2. HTTP GET request
3. HTTP POST request
4. DynamoDB read operation
5. DynamoDB write operation

Each benchmark is executed in instrumented and non-instrumented variants and analyzed for:

- Duration
- Max memory used
- Init duration (cold starts)

## Repository Structure

- `aws-lambda-functions/`: Lambda implementations for Java, Node.js, and Python
- `aws-http-server/`: HTTP test server used by request microbenchmarks
- `cloudwatch-logs/`: raw measurement data and bootstrap/statistical scripts
- `results/`: generated result artifacts

## Results
