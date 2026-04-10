import boto3
import uuid
import json

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('EvaluationTable')

def lambda_handler(event, context):
    unique_id = str(uuid.uuid4())
    
    try:
        table.put_item(
            Item={
                'Id': unique_id,
                'Value': 'New Item'
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Success',
                'id': unique_id
            })
        }
        
    except Exception as e:
        print(f"Fehler beim Schreiben in DynamoDB: {e}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Interner Serverfehler'
            })
        }