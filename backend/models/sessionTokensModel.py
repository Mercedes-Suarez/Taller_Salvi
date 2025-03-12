from backend.models import db
from backend.models.usersModel import User
from datetime import datetime

class SessionToken(db.Model):
    __tablename__ = 'session_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(255), nullable=False, unique=True)
    creation_date = db.Column(db.DateTime, server_default=db.func.current_timestamp(), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)