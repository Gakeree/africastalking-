from flask import Flask, request
import africastalking

app = Flask(__name__)

# Initialize the AfricasTalkingGateway object with your API key and username
username = "kenedygakere@gmail.com"
api_key = "ea40a20d431a791c6928b56799e3491dd66761f800c1ac291089007d89eba74c"
africastalking.initialize(username, api_key)
 

@app.route('/', methods=['POST'])
def ussd():
    session_id = request.values.get('sessionId', None)
    phone_number = request.values.get('phoneNumber', None)
    service_code = request.values.get('serviceCode', None)
    ussd_input = request.values.get('text', 'default')

    if ussd_input == '':
        # first time USSD is called
        response = 'CON Welcome to the Hackathon Event Registration\n'
        response += 'Please choose an option:\n'
        response += '1. Register for the event\n'
        response += '2. Exit\n'
    elif ussd_input == '1':
        # user chooses to register for the event
        response = 'CON Please enter your name:\n'
    elif ussd_input.startswith('1*'):
        # user enters their name for registration
        name = ussd_input.split('*')[1]
        response = f'END Thank you for registering, {name}! We will send you a confirmation message shortly.\n'
    elif ussd_input == '2':
        # user chooses to exit
        response = 'END Thank you for using our service!\n'
    else:
        response = 'END Invalid input. Please try again.\n'
        
    # Send the USSD response back to the user using the AfricasTalkingGateway object
    gateway.send_ussd_push_message(phone_number, response, service_code, session_id)
    
    return ''

if __name__ == '__main__':
    app.run(port=5000, debug=True)
