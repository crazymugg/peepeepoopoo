# Standard Imports

# External Imports
from flask import Flask, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Local Imports
from .config import config
from .db import create_db
from .models import create_models
from .routes import create_routes


def create_app():
    db = create_db()
    models = create_models(db)

    app = Flask(__name__)
    app.config.from_object(config)
    create_routes(app, db, models)

    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(models['Team'], db.session))
    admin.add_view(ModelView(models['Game'], db.session))


    bootstrap = Bootstrap5(app)
    db.init_app(app)



    return app