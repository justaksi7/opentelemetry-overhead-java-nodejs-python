const TARGET_URL = "http://54.93.232.213:3000/get-request";

export const handler = async (event) => {
    try {
        console.log(`Sende GET-Request an: ${TARGET_URL}`);

        const response = await fetch(TARGET_URL);
        
        const responseText = await response.text();

        console.log(`Response Status Code: ${response.status}`);
        console.log(`Response Body: ${responseText}`);

        return {
            "statusCode": response.status,
            "responseBody": responseText
        };
    } catch (error) {
        console.error(`Fehler beim GET-Request: ${error.message}`);
        return {
            "statusCode": 500,
            "error": error.message
        };
    }
};
