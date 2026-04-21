# aws-http-server

## Zweck

Dieser Ordner enthält einen einfachen HTTP-Testserver für die Microbenchmarks:

- Benchmark 2: HTTP GET Request
- Benchmark 3: HTTP POST Request

Die Implementierung ist bewusst minimal gehalten.

Aktuelle Dateien in diesem Ordner:

- `index.js`
- `package.json`
- `package-lock.json`

## Implementierung (`index.js`)

Der Server basiert auf Express und stellt drei Endpunkte bereit:

1. `GET /get-request`
Gibt ein vordefiniertes JSON-Objekt zurück und erhöht den internen Zähler `requestCount`.

2. `POST /post-request`
Akzeptiert ein JSON-Payload, ersetzt den aktuell gespeicherten Datensatz und erhöht `requestCount`.

3. `GET /request-count`
Gibt die Anzahl der verarbeiteten GET-/POST-Anfragen zurück.

## Warum diese Einfachheit wichtig ist

Die Datei ist absichtlich klein, damit möglichst wenig zusätzliche Serverlogik die HTTP-Benchmark-Messungen beeinflusst.

## Laufzeitumgebung

Der HTTP-Testserver wurde mit folgender AWS-EC2-Instanzkonfiguration betrieben:

| Parameter | Wert |
|---|---|
| Instanztyp | m7i-flex.large |
| Architektur | x86_64 |
| vCPUs | 2 |
| Arbeitsspeicher (RAM) | 8 GiB |
| Taktfrequenz | 3.2 GHz (sustained) |
| Betriebssystem | Amazon Linux 2 |
| Region | eu-central-1 (Frankfurt) |
| Availability Zones | eu-central-1a, eu-central-1b, eu-central-1c |
| Netzwerkleistung | Bis zu 12.5 Gigabit |
| EBS-Bandbreite (Baseline) | 312 Mbps |

## Lokaler Start

Beispiel aus dem Ordner `aws-http-server`:

```bash
npm install
npm run dev
```
