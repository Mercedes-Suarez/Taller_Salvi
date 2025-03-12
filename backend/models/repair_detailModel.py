from backend.models import db
#from .repair_orderModel import Repair_order
from backend.models.sparePartsInventoryModel import SparePartsInventory

class Repair_detail(db.Model):
    __tablename__ = 'repair_detail'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repair_order_id = db.Column(db.Integer, db.ForeignKey('repair_order.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sparePartsInventory_id = db.Column(db.Integer, db.ForeignKey('spare_parts_inventory.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from backend.models.repair_orderModel import Repair_order  # Importación diferida    