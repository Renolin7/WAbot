from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    nam = request.form.get('ProfileName')
    print(request.form.get)
    # Create reply
    if msg=='join steady-cut':
      resp = MessagingResponse()
      resp.message('Welcome '+nam+'\n\nThis Sandbox was created by Ren⚽lin')
    if msg=='hi':
       resp = MessagingResponse()
       resp.message('Hi '+nam)
   # resp = MessagingResponse()
    #resp.message("You said: {}".format(msg))

       return str(resp)

if __name__ == "__main__":
    app.run(debug=True)