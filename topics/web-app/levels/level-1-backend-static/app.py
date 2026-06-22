from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)
entries = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        if name and message:
            entries.append({
                "name": name,
                "message": message,
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        return redirect(url_for("index"))
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
