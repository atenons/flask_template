import os
from flask import Flask
from flask_migrate import Migrate
from .database import db
from config import Config


migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)
