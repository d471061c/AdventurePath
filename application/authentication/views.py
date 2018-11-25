from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from .models import Account
from .forms import LoginForm

@app.route("/login", methods = ["POST"])
def login():
    login_form = LoginForm()
    print("Login form: ",login_form)
    account = Account.query.filter_by(username=login_form.username.data, password=login_form.password.data).first()
    if not account:
        return render_template("authentication/login.html", form = login_form, error = "No such username and password")
    
    login_user(account)
    return redirect(url_for("homepage"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/login", methods = ["GET"])
def login_page():
    login_form = LoginForm()
    return render_template("authentication/login.html", form = login_form)

