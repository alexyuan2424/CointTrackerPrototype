# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite as the database
db = SQLAlchemy(app)

# Import routes after initializing app and db
from app.routes import *

# Create tables on startup
with app.app_context():
    db.create_all()
