from backend import db

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id_invoice = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_order = db.Column(db.Integer, nullable=False)  # Se puede hacer relación con una tabla de órdenes
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id_client'), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)