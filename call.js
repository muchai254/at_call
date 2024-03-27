const express = require('express');
const bodyParser = require('body-parser');
const africastalking = require('africastalking')({
  apiKey: 'f1bf750e8d593590c31aa0188b5b60cfc34aae3d9cb7f7fc0c50c4ec4bb5a59e',
  username: 'cyberpark'
});

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.urlencoded({ extended: false }));

app.post('/', (req, res) => {
  const isActive = req.body.isActive;

  if (isActive === '1') {
    const callerNumber = req.body.callerNumber;
    const text = "Humidity exceeded, Humidity exceeded, Humidity exceeded, Humidity exceeded";
    const response = `<?xml version="1.0" encoding="UTF-8"?>
                      <Response>
                          <Say>${text}</Say>
                      </Response>`;
    res.status(200).type('text/xml').send(response);
  } else {
    const duration = req.body.durationInSeconds;
    const currencyCode = req.body.currencyCode;
    const amount = req.body.amount;
    res.sendStatus(204);
  }
});

class Voice {
  constructor() {
    this.voice = africastalking.Voice;
  }

  async call() {
    const callFrom = "+254711082038";
    const callTo = ["+254757669716"];

    try {
      const result = await this.voice.call({
        from: callFrom,
        to: callTo
      });
      console.log(result);
    } catch (error) {
      console.error(`Encountered an error while making the call: ${error}`);
    }
  }
}

app.get('/call', (req, res) => {
  try {
    new Voice().call();
    res.send('<p>Call has been made!</p>');
  } catch (error) {
    res.send('<p>Error making call:</p>');
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
