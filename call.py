# works with both python 2 and 3
from flask import Flask, request, jsonify
import requests
import json
import os
import africastalking
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={ r'/*': { "origins": ["https://aimron001.github.io"]}})





@app.route('/call', methods=['GET', 'POST'])
def making_a_call():
     global data
     global text
     data = request.get_json()
     text = data.get('message', 'No message received')
     print(text)
     try:
        Voice().call()
        return "<p>Call has been made!</p>"
     except:
        return "<p>Error making call:</p>"

@app.route('/', methods=['POST'])
def call_back_endpoint():
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')

    if is_active == '1':
        caller_number = request.form.get('callerNumber')
        # text = "Humidity exceeded, Humidity exceeded, Humidity exceeded, Humidity exceeded"
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

class Voice:
    def __init__(self):
        # Set your app credentials
        self.username = "cyberpark"
        self.api_key = "f1bf750e8d593590c31aa0188b5b60cfc34aae3d9cb7f7fc0c50c4ec4bb5a59e"
        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        # Get the voice service
        self.voice = africastalking.Voice

    def call(self):
        # Set your Africa's Talking phone number in international format
        call_from = "+254711082038"
        # Set the numbers you want to call to in a comma-separated list
        call_to = ["+254794011959"]
        try:
            # Make the call
            result = self.voice.call(call_from, call_to)
            print(result)
        except Exception as e:
            print("Encountered an error while making the call: %s" % str(e))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))
