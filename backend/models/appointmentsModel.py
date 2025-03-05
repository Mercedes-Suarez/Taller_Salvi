from backend.models import db
from .clientModel import Client
from .vehicleModel import Vehicle

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, nullable=False)  # Se puede hacer relación con una tabla de vehículos
    appointment_date = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Enum('Pendiente', 'Confirmada', 'Cancelada', 'Realizada'), nullable=False)
    notes = db.Column(db.Text, nullable=False)