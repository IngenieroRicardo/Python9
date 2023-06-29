from flask import Flask
from flask_ngrok2 import run_with_ngrok #libreria o packete ngrok
app = Flask(__name__)
run_with_ngrok(app, auth_token='24Tds7JSma4pbcB5ENNSn6AEBra_eGVPfHpxbDweenZq7JX4') #token ngrok 

@app.route("/")
def index():
    return "<h1>Hola Mundo</h1>"
    
app.run()
