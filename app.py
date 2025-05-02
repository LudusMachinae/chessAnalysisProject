import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)

#auto reload templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

@app.after_request
def after_request(response):
    #no cache (for now ig)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def homepage():
    print('homepage')
    return render_template('homepage.html')

@app.route("/register")
@login_required
def register():
    print('register')
    return render_template('apology.html', top='register', bottom='error 400'), 400

@app.route("/login")
def login():
    print('login')
    return render_template('apology.html', top='login', bottom='error 400'), 400

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/pwreset")
def pwreset():
    print('pwreset')
    return render_template('apology.html', top='pwreset', bottom='error 400'), 400