from flask import Blueprint, request, jsonify
from backend import db
from backend.models.paymentsModel import Payment

payments_bp = Blueprint('payments', __name__)

# Obtener todos los pagos
@payments_bp.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        "id_invoice": p.id_invoice,
        "id_client": p.id_client,
        "amount": str(p.amount),
        "payment_method": p.payment_method,
        "payment_date": p.payment_date.isoformat(),
        "state": p.state
    } for p in payments])

# Obtener un pago por ID de factura
@payments_bp.route('/payments/<int:id_invoice>', methods=['GET'])
def get_payment(id_invoice):
    payment = Payment.query.get(id_invoice)
    if not payment:
        return jsonify({"error": "Payment not found"}), 404
    return jsonify({
        "id_invoice": payment.id_invoice,
        "id_client": payment.id_client,
        "amount": str(payment.amount),
        "payment_method": payment.payment_method,
        "payment_date": payment.payment_date.isoformat(),
        "state": payment.state
    })