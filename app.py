from flask import Flask, render_template, jsonify
from core.runner import start, results
from core.scorer import calculate
import json



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start_test():
    if results["status"] != "running":
        start()
    return jsonify({"status": "started"})

@app.route("/status")
def status():
    data = results.copy()
    if data["status"] == "completed":
        data["score"] = calculate(data)
    return jsonify(data)

with open("results/results.json", "w") as f:
    json.dump(results, f, indent=4)

if __name__ == "__main__":
    app.run(debug=True)