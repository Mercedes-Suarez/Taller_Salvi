from backend.models import db
from backend.models.clientModel import Client
from backend.models.vehicleModel import Vehicle

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'),nullable=False) # Se puede hacer relación con una tabla de vehículos
    appointment_date = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Enum('Pendiente', 'Confirmada', 'Cancelada', 'Realizada'), nullable=False)
    notes = db.Column(db.Text, nullable=False) 

    vehicles = db.relationship('Vehicle', backref='appointments')
