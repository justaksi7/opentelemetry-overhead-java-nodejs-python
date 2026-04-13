# Language Ranking - Bootstrap vs Raw (Side by Side)

This document groups each Bootstrap table directly with the matching Raw table.
The `1st`, `2nd`, and `3rd` columns show how often each language finished in that position across the benchmark pairings.

## Median Overhead

### Cold Starts

#### Init Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 3 | 0 |
| Node.js | 0 | 0 | 5 |
| Python | 3 | 2 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 2 | 0 | 3 |
| Python | 3 | 2 | 0 |

#### Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 2 | 0 | 3 |
| Python | 3 | 2 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 2 | 0 | 3 |
| Python | 3 | 2 | 0 |

#### Max Memory Used (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 2 | 3 | 0 |
| Node.js | 0 | 0 | 5 |
| Python | 3 | 2 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 4 | 9 | 2 |
| Node.js | 2 | 0 | 13 |
| Python | 9 | 6 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 6 | 9 |
| Node.js | 4 | 5 | 6 |
| Python | 11 | 4 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 3 | 2 | 0 |
| Node.js | 2 | 0 | 3 |
| Python | 0 | 3 | 2 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 3 | 2 | 0 |
| Node.js | 2 | 0 | 3 |
| Python | 0 | 3 | 2 |

#### Max Memory Used (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 4 | 0 |
| Node.js | 1 | 1 | 3 |
| Python | 3 | 0 | 2 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 4 | 6 | 0 |
| Node.js | 3 | 1 | 6 |
| Python | 3 | 3 | 4 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 3 | 2 | 5 |
| Node.js | 2 | 5 | 3 |
| Python | 5 | 3 | 2 |

### Combined Total (25 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 8 | 15 | 2 |
| Node.js | 5 | 1 | 19 |
| Python | 12 | 9 | 4 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 3 | 8 | 14 |
| Node.js | 6 | 10 | 9 |
| Python | 16 | 7 | 2 |

## Median Absolute Values (without OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 5 | 0 | 0 |
| Python | 0 | 5 | 0 |

#### Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 5 | 10 | 0 |
| Python | 10 | 5 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 5 | 10 | 0 |
| Python | 10 | 5 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 1 | 2 | 2 |
| Python | 4 | 0 | 1 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 2 |
| Node.js | 1 | 2 | 2 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 1 | 7 | 2 |
| Python | 9 | 0 | 1 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 7 |
| Node.js | 1 | 7 | 2 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 22 |
| Node.js | 6 | 17 | 2 |
| Python | 19 | 5 | 1 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 3 | 22 |
| Node.js | 6 | 17 | 2 |
| Python | 19 | 5 | 1 |

## Median Absolute Values (with OTel)

### Cold Starts

#### Init Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Max Memory Used (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Cold Starts (15 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 0 | 15 | 0 |
| Python | 15 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 15 |
| Node.js | 0 | 15 | 0 |
| Python | 15 | 0 | 0 |

### Warm Starts

#### Duration (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 3 |
| Node.js | 0 | 4 | 1 |
| Python | 4 | 0 | 1 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 3 |
| Node.js | 0 | 4 | 1 |
| Python | 4 | 0 | 1 |

#### Max Memory Used (5 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 0 | 0 | 5 |
| Node.js | 0 | 5 | 0 |
| Python | 5 | 0 | 0 |

#### Combined for Warm Starts (10 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 8 |
| Node.js | 0 | 9 | 1 |
| Python | 9 | 0 | 1 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 8 |
| Node.js | 0 | 9 | 1 |
| Python | 9 | 0 | 1 |

### Combined Total (25 Comparisons)

##### Bootstrap

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 23 |
| Node.js | 0 | 24 | 1 |
| Python | 24 | 0 | 1 |

##### Raw

| Language | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| Java | 1 | 1 | 23 |
| Node.js | 0 | 24 | 1 |
| Python | 24 | 0 | 1 |
