#!/usr/bin/env python3
"""Bookmark Manager REST API using Flask."""
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory store
bookmarks = []
next_id = 1


def find_bookmark(bookmark_id):
    """Find a bookmark by ID."""
    return next((b for b in bookmarks if b["id"] == bookmark_id), None)


# GET /bookmarks — List all bookmarks
@app.route("/bookmarks", methods=["GET"])
def list_bookmarks():
    return jsonify(bookmarks), 200


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
    if not data or "title" not in data or "url" not in data:
        return jsonify({"error": "title and url are required"}), 400
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
