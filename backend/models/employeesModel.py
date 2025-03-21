from backend.models import db
from backend.models.usersModel import User
from sqlalchemy.dialects.mysql import ENUM

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    post = db.Column(ENUM('Administrador', 'Mecánico', name="post_enum"), nullable=False)
    date_start = db.Column(db.DateTime, nullable=False)

    chat_messages = db.relationship('ChatMessage', back_populates='employee', cascade="all, delete-orphan")