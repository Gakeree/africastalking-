from flask import Flask
import africastalking


# Initialize AfricasTalking with your API key and sender ID
africastalking.initialize(api_key='', username='')
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
 
