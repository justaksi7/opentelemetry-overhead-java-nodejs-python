package com.example;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class GET_Request implements RequestHandler<Object, Map<String, Object>> {

    private static final HttpClient HTTP_CLIENT = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_1_1)
            .build();

    private static final String TARGET_URL = "http://3.75.142.92:3000/get-request";

    @Override
    public Map<String, Object> handleRequest(Object input, Context context) {
        try {
            System.out.println("Sende GET-Request an: " + TARGET_URL);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(TARGET_URL))
                    .GET()
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
            System.err.println("Fehler beim GET-Request: " + e.getMessage());
            Map<String, Object> errorMap = new HashMap<>();
            errorMap.put("statusCode", 500);
            errorMap.put("error", e.getMessage());
            return errorMap;
        }
    }
}