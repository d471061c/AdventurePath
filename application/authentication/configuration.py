from os import urandom
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from application import app
from .models import Account

app.config['SECRET_KEY'] = urandom(32)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "Please login to use this functionality"

@login_manager.user_loader
def load_account(account_id):
    return Account.query.get(account_id)