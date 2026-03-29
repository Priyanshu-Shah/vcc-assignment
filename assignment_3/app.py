from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Running on LOCAL VM"

app.run(host='0.0.0.0', port=5000)