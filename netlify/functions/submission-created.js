const { BUTTONDOWN_API_KEY } = process.env;
const fetch = require('node-fetch');

exports.handler = async (event, context) => {
  const email = JSON.parse(event.body).payload.email;
  console.log(`Received a submission: ${email}`);

  try {
    const response = await fetch("https://api.buttondown.email/v1/subscribers", {
      method: "POST",
      headers: {
        Authorization: `Token ${BUTTONDOWN_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email }),
    });

    let responseText = await response.text();
    console.log("Response:", responseText);

    if (!response.ok) {
      return {
        statusCode: response.status,
        body: JSON.stringify({ error: responseText })
      };
    }

    return {
      statusCode: 200,
      body: JSON.stringify({ message: "Subscription successful" })
    };
  } catch (error) {
    console.error('Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: "Internal server error" })
    };
  }
};
