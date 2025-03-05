from backend.models import db
from .clientModel import Client
from .vehicleModel import Vehicle

class Repair_orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.DateTime, nullable=False)  
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    status = db.Column(db.String(15), nullable=False) 
    total = db.Column(db.Numeric(10, 2), nullable=False) 
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False) 
    estimated_delivery = db.Column(db.DateTime, nullable=True)  
    estimated_total = db.Column(db.Numeric(10, 2), nullable=True) 
    finish_total = db.Column(db.Numeric(10, 2), nullable=True)
