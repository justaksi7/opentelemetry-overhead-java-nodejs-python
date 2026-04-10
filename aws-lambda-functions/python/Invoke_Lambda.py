import boto3
import json

lambda_client = boto3.client('lambda')
TARGET_FUNCTION = "arn:aws:lambda:eu-central-1:191880149831:function:invocation-Lambda"

def lambda_handler(event, context):
    try:
        payload_data = {"message": "Hello from Python Lambda"}
        
        lambda_client.invoke(
            FunctionName=TARGET_FUNCTION,
            InvocationType='Event',  
            Payload=json.dumps(payload_data)
        )

        print("Invocation sent (async)")
        return "ok"
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return "error"