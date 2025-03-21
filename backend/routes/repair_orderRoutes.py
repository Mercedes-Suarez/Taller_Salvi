from flask import Blueprint, request, jsonify
from backend.services.repair_orderServices import (
    get_all_repair_orders, get_repair_order_by_client_id,
    create_repair_order, update_repair_order, delete_repair_order
)
# Blueprint para Repair Orders
repair_order_bp = Blueprint('repair_order', __name__)

@repair_order_bp.route('/repair_order', methods=['GET'])
def get_repair_orders():
    try:
       orders = get_all_repair_orders()
       return jsonify([{ 
        "client_id": order.client_id,
        "vehicle_id": order.vehicle_id,
        "start_date": order.start_date.isoformat(),
        "end_date": order.end_date.isoformat() if order.end_date else None,
        "status": order.status,
        "total": str(order.total),
        "entry_date": order.entry_date.isoformat(),
        "estimated_delivery": order.estimated_delivery.isoformat(),
        "estimated_total": str(order.estimated_total) if order.estimated_total else None,
        "finish_total": str(order.finish_total) if order.finish_total else None
    } for order in orders])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Obtener una orden de reparación por ID de cliente
@repair_order_bp.route('/repair_order/<int:client_id>', methods=['GET'])
def get_repair_order(client_id):
    try:
        order = get_repair_order_by_client_id(client_id)
        if not order:
            return jsonify({"error": "Repair Order not found"}), 404
        return jsonify({
            "client_id": order.client_id,
            "vehicle_id": order.vehicle_id,
            "start_date": order.start_date.isoformat(),
            "end_date": order.end_date.isoformat() if order.end_date else None,
            "status": order.status,
            "total": str(order.total),
            "entry_date": order.entry_date.isoformat(),
            "estimated_delivery": order.estimated_delivery.isoformat(),
            "estimated_total": str(order.estimated_total) if order.estimated_total else None,
            "finish_total": str(order.finish_total) if order.finish_total else None
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@repair_order_bp.route('/repair_order', methods=['POST'])
def create_repair_order_route():
    try:
        data = request.json
        new_order = create_repair_order(data)
        return jsonify({"message": "Repair Order added", "client_id": new_order.client_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@repair_order_bp.route('/repair_order/<int:client_id>', methods=['PUT'])
def update_repair_order_route(client_id, data):
    try:
        data = request.json
        updated_order = update_repair_order(client_id, data)
        if not updated_order:
            return jsonify({"error": "Repair Order not found"}), 404

        return jsonify({"message": "Repair Order updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@repair_order_bp.route('/repair_order/<int:client_id>', methods=['DELETE'])
def delete_repair_order_route(client_id):
    try:
        deleted_order = delete_repair_order(client_id)
        if not deleted_order:
            return jsonify({"error": "Repair Order not found"}), 404

        return jsonify({"message": "Repair Order deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500