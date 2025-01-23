const { BUTTONDOWN_API_KEY } = process.env;
import fetch from "node-fetch";

exports.handler = async (event, context) => {
  try {
    const email = JSON.parse(event.body).payload.email;
    console.log('DEBUG: Starting function');
    console.log(`DEBUG: Email received: ${email}`);
    console.log('DEBUG: API Key exists:', !!BUTTONDOWN_API_KEY);

    const response = await fetch("https://api.buttondown.email/v1/subscribers", {
      method: "POST",
      headers: {
        Authorization: `Token ${BUTTONDOWN_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email_address: email }),
    });

    const responseText = await response.text();
    console.log('DEBUG: Response status:', response.status);
    console.log('DEBUG: Response body:', responseText);

    return {
      statusCode: response.status,
      body: JSON.stringify({
        status: response.status,
        response: responseText,
        message: 'Check logs for details'
      })
    };
  } catch (error) {
    console.error('DEBUG: Error caught:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: error.message,
        stack: error.stack
      })
    };
  }
};
