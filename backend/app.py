from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api/test")
def test():
    return jsonify({"message": "API is working!"})