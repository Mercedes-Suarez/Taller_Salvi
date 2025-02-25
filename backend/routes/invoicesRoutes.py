from flask import Blueprint, request, jsonify
from backend import db
from backend.models.invoicesModel import Invoice

invoices_bp = Blueprint('invoices', __name__)

# Obtener todas las facturas
@invoices_bp.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify([{
        "id_invoice": i.id_invoice,
        "id_order": i.id_order,
        "id_client": i.id_client,
        "issue_date": i.issue_date.isoformat(),
        "total": str(i.total)
    } for i in invoices])

# Obtener una factura por ID
@invoices_bp.route('/invoices/<int:id_invoice>', methods=['GET'])
def get_invoice(id_invoice):
    invoice = Invoice.query.get(id_invoice)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404
    return jsonify({
        "id_invoice": invoice.id_invoice,
        "id_order": invoice.id_order,
        "id_client": invoice.id_client,
        "issue_date": invoice.issue_date.isoformat(),
        "total": str(invoice.total)
    })