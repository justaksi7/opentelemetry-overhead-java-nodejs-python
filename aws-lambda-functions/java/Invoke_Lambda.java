package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import software.amazon.awssdk.services.lambda.LambdaClient;
import software.amazon.awssdk.services.lambda.model.InvokeRequest;
import software.amazon.awssdk.services.lambda.model.InvocationType;
import software.amazon.awssdk.core.SdkBytes;

public class Invoke_Lambda implements RequestHandler<Object, String> {

    private static final LambdaClient lambdaClient = LambdaClient.builder().build();
    private static final String TARGET_FUNCTION = "target-lambda-name";

    @Override
    public String handleRequest(Object input, Context context) {
        try {
            InvokeRequest req = InvokeRequest.builder()
                    .functionName(TARGET_FUNCTION)
                    .invocationType(InvocationType.EVENT) // 🔥 async
                    .payload(SdkBytes.fromUtf8String("{\"message\":\"Hello from Java Lambda\"}"))
                    .build();

            lambdaClient.invoke(req);

            context.getLogger().log("Invocation sent (async)\n");
            return "ok";
        } catch (Exception e) {
            context.getLogger().log("Error: " + e.getMessage());
            return "error";
        }
    }
}