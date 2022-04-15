from app import app, db
from flask import request, render_template, flash, redirect, url_for
from models import User
from forms import RegisterForm,LoginForm
from flask_login import current_user, login_user, logout_user, login_required



#login page, checks if there is a valid username in the DB, then checks credentials to enter homepage
@app.route("/login", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def login():
    loginform = LoginForm(csrf_enabled=False)
    if loginform.validate_on_submit():
        user = User.query.filter_by(username=loginform.username.data).first()
        if user != None:
            if user.verify_password(loginform.password.data):
                return redirect(url_for("userhome"))
            else:
                flash(f"Incorrect password!")
        else:
            flash(f"User '{loginform.username.data}' doesn't exist!")
    return render_template("login.html", loginform=loginform)

#register page in case the user needs a new account
@app.route("/register", methods=["GET", "POST"])
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        user = User(username=registerform.username.data)
        user.set_password(registerform.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", registerform=registerform)

#user homepage
@app.route("/home", methods=["GET", "POST"])
def userhome():
    return render_template("home.html")
