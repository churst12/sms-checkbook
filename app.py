import os
from flask import Flask
import json
import requests
from flask import render_template


#plzwork
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title='Home')

@app.route("/send")
def postDigital():
	#headers = {'Authorization': '1e55402a63d64eeea4d633f0efcb432d':'WnyNnTkSN6PY4Be1fk99KHGN5yVMEB'}
	#hello
	url = "https://sandbox.checkbook.io/v3/check/digital"
	data = {'name':'Test Inc.',
			'recipient':'widgets@example.com', 
			'amount': 10.42
			}
	#r = request.post( url, headers=headers, data=data)
	print "BEFORE BEFORE"
	r = requests.post(url, data=data, headers={'Authorization':'6467326cd8274bb29b72d307cf39a9e9:bLCfg6rdOwMpCURUo77S52EzF78TMo'})
	print "AFTER AFTER"
	return r.text
	

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run()