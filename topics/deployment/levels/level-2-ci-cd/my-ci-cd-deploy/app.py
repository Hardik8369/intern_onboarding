"""
Flask app for Deployment Level 2 — CI/CD.

This app exposes a /version endpoint that should show the Git commit hash.
The commit hash is passed via the COMMIT_HASH environment variable.

Do NOT modify this file unless a constraint requires it.
"""

import os
from flask import Flask, jsonify

app = Flask(__name__)

# The Dockerfile should set COMMIT_HASH as an environment variable
COMMIT_HASH = os.environ.get("COMMIT_HASH", "unknown")
APP_NAME = "ci-cd-app"


@app.route("/")
def index():
    return f"Hello from {APP_NAME}! Commit: {COMMIT_HASH}\n"


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "app": APP_NAME,
    })


@app.route("/version")
def version():
    return jsonify({
        "version": COMMIT_HASH,
        "app": APP_NAME,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
