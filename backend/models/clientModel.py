from backend.models import db
from .userModel import User

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False)

# Relación con Users
    user_id = db.relationship('User', backref=db.backref('Client', lazy=True))