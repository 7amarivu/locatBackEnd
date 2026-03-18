from flask import Flask, request

app = Flask(__name__)

@app.route("/location", methods=["POST"])
def location():
    data = request.json
    print("Received location:", data)  # You can save to DB here
    return {"status": "ok"}

if __name__ == "__main__":
    app.run()
