from flask import render_template

from application import app

@app.route("/")
def homepage():
    return render_template("index.html")

from application.activities import views
from application.authentication import views