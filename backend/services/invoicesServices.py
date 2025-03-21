from backend.models import db
from backend.models.invoicesModel import Invoice
from datetime import datetime

def get_all_invoices():
    """Obtiene todas las facturas."""
    return Invoice.query.all()

def get_invoice_by_id(invoice_id):
    """Obtiene una factura por su ID."""
    return Invoice.query.get(invoice_id)

def create_invoice(data):
    """Crea una nueva factura en la base de datos."""
    if 'id_order' not in data or not isinstance(data['id_order'], int):
        raise ValueError("id_order must be an integer")

    if 'id_client' not in data or not isinstance(data['id_client'], int):
        raise ValueError("id_client must be an integer")

    if 'total' not in data or not isinstance(data['total'], (int, float)):
        raise ValueError("total must be a number")

    try:

        issue_date = datetime.fromisoformat(data['issue_date']) if 'issue_date' in data else datetime.utcnow()
    except ValueError:
        raise ValueError("issue_date must be in ISO format (YYYY-MM-DDTHH:MM:SS)")

    new_invoice = Invoice(
        id_order=data['id_order'],
        id_client=data['id_client'],
        issue_date=issue_date,
        total=data['total']
    )

    db.session.add(new_invoice)
    db.session.commit()
    return new_invoice

def update_invoice(invoice_id, data):
    """Actualiza una factura existente."""
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return None

    if 'id_order' in data and isinstance(data['id_order'], int):
        invoice.id_order = data['id_order']

    if 'id_client' in data and isinstance(data['id_client'], int):
        invoice.id_client = data['id_client']

    if 'issue_date' in data:
        try:
            invoice.issue_date = datetime.fromisoformat(data['issue_date'])
        except ValueError:
            raise ValueError("issue_date must be in ISO format (YYYY-MM-DDTHH:MM:SS)")

    if 'total' in data and isinstance(data['total'], (int, float)):
        invoice.total = data['total']

    db.session.commit()
    return invoice

def delete_invoice(invoice_id):
    """Elimina una factura de la base de datos."""
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return None

    db.session.delete(invoice)
    db.session.commit()
    return invoice