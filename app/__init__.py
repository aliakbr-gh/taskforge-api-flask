from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from app.middleware.jwt_handlers import jwt

migrate = Migrate()
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # loading config
    from app.config import Config
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # routes would be register here
    from app.routes.home import home_bp
    from app.routes.health import health_bp
    from app.routes.auth import auth_bp
    from app.routes.task import task_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app