const { BUTTONDOWN_API_KEY } = process.env;
import fetch from "node-fetch";

exports.handler = async (event, context) => {
  try {
    const email = JSON.parse(event.body).payload.email;
    console.log(`Subscribing email: ${email}`);

    const response = await fetch("https://api.buttondown.email/v1/subscribers", {
      method: "POST",
      headers: {
        Authorization: `Token ${BUTTONDOWN_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email_address: email }),
    });

    const responseData = await response.json();

    if (response.ok) {
      return {
        statusCode: 200,
        body: JSON.stringify({
          message: "Successfully subscribed to newsletter"
        })
      };
    } else {
      console.error("Subscription error:", responseData);
      return {
        statusCode: response.status,
        body: JSON.stringify({
          message: "Error subscribing to newsletter"
        })
      };
    }
  } catch (error) {
    console.error("Function error:", error);
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: "Internal server error"
      })
    };
  }
};
