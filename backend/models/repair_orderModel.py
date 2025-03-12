from backend.models import db
from backend.models.clientModel import Client
from backend.models.vehicleModel import Vehicle

class Repair_order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clients_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    repair_detail_id = db.Column(db.Integer, db.ForeignKey('repair_detail.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)  
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('Pendiente', 'En proceso', 'Completada', 'Cancelada'), nullable=False) 
    total = db.Column(db.Numeric(10, 2), nullable=False) 
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False) 
    estimated_delivery = db.Column(db.DateTime, nullable=True)  
    estimated_total = db.Column(db.Numeric(10, 2), nullable=True) 
    finish_total = db.Column(db.Numeric(10, 2), nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from .repair_detailModel import Repair_detail  # Importación diferida