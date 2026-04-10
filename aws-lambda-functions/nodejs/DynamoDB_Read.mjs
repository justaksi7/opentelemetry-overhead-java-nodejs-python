import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({ region: "eu-central-1" });

export const handler = async () => {
  const id = "cf19b76e-54e6-4672-bcc3-e25bde8721f8"

  try {
    await client.send(new GetItemCommand({
      TableName: "EvaluationTable",
        Key: {"Id": {S: id}}
    }));

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