package com.example;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.google.gson.Gson;

public class POST_Request implements RequestHandler<Object, Map<String, Object>> {

    private static final HttpClient HTTP_CLIENT = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_1_1)
            .build();
            
    private static final Gson GSON = new Gson();
    private static final String TARGET_URL = "http://52.29.42.146:3000/post-request";

    @Override
    public Map<String, Object> handleRequest(Object input, Context context) {
        try {
            Map<String, String> data = new HashMap<>();
            data.put("first_name", "Mats");
            data.put("last_name", "Winter");
            data.put("email", "mats.winter@example.com");
            data.put("job", "Backend Developer");

            String jsonBody = GSON.toJson(data);
            System.out.println("Sende POST-Request mit Daten: " + jsonBody);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(TARGET_URL))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                    .build();

            HttpResponse<String> response = HTTP_CLIENT.send(request, HttpResponse.BodyHandlers.ofString());
            String responseText = response.body();

            System.out.println("Response Status Code: " + response.statusCode());
            System.out.println("Response Body: " + responseText);

            Map<String, Object> responseMap = new HashMap<>();
            responseMap.put("statusCode", response.statusCode());
            responseMap.put("responseBody", responseText);
            return responseMap;

        } catch (Exception e) {
            System.err.println("Fehler beim Senden des POST-Requests: " + e.getMessage());
            
            Map<String, Object> errorMap = new HashMap<>();
            errorMap.put("statusCode", 500);
            errorMap.put("error", e.getMessage());
            return errorMap;
        }
    }
}