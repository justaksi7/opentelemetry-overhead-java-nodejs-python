package com.example;

import java.util.HashMap;
import java.util.Map;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;

public class DynamoDB_Read implements RequestHandler<Object, Map<String, Object>> {

    
    private static final DynamoDbClient DYNAMO_DB_CLIENT = DynamoDbClient.builder()
            .region(Region.EU_CENTRAL_1)
            .build();

    private static final String TABLE_NAME = "EvaluationTable";

    @Override
    public Map<String, Object> handleRequest(Object input, Context context) {
        String uniqueId = "2154b8e4-c7f2-462d-a26b-0f8857729c73";
        Map<String, Object> responseMap = new HashMap<>();

        try {
            Map<String, AttributeValue> keyToGet = new HashMap<>();
            keyToGet.put("Id", AttributeValue.builder().s(uniqueId).build());

            GetItemRequest request = GetItemRequest.builder()
                    .tableName(TABLE_NAME)
                    .key(keyToGet)
                    .build();

            GetItemResponse result = DYNAMO_DB_CLIENT.getItem(request);

            context.getLogger().log("Leseoperation erfolgreich für ID: " + uniqueId + "\n");

            responseMap.put("statusCode", 200);
            responseMap.put("body", "{\"message\": \"Success\", \"id\": \"" + uniqueId + "\"}");

        } catch (DynamoDbException e) {
            context.getLogger().log("Fehler beim Lesen in DynamoDB: " + e.getMessage() + "\n");
            
            responseMap.put("statusCode", 500);
            responseMap.put("body", "{\"error\": \"Interner Serverfehler\"}");
        }

        return responseMap;
    }
}