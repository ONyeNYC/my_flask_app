from flask import Flask
from .models import initialize_db

def create_app():
    app = Flask(__name__)

    # Initialize the database
    initialize_db()

    # Import routes
    from . import routes

    return app
