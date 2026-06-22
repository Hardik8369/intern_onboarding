#!/usr/bin/env python3
"""Guestbook API backend with CORS support."""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

entries = []

@app.route("/api/entries", methods=["GET"])
def get_entries():
    return jsonify(entries), 200

@app.route("/api/entries", methods=["POST"])
def create_entry():
    data = request.json
    if not data or not data.get("name") or not data.get("message"):
        return jsonify({"error": "name and message are required"}), 400
    entry = {
        "id": len(entries) + 1,
        "name": data["name"].strip(),
        "message": data["message"].strip(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    entries.append(entry)
    return jsonify(entry), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
