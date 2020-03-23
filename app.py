from flask import Flask
from flask import render_template

from config import apply_config

app = Flask(__name__)
apply_config(app)


@app.route("/", )
def index():
    return render_template("index.html", )
