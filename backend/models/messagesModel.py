from backend.models import db
from datetime import datetime
from backend.models.usersModel import User

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    sent_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.Enum('Pendiente', 'En gestión', 'Respondido', name='status_enum'), nullable=False, default='Pendiente')
    response_text = db.Column(db.Text, nullable=True)
    response_date = db.Column(db.DateTime, nullable=True)