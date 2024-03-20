# works with both python 2 and 3
from flask import Flask, request
import os
import africastalking

app = Flask(__name__)

class Voice:
    def __init__(self):
        # Set your app credentials
        self.username = "cyberpark"
        self.api_key = "87027f64b2f831607891cf7814feec9e73d0b4a6eda61c2f11fd6ac1bc0e865e"
        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        # Get the voice service
        self.voice = africastalking.Voice

    def call(self):
        # Set your Africa's Talking phone number in international format
        call_from = "+254711082038"
        # Set the numbers you want to call to in a comma-separated list
        call_to = ["+254757610846"]
        try:
            # Make the call
            result = self.voice.call(call_from, call_to)
            print(result)
        except Exception as e:
            print("Encountered an error while making the call: %s" % str(e))

@app.route('/call', methods=['POST', 'GET'])
def making_a_call():
    data = request.form.get('data', '') or request.args.get('temperature', '')
    try:
        voice = Voice()
        voice.call()
        return "<p>Call has been made!</p>"
    except Exception as e:
        return "<p>Error making call: %s</p>" % str(e)

@app.route('/', methods=['POST'])
def call_back_endpoint():
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')

    if is_active == '1':
        caller_number = request.form.get('callerNumber')
        text = "the driver is drunk. Kindly come pick him at dedan kimathi university of technology near S.T.L"
        response = f'''<?xml version="1.0" encoding="UTF-8"?>
                      <Response>
                          <Say>{text}</Say>
                      </Response>'''
        return response, 200, {'Content-Type': 'text/xml'}
    else:
        duration = request.form.get('durationInSeconds')
        currency_code = request.form.get('currencyCode')
        amount = request.form.get('amount')
        return '', 204

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))
