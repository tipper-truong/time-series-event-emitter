from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.extensions import db
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    CORS(app)
    db.init_app(app)
    Migrate(app, db)

    # Register blueprints
    from app.api.v1.events import bp as events_bp
    app.register_blueprint(events_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app 