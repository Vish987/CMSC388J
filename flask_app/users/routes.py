from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from ..forms import RegistrationForm, LoginForm
from ..models import User
from .. import bcrypt

users = Blueprint("users", __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('budgets.view_budgets'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email=form.email.data, password=hashed_password)
        user.save()
        return redirect(url_for("users.login"))

    return render_template("register.html", form=form)

@users.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('budgets.view_budgets'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('budgets.view_budgets'))
        else:
            flash("Login failed. Invalid credentials.", "danger")

    return render_template("login.html", form=form)

@users.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.login"))