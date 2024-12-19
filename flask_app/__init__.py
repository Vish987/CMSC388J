# 3rd-party packages
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


# Initialize extensions
db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()

# Blueprints
from .users.routes import users
from .budgets.routes import budgets
from .expenses.routes import expenses

def custom_404(e):
    return render_template("404.html"), 404

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(users)
    app.register_blueprint(budgets)
    app.register_blueprint(expenses)
    app.register_error_handler(404, custom_404)

    login_manager.login_view = "users.login"

    return app