from flask import Blueprint, request, jsonify
from backend.models import db
from backend.models.invoicesModel import Invoice
from backend.services.invoicesServices import (
    get_all_invoices, get_invoice_by_id, create_invoice as create_invoice_service,
    update_invoice as update_invoice_service, delete_invoice as delete_invoice_service
)
from datetime import datetime

invoices_bp = Blueprint('invoices', __name__)

# Obtener todas las facturas
@invoices_bp.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = get_all_invoices()
    return jsonify([{
        "id_invoice": i.id_invoice,
        "id_order": i.id_order,
        "id_client": i.id_client,
        "issue_date": i.issue_date.isoformat() if i.issue_date else None,
        "total": float(i.total) if i.total is not None else None
    } for i in invoices])

@invoices_bp.route('/invoices/<int:id>', methods=['GET'])
def get_invoice_by_id_route(id):
    invoice = get_invoice_by_id(id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404

    return jsonify({
        "id_invoice": invoice.id_invoice,
        "id_order": invoice.id_order,
        "id_client": invoice.id_client,
        "issue_date":  invoice.issue_date.isoformat() if invoice.issue_date else None,
        "total": float(invoice.total) if invoice.total is not None else None
    })

# Crear una nueva factura
@invoices_bp.route('/invoices', methods=['POST'])
def create_invoice_route():
    try:
        data = request.json
        issue_date = datetime.fromisoformat(data['issue_date']) if 'issue_date' in data else datetime.utcnow()
        data['issue_date'] = issue_date

        new_invoice = create_invoice_service(data)
        return jsonify({"message": "Invoice created successfully", "id_invoice": new_invoice.id_invoice}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Actualizar una factura
@invoices_bp.route('/invoices/<int:id>', methods=['PUT'])
def update_invoice_route(id):

    try:
        data = request.json
        updated_invoice = update_invoice_service(id, data)
        if not updated_invoice:
            return jsonify({"error": "Invoice not found"}), 404
        
        return jsonify({"message": "Invoice updated successfully"})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Eliminar una factura
@invoices_bp.route('/invoices/<int:id>', methods=['DELETE'])
def delete_invoice_route(id):
    try:
        deleted_invoice = delete_invoice_service(id)
        if not deleted_invoice:
            return jsonify({"error": "Invoice not found"}), 404
        
        return jsonify({"message": "Invoice deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500