import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";
import { randomUUID } from "crypto";

const client = new DynamoDBClient({ region: "eu-central-1" });

export const handler = async () => {
  const id = randomUUID();

  try {
    await client.send(
      new PutItemCommand({
        TableName: "EvaluationTable",
        Item: {
          Id: { S: id },
          Value: { S: "New Item" }
        }
      })
    );

    return { 
      statusCode: 200,
      body: JSON.stringify({ message: "Success", id }) 
    };
  } catch (error) {
    console.error("Fehler beim Schreiben in DynamoDB:", error);
    
    return { 
      statusCode: 500,
      body: JSON.stringify({ error: "Interner Serverfehler" }) 
    };
  }
};
