import { LambdaClient, InvokeCommand } from "@aws-sdk/client-lambda";

const lambdaClient = new LambdaClient({});
const TARGET_FUNCTION = "arn:aws:lambda:eu-central-1:191880149831:function:invocation-Lambda";

export const handler = async (event, context) => {
    try {
        const payload = JSON.stringify({ "message": "Hello from Node Lambda" });

        const command = new InvokeCommand({
            FunctionName: TARGET_FUNCTION,
            InvocationType: "Event", 
            Payload: new TextEncoder().encode(payload)
        });

        await lambdaClient.send(command);

        console.log("Invocation sent (async)");
        return "ok";
        
    } catch (error) {
        console.error("Error: " + error.message);
        return "error";
    }
};