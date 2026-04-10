import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('EvaluationTable')

def lambda_handler(event, context):
    unique_id = "cf19b76e-54e6-4672-bcc3-e25bde8721f8"
    try:
        table.get_item(
            Key={
                'Id': unique_id
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
        print(f"Fehler beim Lesen in DynamoDB: {e}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Interner Serverfehler'
            })
        }
