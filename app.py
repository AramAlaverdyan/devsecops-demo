from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Secure Web App! DevSecOps 2026.</h1>"

if __name__ == '__main__':
    # ԿԱՐԵՎՈՐ Է. Docker-ի ներսում պետք է լսել 0.0.0.0 պորտը, որ դրսից հասանելի լինի
    app.run(host='0.0.0.0', port=5000)
