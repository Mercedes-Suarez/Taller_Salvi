from backend.models import db
from backend.models.repair_orderModel import Repair_order
from backend.models.clientModel import Client

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('repair_order.id'), nullable=False)  # Se puede hacer relación con una tabla de órdenes
    clients_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)