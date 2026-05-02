from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["post", "get"])
def index():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        message = int(area) * 300_000
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run()