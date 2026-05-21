from flask import Flask
from werkzeug.serving import WSGIRequestHandler

# 🥷 ՍՈՒՏ ԻՆՖՈ. Փոխում ենք Werkzeug սերվերի պաշտոնական այցեքարտը
WSGIRequestHandler.version_string = lambda self: "NASA-Mainframe-Secure/2026"

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Secure Web App! DevSecOps 2026.</h1>"

# 🛡️ ԲՈՒԺՈՒՄ ԵՆՔ CLICKJACKING-Ը. Ամեն հարցման պատասխանին կպցնում ենք անվտանգության պատերը
@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # nosec
