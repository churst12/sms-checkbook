import os
from flask import Flask
import json
import requests
from flask import render_template
from twilio.rest import Client

#plzwork
app = Flask(__name__)

account_sid = "AC38da0daad1219a2eaf7c67b63d20e44b"
auth_token = "0001f81770b347148ff802674600de3a"
client = Client(account_sid, auth_token)

@app.route("/")
def hello():
    return render_template('index.html', title='Home')

@app.route("/send")
def postDigital():
	#+18317048704
	url = "https://sandbox.checkbook.io/v3/check/digital"
	dataDict = {'name':'Widgets Inc.',
			'recipient':'widgets@example.com', 
			'amount': 10.42
			}
	jsonDict = json.dumps(dataDict)
	#r = request.post( url, headers=headers, data=data)
	print "BEFORE BEFORE"
	r = requests.post(url, data=jsonDict, headers={'Authorization':'6467326cd8274bb29b72d307cf39a9e9:bLCfg6rdOwMpCURUo77S52EzF78TMo'})
	print "AFTER AFTER"
	message = client.messages.create(
    	to="+14087310723", 
    	from_="+18317048704",
    	body=r.text)
	return r.txt
	

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run()