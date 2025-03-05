from backend.models import db
from .repair_ordersModel import Repair_orders
from .sparePartsInventoryModel import SparePartsInventory

class Repair_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_order = db.Column(db.Integer, db.ForeignKey('repair_orders.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sparePartsInventory_id = db.Column(db.Integer, db.ForeignKey('spare_parts_inventory.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)