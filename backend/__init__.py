from flask import Flask
from propelauth_py import init_base_auth
import os

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_pyfile('config.py', silent=True)

    # Initialize PropelAuth
    auth = init_base_auth({
        'auth_url': os.getenv('PROPELAUTH_AUTH_URL'),
        'api_key': os.getenv('PROPELAUTH_API_KEY'),
    })

    # Store auth instance in app context
    app.auth = auth

    # Import and register blueprints
    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
