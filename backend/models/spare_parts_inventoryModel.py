from backend import db

class Spare_parts_inventory(db.Model):
    __tablename__ = 'spare_parts_inventory'

    id_part = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)