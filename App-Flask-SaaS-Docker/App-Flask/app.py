# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Bienvenido a la App Flask en Google Cloud-GCP!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
