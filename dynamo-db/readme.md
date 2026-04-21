# dynamo-db

## AWS-DynamoDB-Tabellenstruktur

Dieses Projekt verwendet die Tabelle `EvaluationTable`.

Dokumentierte Struktur (wie von den Benchmark-Funktionen genutzt):

```javascript
TableName: 'EvaluationTable',
Key: {
	Id: { S: '...' }
}
```

## Tabellenkonfiguration

Die DynamoDB-Tabelle wurde mit folgenden Parametern konfiguriert:

| Parameter | Wert |
|---|---|
| Tabellenname | `EvaluationTable` |
| Primärschlüssel | `Id` (String-UUID) |
| Lesekapazitätsmodus | On-demand (Standard) |
| Schreibkapazitätsmodus | On-demand (Standard) |
| Verschlüsselung | AWS Owned Key (Standard) |
| Point-in-time Recovery | Deaktiviert (Standard) |
| Region | eu-central-1 (Frankfurt) |

## Key-Schema

- Tabelle: `EvaluationTable`
- Primärschlüssel: `Id` (String-UUID)
- Beispiel-Schlüsselabfrage: `Id = <uuid>`

