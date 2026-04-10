import urllib3

http = urllib3.PoolManager()
TARGET_URL = "http://54.93.232.213:3000/get-request"

def lambda_handler(event, context):
    try:
        print(f"Sende GET-Request an: {TARGET_URL}")

        response = http.request('GET', TARGET_URL)
        
        response_text = response.data.decode('utf-8')

        print(f"Response Status Code: {response.status}")
        print(f"Response Body: {response_text}")

        return {
            "statusCode": response.status,
            "responseBody": response_text
        }
    except Exception as e:
        print(f"Fehler beim GET-Request: {str(e)}")
        return {
            "statusCode": 500,
            "error": str(e)
        }