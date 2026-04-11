# Language Ranking - Bootstrap

This document summarizes how Java, Node.js, and Python ranked against each other in the bootstrap comparisons.
The `1st`, `2nd`, and `3rd` columns show how often each language finished in that position across the benchmark pairings.
A higher `1st` count means the language performed better in more comparisons, while the mean and median sections show whether that pattern is stable across different ways of aggregating the data.

## Interpretation Note (One-Sided Tests)

The underlying significance checks are one-sided (directional).
As a result, some entries may appear as not significant even when a clear difference exists in the opposite direction to the tested hypothesis.
This does not mean there is no difference; it means the tested direction was not supported.

## Mean Overhead

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 3 | 0 |
| Node.js | 3 | 0 | 2 |
| Python | 0 | 2 | 3 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 9 | 4 |
| Node.js | 13 | 0 | 2 |
| Python | 0 | 6 | 9 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 3 | 2 | 0 |
| Python | 2 | 0 | 3 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 8 | 2 | 0 |
| Python | 2 | 5 | 3 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 12 | 11 |
| Node.js | 21 | 2 | 2 |
| Python | 2 | 11 | 12 |

## Median Overhead

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 3 | 0 |
| Node.js | 3 | 0 | 2 |
| Python | 0 | 2 | 3 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 9 | 4 |
| Node.js | 13 | 0 | 2 |
| Python | 0 | 6 | 9 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 2 | 3 |
| Node.js | 3 | 0 | 2 |
| Python | 2 | 3 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 4 | 1 |
| Node.js | 3 | 1 | 1 |
| Python | 2 | 0 | 3 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 6 | 4 |
| Node.js | 6 | 1 | 3 |
| Python | 4 | 3 | 3 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 15 | 8 |
| Node.js | 19 | 1 | 5 |
| Python | 4 | 9 | 12 |

## Mean Absolute Values (without OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 5 | 10 | 0 |
| Python | 10 | 5 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 1 | 2 | 2 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 1 | 7 | 2 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 22 |
| Node.js | 6 | 17 | 2 |
| Python | 19 | 5 | 1 |

## Mean Absolute Values (with OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 0 | 15 | 0 |
| Python | 15 | 0 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 4 | 0 |
| Node.js | 0 | 1 | 4 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 4 | 5 |
| Node.js | 0 | 6 | 4 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 4 | 20 |
| Node.js | 0 | 21 | 4 |
| Python | 24 | 0 | 1 |

## Median Absolute Values (without OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 5 | 10 | 0 |
| Python | 10 | 5 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 1 | 2 | 2 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 1 | 7 | 2 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 22 |
| Node.js | 6 | 17 | 2 |
| Python | 19 | 5 | 1 |

## Median Absolute Values (with OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 0 | 15 | 0 |
| Python | 15 | 0 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 3 |
| Node.js | 0 | 4 | 1 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 8 |
| Node.js | 0 | 9 | 1 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 23 |
| Node.js | 0 | 24 | 1 |
| Python | 24 | 0 | 1 |


# Language Ranking - Raw

## Interpretation Note (One-Sided Tests)

The underlying significance checks are one-sided (directional).
As a result, some entries may appear as not significant even when a clear difference exists in the opposite direction to the tested hypothesis.
This does not mean there is no difference; it means the tested direction was not supported.

## Mean Overhead

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 3 | 0 |
| Node.js | 3 | 0 | 2 |
| Python | 0 | 2 | 3 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 9 | 4 |
| Node.js | 13 | 0 | 2 |
| Python | 0 | 6 | 9 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 3 | 2 | 0 |
| Python | 2 | 0 | 3 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 8 | 2 | 0 |
| Python | 2 | 5 | 3 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 12 | 11 |
| Node.js | 21 | 2 | 2 |
| Python | 2 | 11 | 12 |

## Median Overhead

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 3 | 0 |
| Node.js | 3 | 0 | 2 |
| Python | 0 | 2 | 3 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 2 | 3 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 9 | 4 |
| Node.js | 13 | 0 | 2 |
| Python | 0 | 6 | 9 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 2 | 3 |
| Node.js | 3 | 0 | 2 |
| Python | 2 | 3 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 4 | 1 |
| Node.js | 3 | 1 | 1 |
| Python | 2 | 0 | 3 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 6 | 4 |
| Node.js | 6 | 1 | 3 |
| Python | 4 | 3 | 3 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 15 | 8 |
| Node.js | 19 | 1 | 5 |
| Python | 4 | 9 | 12 |

## Mean Absolute Values (without OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 5 | 10 | 0 |
| Python | 10 | 5 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 1 | 2 | 2 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 1 | 7 | 2 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 22 |
| Node.js | 6 | 17 | 2 |
| Python | 19 | 5 | 1 |

## Mean Absolute Values (with OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 0 | 15 | 0 |
| Python | 15 | 0 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 4 | 0 |
| Node.js | 0 | 1 | 4 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 4 | 5 |
| Node.js | 0 | 6 | 4 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 4 | 20 |
| Node.js | 0 | 21 | 4 |
| Python | 24 | 0 | 1 |

## Median Absolute Values (without OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 5 | 10 | 0 |
| Python | 10 | 5 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 1 | 2 | 2 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 1 | 7 | 2 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 22 |
| Node.js | 6 | 17 | 2 |
| Python | 19 | 5 | 1 |

## Median Absolute Values (with OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 0 | 15 | 0 |
| Python | 15 | 0 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 3 |
| Node.js | 0 | 4 | 1 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 8 |
| Node.js | 0 | 9 | 1 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 23 |
| Node.js | 0 | 24 | 1 |
| Python | 24 | 0 | 1 |
