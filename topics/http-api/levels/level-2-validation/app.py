#!/usr/bin/env python3
"""Bookmark Manager REST API — Level 2 with validation, search, and logging."""
from flask import Flask, jsonify, request
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)

app = Flask(__name__)

# In-memory store
bookmarks = []
next_id = 1


def validate_bookmark(data, require_all=True):
    """Validate bookmark data. Returns error message or None if valid."""
    if not data:
        return "Request body is required"
    if require_all:
        if "title" not in data:
            return "title is required"
        if "url" not in data:
            return "url is required"
    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return "title must be a non-empty string"
    if "url" in data:
        if not isinstance(data["url"], str):
            return "url must be a string"
        if not (data["url"].startswith("http://") or data["url"].startswith("https://")):
            return "url must start with http:// or https://"
    if "tags" in data:
        if not isinstance(data["tags"], list):
            return "tags must be a list"
        if not all(isinstance(t, str) for t in data["tags"]):
            return "tags must be a list of strings"
    return None


def find_bookmark(bookmark_id):
    """Find a bookmark by ID."""
    return next((b for b in bookmarks if b["id"] == bookmark_id), None)


@app.after_request
def log_request(response):
    """Log every request."""
    app.logger.info(f"{request.method} {request.path} → {response.status_code}")
    if response.status_code >= 500:
        app.logger.error(f"Server error: {request.method} {request.path}")
    return response


# GET /bookmarks — List all bookmarks with optional tag filter
@app.route("/bookmarks", methods=["GET"])
def list_bookmarks():
    tag = request.args.get("tag")
    if tag:
        result = [b for b in bookmarks if tag in b["tags"]]
    else:
        result = bookmarks
    return jsonify(result), 200


# GET /bookmarks/search?q=<query> — Search bookmarks by title
@app.route("/bookmarks/search", methods=["GET"])
def search_bookmarks():
    query = request.args.get("q", "").lower()
    result = [b for b in bookmarks if query in b["title"].lower()]
    return jsonify(result), 200


# GET /bookmarks/<id> — Get one bookmark
@app.route("/bookmarks/<int:bookmark_id>", methods=["GET"])
def get_bookmark(bookmark_id):
    bookmark = find_bookmark(bookmark_id)
    if bookmark is None:
        return jsonify({"error": "Bookmark not found"}), 404
    return jsonify(bookmark), 200


# POST /bookmarks — Create a bookmark
@app.route("/bookmarks", methods=["POST"])
def create_bookmark():
    global next_id
    data = request.json
    error = validate_bookmark(data, require_all=True)
    if error:
        app.logger.warning(f"Validation failed: {error}")
        return jsonify({"error": error}), 400
    bookmark = {
        "id": next_id,
        "title": data["title"],
        "url": data["url"],
        "tags": data.get("tags", []),
        "created_at": datetime.utcnow().isoformat()
    }
    bookmarks.append(bookmark)
    next_id += 1
    return jsonify(bookmark), 201


# PUT /bookmarks/<id> — Update a bookmark
@app.route("/bookmarks/<int:bookmark_id>", methods=["PUT"])
def update_bookmark(bookmark_id):
    bookmark = find_bookmark(bookmark_id)
    if bookmark is None:
        return jsonify({"error": "Bookmark not found"}), 404
    data = request.json
    error = validate_bookmark(data, require_all=False)
    if error:
        app.logger.warning(f"Validation failed: {error}")
        return jsonify({"error": error}), 400
    if "title" in data:
        bookmark["title"] = data["title"]
    if "url" in data:
        bookmark["url"] = data["url"]
    if "tags" in data:
        bookmark["tags"] = data["tags"]
    return jsonify(bookmark), 200


# DELETE /bookmarks/<id> — Delete a bookmark
@app.route("/bookmarks/<int:bookmark_id>", methods=["DELETE"])
def delete_bookmark(bookmark_id):
    bookmark = find_bookmark(bookmark_id)
    if bookmark is None:
        return jsonify({"error": "Bookmark not found"}), 404
    bookmarks.remove(bookmark)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
