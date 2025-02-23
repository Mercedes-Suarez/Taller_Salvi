from backend import db
from backend.models.clientsModel import Client

class Vehicles(db.Model):
    __tablename__ = 'vehicles'

    id_vehicle = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id_client'), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    number_frame = db.Column(db.String(50), nullable=False)

    # Relación con Users (Clientes)
    client = db.relationship('Client', backref=db.backref('vehicles', lazy=True))

    def __init__(self, id_client, brand, model, year, number_frame):
        self.id_client = id_client
        self.brand = brand
        self.model = model
        self.year = year
        self.number_frame = number_frame    