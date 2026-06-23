from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

entries = []

def validate_entry(data):
    name = (data.get("name") or "").strip()
    message = (data.get("message") or "").strip()
    if not name:
        return False, "name is required and cannot be empty"
    if len(name) > 100:
        return False, "name must be 100 characters or fewer"
    if not message:
        return False, "message is required and cannot be empty"
    if len(message) > 500:
        return False, "message must be 500 characters or fewer"
    return True, None

@app.route("/api/entries", methods=["GET"])
def get_entries():
    return jsonify(entries), 200

@app.route("/api/entries", methods=["POST"])
def create_entry():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400
    ok, error_msg = validate_entry(data)
    if not ok:
        return jsonify({"error": error_msg}), 400
    entry = {
        "id": len(entries) + 1,
        "name": data["name"].strip(),
        "message": data["message"].strip(),
    }
    entries.append(entry)
    return jsonify(entry), 201

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "status": 404}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error", "status": 500}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
