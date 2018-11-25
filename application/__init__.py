from flask import Flask
from flask_sqlalchemy import SQLAlchemy

RESOURCES = "resources"

# Application
app = Flask(__name__, 
            static_folder=RESOURCES + "/static",
            template_folder=RESOURCES + "/templates")

## Configure Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}/adventurepath.db".format(RESOURCES)
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

## Views & Models
from application import views, models

## Create database
db.create_all()