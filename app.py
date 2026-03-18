from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow all origins

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    print("Received data:", data)
    return {"status": "ok"}
