from flask import Flask

def create_app():
    app = Flask(__name__)

    # routes would be register here
    from app.routes.home import home_bp
    from app.routes.health import health_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(health_bp)

    return app