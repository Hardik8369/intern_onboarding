"""Flask app with Redis integration for visit counter."""
from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Connect to Redis at hostname 'redis' (compose service name)
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("visit_count")
    return f"Hello! You are visitor #{count}\n"

@app.route("/health")
def health():
    try:
        r.ping()
        redis_status = "connected"
    except Exception:
        redis_status = "disconnected"
    return jsonify({"status": "ok", "redis": redis_status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
