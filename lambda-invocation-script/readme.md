# lambda-invocation-script

## Zweck

Dieser Ordner enthaelt ein Python-Skript, das eine AWS-Lambda-Funktion asynchron und mit konfigurierbarer Parallelitaet mehrfach aufruft.

Datei:

- `Lambda_Invocation_Script.py`

## Was das Skript macht

Das Skript:

1. baut ein kleines JSON-Payload,
2. legt eine Gesamtzahl von Aufrufen fest,
3. begrenzt die Gleichzeitigkeit ueber ein Semaphore,
4. sendet asynchrone Lambda-Aufrufe mit `InvocationType="Event"`,
5. misst die Gesamtdauer und gibt den Durchsatz aus.

## Wichtige Konfigurationswerte im Skript

- `LAMBDA_NAME`: Ziel-Lambda (ARN)
- `TOTAL_INVOCATIONS`: Anzahl geplanter Aufrufe
- `MAX_CONCURRENCY`: Maximale gleichzeitige Aufrufe

Hinweis: Vor der Ausfuehrung muss `LAMBDA_NAME` im Skript auf eine gueltige Ziel-Funktion gesetzt werden.
