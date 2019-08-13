from app import app
from config import Config, SafaricomPrefix
import africastalking
from flask_api import status
from flask import request
import json


username = Config.AT_USERNAME
api_key = Config.AT_API_KEY
africastalking.initialize(username, api_key)

#Initialize payments module under data variable
data_bundles = africastalking.Payment

# Data cleaning functions

def validate_phone_number(number):
    if isinstance(number, str):
        first_value = number[0]
        if first_value is '0':
            number.replace('0','+254')
        elif '+254' in number:
            return number
        else:
            raise ValueError('This is not a valid phone number')

#Validate if phone number is A safaricom based one

def validate_phone_number_is_safaricom(number):
    first_four_numbers = number[0:4]
    if SafaricomPrefix.SAFARICOM_NUMBERS in first_four_numbers:
        return number
    else:
        raise ValueError('This is not a Safaricom Phone number')

#Routes for the API

@app.route('/')
def index():
    return 'Hello world, we are live!'

# Sending data to multiple users

@app.route('/api/v1/sendingdata', methods = ['GET','POST'])
def sendingdata():
    #return 'Sending data live'
    data = request.get_json(force=True)
    print(data)
    phone_number = data['phoneNumber']
    data_amount = int(data['dataAmount'])
    data_unit = data['dataUnit']
    validity = data['dataValidity']

    try:
        validate_phone_number_is_safaricom(phone_number)
        validate_phone_number(phone_number)
    except Exception as e:
        print(f'Houston at validation, we have a problem: {e}')

    data_details = [{
        "phoneNumber": str(phone_number),
        "quantity": int(data_amount),
        "unit": str(data_unit),
        "validity": str(validity),
        "metadata": {
            "foo":"bar"
        }
    }]

    try:
        response = data_bundles.mobile_data(product_name = Config.PRODUCT_NAME, recipients = data_details)
        print(response)
    except Exception as e:
        print(f'Houston, we have a problem {e}')


# Sending data to multiple users

@app.route('/api/v1/sendingdata/many', methods = ['GET','POST'])
def sendingdata_multiple():
      pass


# Getting data purchase notifications from the AT API

@app.route('/api/v1/sendingdata/notifications', methods = ['GET','POST'])
def sendingdata_notifications():
    return 'Sending data notifications live'