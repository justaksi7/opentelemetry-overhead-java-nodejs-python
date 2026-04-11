# dynamo-db

## AWS DynamoDB Table Structure

This project uses the `EvaluationTable` table.

Documented structure (as used by the benchmark functions):

```javascript
TableName: 'EvaluationTable',
Key: {
	Id: { S: '...' }
}
```

## Table Configuration

The DynamoDB table was configured with the following parameters:

| Parameter | Value |
|---|---|
| Table name | `EvaluationTable` |
| Primary key | `Id` (String-UUID) |
| Read capacity mode | On-demand (standard) |
| Write capacity mode | On-demand (standard) |
| Encryption | AWS Owned Key (standard) |
| Point-in-time recovery | Disabled (standard) |
| Region | eu-central-1 (Frankfurt) |

## Key Schema

- Table: `EvaluationTable`
- Primary key: `Id` (String-UUID)
- Example key lookup: `Id = <uuid>`

