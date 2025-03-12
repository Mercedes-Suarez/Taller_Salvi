from backend.models import db
from sqlalchemy.orm import validates
from backend.models.invoicesModel import Invoice
from backend.models.clientModel import Client

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoices_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    clients_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2))
    payment_method = db.Column(db.Enum('Efectivo', 'Tarjeta', 'Transferencia', 'Otros'), nullable=False)
    payment_date = db.Column(db.DateTime)
    status = db.Column(db.String(10))

    @validates('status')
    def validate_state(self, key, value):
        valid_states = ['Pendiente', 'Cobrado']
        if value not in valid_states:
            raise ValueError(f"Estado '{value}' no es válido. Debe ser 'Pendiente' o 'Cobrado'.")
        return value