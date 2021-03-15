from flask import Flask
from flask import request
from flask import render_template

import json

app = Flask(__name__)

@app.before_first_request

@app.route("/", methods=["GET", "POST"])
def render():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=1200, debug=True)
