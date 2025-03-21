from flask import Blueprint, request, jsonify
from backend.services.repair_detailServices import (
    get_all_repair_details, get_repair_detail_by_order_id, 
    create_repair_detail, delete_repair_detail
)
repair_detail_bp = Blueprint('repair_detail', __name__)

# Obtener todos los detalles de reparación
@repair_detail_bp.route('/repair_detail', methods=['GET'])
def get_repair_details():
    try:

        details = get_all_repair_details()
        return jsonify([{
             "order_id": d.order_id,
             "description": d.description,
             "sparePartsInventory_id": d.sparePartsInventory_id,
             "amount": d.amount,
             "unit_price": str(d.unit_price)
    } for d in details])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener un detalle de reparación por ID de orden
@repair_detail_bp.route('/repair_detail/<int:order_id>', methods=['GET'])
def get_repair_detail(order_id):

    detail = get_repair_detail_by_order_id(order_id)
    if not detail:
        return jsonify({"error": "Detail not found"}), 404
    return jsonify({
        "order_id": detail.order_id,
        "description": detail.description,
        "sparePartsInventory_id": detail.sparePartsInventory_id,
        "amount": detail.amount,
        "unit_price": str(detail.unit_price)
    })

# Crear un nuevo detalle de reparación
@repair_detail_bp.route('/repair_detail', methods=['POST'])
def create_repair_detail_route():
    try:

        data = request.json
        new_detail = create_repair_detail(data)
        return jsonify({"message": "Repair detail added", "order_id": new_detail.order_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Eliminar un detalle de reparación
@repair_detail_bp.route('/repair_detail/<int:order_id>', methods=['DELETE'])
def delete_repair_detail_route(order_id):
    try:
        deleted_detail = delete_repair_detail(order_id)
    
        if not deleted_detail:
            return jsonify({"error": "Detail not found"}), 404

        return jsonify({"message": "Repair detail deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500