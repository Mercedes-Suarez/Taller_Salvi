from backend.models import db
from backend.models.paymentsModel import Payment

def get_all_payments():
    """Obtiene todos los pagos."""
    return Payment.query.all()

def get_payment_by_invoice(id_invoice):
    """Obtiene un pago por ID de factura."""
    return Payment.query.get(id_invoice)

def create_payment(data):
    """Crea un nuevo pago en la base de datos."""
    new_payment = Payment(
        id_invoice=data['id_invoice'],
        id_client=data['id_client'],
        amount=data['amount'],
        payment_method=data['payment_method'],
        payment_date=data['payment_date'],
        state=data['state']
    )
    db.session.add(new_payment)
    db.session.commit()
    return new_payment

def update_payment(id_invoice, data):
    """Actualiza la información de un pago."""
    payment = Payment.query.get(id_invoice)
    if not payment:
        return None
    
    payment.amount = data.get('amount', payment.amount)
    payment.payment_method = data.get('payment_method', payment.payment_method)
    payment.payment_date = data.get('payment_date', payment.payment_date)
    payment.state = data.get('state', payment.state)

    db.session.commit()
    return payment

def delete_payment(id_invoice):
    """Elimina un pago de la base de datos."""
    payment = Payment.query.get(id_invoice)
    if not payment:
        return None
    
    db.session.delete(payment)
    db.session.commit()
    return payment