"""
Simple Flask counter app for Docker Level 1.

This app counts page visits in memory. Each GET to / increments the counter.
The /health endpoint returns a status check.

NOTE: Do NOT modify this file. Write a Dockerfile to containerize it.
"""

from flask import Flask, jsonify

app = Flask(__name__)
visit_count = 0


@app.route("/")
def index():
    global visit_count
    visit_count += 1
    return f"Hello! You are visitor #{visit_count}\n"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
