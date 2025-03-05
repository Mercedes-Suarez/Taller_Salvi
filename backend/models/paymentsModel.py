from backend.models import db
from sqlalchemy.orm import validates
from .invoicesModel import Invoice
from .clientModel import Client

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2))
    payment_method = db.Column(db.String(20))
    payment_date = db.Column(db.DateTime)
    state = db.Column(db.String(10))

    @validates('state')
    def validate_state(self, key, value):
        valid_states = ['Pendiente', 'Cobrado']
        if value not in valid_states:
            raise ValueError(f"Estado '{value}' no es válido. Debe ser 'Pendiente' o 'Cobrado'.")
        return value