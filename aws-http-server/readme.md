# aws-http-server

## Purpose

This folder contains a simple HTTP test server for the microbenchmarks:

- Benchmark 2: HTTP GET Request
- Benchmark 3: HTTP POST Request

The implementation is intentionally minimal and only uses the file `index.js`.

## Implementation (`index.js`)

The server is based on Express and exposes three endpoints:

1. `GET /get-request`
Returns a predefined JSON object and increments the internal `requestCount` counter.

2. `POST /post-request`
Accepts a JSON payload, replaces the currently stored record, and increments `requestCount`.

3. `GET /request-count`
Returns the number of processed GET/POST requests.

## Why This Simplicity Matters

The file is intentionally small so that as little additional server logic as possible affects the HTTP benchmark measurements.

## Runtime Environment

The HTTP test server was run on the following AWS EC2 instance configuration:

| Parameter | Value |
|---|---|
| Instance type | m7i-flex.large |
| Architecture | x86_64 |
| vCPUs | 2 |
| Memory (RAM) | 8 GiB |
| Clock speed | 3.2 GHz (sustained) |
| Operating system | Amazon Linux 2 |
| Region | eu-central-1 (Frankfurt) |
| Availability zones | eu-central-1a, eu-central-1b, eu-central-1c |
| Network performance | Up to 12.5 Gigabit |
| EBS bandwidth (baseline) | 312 Mbps |
