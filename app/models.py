from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    subscription_level = db.Column(db.String(20), nullable=False)  # basic/premium
    account_status = db.Column(db.String(20), nullable=False)     # active/frozen

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    access_level = db.Column(db.String(20), nullable=False)       # basic/premium
    available_hours = db.Column(db.String(50), nullable=False)   # e.g., "09:00-18:00"

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attribute = db.Column(db.String(50), nullable=False)          # e.g., "subscription_level"
    operator = db.Column(db.String(10), nullable=False)          # e.g., "=="
    value = db.Column(db.String(50), nullable=False)             # e.g., "premium"
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=False)