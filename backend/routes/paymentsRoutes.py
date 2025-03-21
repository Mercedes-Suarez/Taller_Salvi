from flask import Blueprint, request, jsonify
from backend.services.paymentsServices import (
    get_all_payments, get_payment_by_invoice, create_payment,
    update_payment, delete_payment
)

payments_bp = Blueprint('payments', __name__)

# Obtener todos los pagos
@payments_bp.route('/payments', methods=['GET'])
def get_payments():
    try:
        payments = get_all_payments()
        return jsonify([{
            "id_invoice": p.id_invoice,
            "id_client": p.id_client,
            "amount": str(p.amount),
            "payment_method": p.payment_method,
            "payment_date": p.payment_date.isoformat(),
            "state": p.state
        } for p in payments])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener un pago por ID de factura
@payments_bp.route('/payments/<int:id_invoice>', methods=['GET'])
def get_payment(id_invoice):
    try:
        payment = get_payment_by_invoice(id_invoice)
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Crear un nuevo pago
@payments_bp.route('/payments', methods=['POST'])
def create_new_payment():
    try:
        data = request.json
        new_payment = create_payment(data)
        return jsonify({"message": "Payment added", "id_invoice": new_payment.id_invoice}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Actualizar un pago existente
@payments_bp.route('/payments/<int:id_invoice>', methods=['PUT'])
def update_existing_payment(id_invoice):
    try:
        data = request.json
        updated_payment = update_payment(id_invoice, data)
        if not updated_payment:
            return jsonify({"error": "Payment not found"}), 404

        return jsonify({"message": "Payment updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Eliminar un pago
@payments_bp.route('/payments/<int:id_invoice>', methods=['DELETE'])
def delete_existing_payment(id_invoice):
    try:
        deleted_payment = delete_payment(id_invoice)
        if not deleted_payment:
            return jsonify({"error": "Payment not found"}), 404

        return jsonify({"message": "Payment deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500