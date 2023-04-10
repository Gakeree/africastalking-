from flask import Flask
import africastalking


# Initialize AfricasTalking with your API key and sender ID
africastalking.initialize(api_key='4e4a41d67dcec3a6705b5a069e3dce627931395570a28f53a4b614d00017c937', username='smskennar')
sms = africastalking.SMS

app = Flask(__name__)

@app.route('/send_sms')
def send_sms():
    to = ['+254705896124', '+254716248935']  # list of phone numbers to send message to
    message = 'Hello, Thank you for participating in SEKU Hackathon Day! See you Next time. From Your Instructor; @kengakere'
    response = sms.send(message, to)
    if all(recipient['status'] == 'Success' for recipient in response['SMSMessageData']['Recipients']):
        return 'SMS sent successfully to all recipients!'
    else:
        return 'Failed to send SMS to all recipients.'

if __name__ == '__main__':
    app.run(debug=True)
username = "kenedygakere@gmail.com"
api_key = "ea40a20d431a791c6928b56799e3491dd66761f800c1ac291089007d89eba74c"