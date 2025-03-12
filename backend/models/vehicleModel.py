from backend.models import db
from backend.models.clientModel import Client

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clients_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    number_frame = db.Column(db.String(50), nullable=False)

    # Relación con Users (Clientes)
    clients = db.relationship('Client', backref=db.backref('vehicles', lazy=True))
    appointments = db.relationship('Appointment', backref='vehicle', lazy=True)

    def __init__(self, client_id, brand, model, year, number_frame):
        self.client_id = client_id
        self.brand = brand
        self.model = model
        self.year = year
        self.number_frame = number_frame    