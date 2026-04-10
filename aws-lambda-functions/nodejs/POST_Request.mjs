const TARGET_URL = "http://3.75.142.92:3000/post-request";

export const handler = async (event) => {
    try {
        const data = {
            "first_name": "Mats",
            "last_name": "Winter",
            "email": "mats.winter@example.com",
            "job": "Backend Developer"
        };

        const jsonBody = JSON.stringify(data);
        console.log(`Sende POST-Request mit Daten: ${jsonBody}`);

        const response = await fetch(TARGET_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonBody
        });

        const responseText = await response.text();

        console.log(`Response Status Code: ${response.status}`);
        console.log(`Response Body: ${responseText}`);

        return {
            "statusCode": response.status,
            "responseBody": responseText
        };

    } catch (error) {
        console.error(`Fehler beim Senden des POST-Requests: ${error.message}`);
        
        return {
            "statusCode": 500,
            "error": error.message
        };
    }
};
