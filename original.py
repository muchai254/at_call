# works with both python 2 and 3
from _future_ import print_function
#my code
from flask import Flask, request
# import threading 
# import paho.mqtt.client as mqtt
import requests
import json
# from mqtt import start_mqtt_subscriber
app = Flask(_name_)
import os
# mqtt_data = {}



import africastalking


# current_temperature = ''

@app.route('/call', methods=['POST', 'GET'])
def making_a_call():
    global data
    data = request.form.get('data', '') or request.args.get('temperature', '') 
    try:
        VOICE().call()
        return "<p>Call has been made!</p>"
    except:
        return "<p>Error making call!</p>"
    

    
@app.route('/', methods=['POST'])
def call_back_endpoint():
    # Read in a couple of POST variables passed in with the request
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')

    if is_active == '1':
        # Read in the caller's number. The format will contain the + in the beginning
        caller_number = request.form.get('callerNumber')

      

        text = "the driver is drunk. Kindly come pick him at dedan kimathi university of technology near S.T.L"
        # text = f"Sensor reading is {current_temperature}"
        # if current_temperature:
        #     text = f"Sensor reading is {current_temperature}"
        # else:
        #     text = f"There is no reading"
            
        # Compose the response
        response = f'''<?xml version="1.0" encoding="UTF-8"?>
                      <Response>
                          <Say>{text}</Say>
                      </Response>'''

        # Print the response onto the page so that our gateway can read it
        return response, 200, {'Content-Type': 'text/xml'}
    else:
        # Read in call details (duration, cost). This flag is set once the call is completed.
        # Note that the gateway does not expect a response in this case
        duration = request.form.get('durationInSeconds')
        currency_code = request.form.get('currencyCode')
        amount = request.form.get('amount')

        # You can then store this information in the database for your records
        return '', 204

class VOICE:
    def _init_(self):
		# Set your app credentials
        self.username = "cyberpark"
        self.api_key = "87027f64b2f831607891cf7814feec9e73d0b4a6eda61c2f11fd6ac1bc0e865e"
		# Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
		# Get the voice service
        self.voice = africastalking.Voice

    def call(self):
        # Set your Africa's Talking phone number in international format
        callFrom = "+254711082038"
        # Set the numbers you want to call to in a comma-separated list
        callTo   = ["+254726109415"]
        try:
			# Make the call
            result = self.voice.call(callFrom, callTo)
            print (result)

            
        
         
            
        except Exception as e:
            print ("Encountered an error while making the call:%s" %str(e))

if _name_ == '_main_':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))