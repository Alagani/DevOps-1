from flask import Flask, jsonify, request

app = Flask(__name__)

data = []

@app.route("/")
def home():
    return "API is running"

@app.route("/data")
def get_data():
    return jsonify(data)

@app.route("/data", methods=["POST"])
def add_data():
    item = request.get_json()
    data.append(item)
    return jsonify(item), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)