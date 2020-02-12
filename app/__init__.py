from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # pass config
    app.config.from_object(Config)
    # register blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # initialize app to extensions
    db.init_app(app)
    return app