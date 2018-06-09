import os
from flask import Flask
import json
import requests
from flask import render_template

Authorization= '23566e2b3f2d26921e2355bfd03497ee','16640e2b05a59751b7bf923737cb9942'
#plzwork
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title='Home')

@app.route("/send")
def postDigital():
	endpoint = "https://sandbox.checkbook.io/v3/check/digital"
	info = {"name":"Test Inc.",
			"recipient":"widgets@example.com", 
			"amount": 10.42
			}
	r = request.post( endpoint, data = info)
	#return r.text
	return "HI"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run()