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

The project evaluates the overhead introduced by OpenTelemetry instrumentation in AWS-based serverless workloads.

For each language (Java, Node.js, Python), 12.000 instrumented and 12.000 non-instrumented function invocations (2.000 cold starts and 10.000 hot starts) were observed and the results were evaluated. The differences in performance between the instrumented and non-instrumented versions were tested for statistical significance in all 3 languages across all 3 metrics (Duration, Init Duration and Max Memory Used) using Welch's t-tests. All of the performance differences were statistically significant. Additionally to the differences between the instrumented and non-instrumented versions of the functions, the performance differences across all 3 languages were tested for statistical significance using bootstrap tests based on the means and medians as well. All of the differences were statistically significant based on the medians. In the case of means the only statistical insignificance occured between Python and NodeJS for the microbenchmark HTTP GET request (for hot starts only).
## Microbenchmarks

In total, five microbenchmarks are used to evaluate tracing overhead under typical AWS serverless interaction patterns.

<img src="gfx/Microbenchmarks.png" width=400>

All benchmarks are executed in two variants:

- Baseline (without tracing instrumentation)
- Instrumented (with tracing instrumentation)

For each benchmark, the following metrics are compared:

- Duration
- Max memory used
- Init duration (cold starts)

<details><summary><b>Function Invocation</b></summary>

This microbenchmark measures the overhead of one AWS Lambda function invoking another Lambda function asynchronously (fire-and-forget).

Typical flow:

1. Function A receives a lightweight input payload.
2. Function A invokes Function B asynchronously.
3. Function A does not wait for Function B to complete.
4. Function A returns immediately after the invocation call is sent.

What this captures:

- Tracing overhead for inter-function communication
- Context propagation overhead across function boundaries
- Additional latency introduced in short call chains

</details>

<details><summary><b>HTTP GET Request</b></summary>

This microbenchmark evaluates read-only outbound HTTP communication from a Lambda function to an endpoint in the AWS-based test setup.

Typical flow:

1. The function issues a GET request to a fixed endpoint.
2. A small response payload is returned.
3. The function returns or processes the response.

What this captures:

- Tracing overhead for outbound client spans
- Header/context injection overhead in network requests
- Relative overhead when operation logic is simple and I/O-bound

</details>

<details><summary><b>HTTP POST Request</b></summary>

This microbenchmark evaluates outbound HTTP communication with a request body from a Lambda function to an endpoint in the AWS-based test setup.

Typical flow:

1. The function creates a small structured payload.
2. The function sends a POST request to a fixed endpoint.
3. The endpoint returns a response that is forwarded or minimally processed.

What this captures:

- Tracing overhead for request + response handling
- Serialization and propagation overhead on write-style API calls
- Additional instrumentation cost compared to read-only HTTP requests

</details>

<details><summary><b>AWS DynamoDB Read Operation</b></summary>

This microbenchmark measures the overhead of reading a single record from AWS DynamoDB.

Typical flow:

1. The function builds a lookup key.
2. The function performs a single-item read.
3. The retrieved item is returned.

What this captures:

- Tracing overhead for datastore client operations
- Context propagation into storage-layer calls
- Overhead characteristics for short, read-dominated data access

</details>

<details><summary><b>AWS DynamoDB Write Operation</b></summary>

This microbenchmark measures the overhead of writing a single record to AWS DynamoDB.

Typical flow:

1. The function builds a small record.
2. The function performs a single-item write.
3. The function returns operation metadata or a success indicator.

What this captures:

- Tracing overhead for write-oriented datastore calls
- Instrumentation cost for mutation operations
- Relative overhead differences between read and write paths

</details>

Together, these five microbenchmarks cover Lambda-to-Lambda calls, outbound HTTP traffic, and DynamoDB access patterns within AWS. This provides a compact but representative basis for comparing tracing overhead across runtimes and startup modes.

## Repository Structure

- `aws-lambda-functions/`: Lambda implementations for Java, Node.js, and Python
- `aws-http-server/`: HTTP test server used by request microbenchmarks
- `cloudwatch-logs/`: raw measurement data and bootstrap/statistical scripts
- `results/`: generated result artifacts

## Results
