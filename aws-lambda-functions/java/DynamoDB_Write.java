package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class DynamoDB_Write implements RequestHandler<Object, Map<String, Object>> {

    private static final DynamoDbClient DYNAMO_DB_CLIENT = DynamoDbClient.builder()
            .region(Region.EU_CENTRAL_1)
            .build();

    private static final String TABLE_NAME = "EvaluationTable";

    @Override
    public Map<String, Object> handleRequest(Object input, Context context) {
        String uniqueId = UUID.randomUUID().toString();
        Map<String, Object> response = new HashMap<>();

        try {
            Map<String, AttributeValue> item = new HashMap<>();
            item.put("Id", AttributeValue.builder().s(uniqueId).build());
            item.put("Value", AttributeValue.builder().s("New Item").build());

            PutItemRequest request = PutItemRequest.builder()
                    .tableName(TABLE_NAME)
                    .item(item)
                    .build();

            DYNAMO_DB_CLIENT.putItem(request);

            context.getLogger().log("Erfolgreich geschrieben: " + uniqueId);

            response.put("statusCode", 200);
            response.put("body", "{\"message\": \"Success\", \"id\": \"" + uniqueId + "\"}");

        } catch (DynamoDbException e) {
            context.getLogger().log("Fehler beim Schreiben in DynamoDB: " + e.getMessage());
            
            response.put("statusCode", 500);
            response.put("body", "{\"error\": \"Interner Serverfehler\"}");
        }

        return response;
    }
}