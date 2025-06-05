from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "People who are crazy enough to think they can change the world, are the ones who do."
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
