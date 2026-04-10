import json
import urllib3

TARGET_URL = "http://3.75.142.92:3000/post-request"

http = urllib3.PoolManager()

def lambda_handler(event, context):
    try:
        data = {
            "first_name": "Mats",
            "last_name": "Winter",
            "email": "mats.winter@example.com",
            "job": "Backend Developer"
        }

        json_body = json.dumps(data)
        print(f"Sende POST-Request mit Daten: {json_body}")

        response = http.request(
            'POST',
            TARGET_URL,
            body=json_body,
            headers={'Content-Type': 'application/json'}
        )

        print(f"Response Status Code: {response.status}")
        response_text = response.data.decode('utf-8')
        print(f"Response Body: {response_text}")

        return {
            "statusCode": response.status,
            "responseBody": response_text
        }

    except Exception as e:
        print(f"Fehler beim Senden des POST-Requests: {str(e)}")
        
        return {
            "statusCode": 500,
            "error": str(e)
        }
