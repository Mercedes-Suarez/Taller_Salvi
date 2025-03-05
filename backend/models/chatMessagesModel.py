from backend.models import db
from .clientModel import Client
from .employeesModel import Employee
from datetime import datetime

class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    sent_date = db.Column(db.DateTime, default=lambda: datetime.utcnow(), nullable=False)
    ready = db.Column(db.Boolean, default=False, nullable=False)