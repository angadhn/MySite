const { BUTTONDOWN_API_KEY } = process.env;
import fetch from "node-fetch";

exports.handler = async (event, context) => {
  const email = JSON.parse(event.body).payload.email;
  console.log(`Received a submission: ${email}`);
  console.log('Using API key:', BUTTONDOWN_API_KEY ? 'Key exists' : 'No key found');

  const response = await fetch("https://api.buttondown.email/v1/subscribers", {
    method: "POST",
    headers: {
      Authorization: `Token ${BUTTONDOWN_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email }),
  });

  let responseText = await response.text();
  console.log('Response status:', response.status);
  console.log('Response body:', responseText);

  return {
    statusCode: response.status,
    body: responseText
  };
};
