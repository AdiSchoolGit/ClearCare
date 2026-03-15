from flask import Flask

from app.config import Config
from app.db import mongo


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Set mongo URI

    # initialize Mongo
    mongo.init_app(app)
    return app
