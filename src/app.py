# Standard Imports

# External Imports
from flask import Flask, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

# Local Imports
from .config import config
from .models import create_models
from .routes import create_routes


def create_app():
    db = SQLAlchemy()
    models = create_models(db)

    app = Flask(__name__)
    app.config.from_object(config)
    create_routes(app, db)

    bootstrap = Bootstrap5(app)
    db.init_app(app)



    return app