from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself suazn.",
    "You are capable of amazing things.",
    "Every day is a fresh start.",
    "Stay positive and strong.",
    "Work hard and be kind."
]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
