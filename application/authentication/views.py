from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from .models import Account
from .forms import LoginForm, RegisterForm
from .configuration import bcrypt

@app.route("/login", methods = ["POST"])
def login():
    login_form = LoginForm()
    print("Login form: ",login_form)
    account = Account.query.filter_by(username=login_form.username.data).first()
    if not account or not bcrypt.check_password_hash(account.password, login_form.password.data):
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

@app.route("/register", methods = ["GET"])
def registration_page():
    register_form = RegisterForm()
    return render_template("authentication/register.html", form = register_form)

@app.route("/register", methods = ["POST"])
def register():
    register_form = RegisterForm()

    account = Account(register_form.name.data, 
                      register_form.username.data, 
                      bcrypt.generate_password_hash(register_form.password.data))
    
    try:
        db.session().add(account)
        db.session().commit()
    except Exception:
        return render_template("authentication/register.html", form = register_form, error="Username taken")
    
    return redirect(url_for("homepage"))