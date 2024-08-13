from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)
