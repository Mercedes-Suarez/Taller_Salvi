from ..models import db
from backend.models.clientModel import Client

class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    number_frame = db.Column(db.String(50), nullable=False)

    # Relación con Users (Clientes)
    client = db.relationship('Client', backref=db.backref('vehicles', lazy=True))

    def __init__(self, id_client, brand, model, year, number_frame):
        self.client_id = id_client
        self.brand = brand
        self.model = model
        self.year = year
        self.number_frame = number_frame    