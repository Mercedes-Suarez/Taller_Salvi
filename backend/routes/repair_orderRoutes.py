from flask import Blueprint, request, jsonify
from backend.models import db
from backend.models.repair_orderModel import Repair_order

# Blueprint para Repair Orders
repair_order_bp = Blueprint('repair_order', __name__)

@repair_order_bp.route('/repair_order', methods=['GET'])
def get_repair_order():
    orders = Repair_order.query.all()
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

@repair_order_bp.route('/repair_order', methods=['POST'])
def create_repair_order():
    data = request.json
    new_order = Repair_order(
        client_id=data['client_id'],
        vehicle_id=data['vehicle_id'],
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        status=data['status'],
        total=data['total'],
        entry_date=data['entry_date'],
        estimated_delivery=data['estimated_delivery'],
        estimated_total=data.get('estimated_total'),
        finish_total=data.get('finish_total')
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Repair Order added"}), 201

@repair_order_bp.route('/repair_order/<int:id_client>', methods=['PUT'])
def update_repair_order(id_client):
    order = Repair_order.query.filter_by(id_client=id_client).first()
    if not order:
        return jsonify({"error": "Repair Order not found"}), 404
    
    data = request.json
    order.status = data.get('status', order.status)
    order.end_date = data.get('end_date', order.end_date)
    order.total = data.get('total', order.total)
    order.estimated_total = data.get('estimated_total', order.estimated_total)
    order.finish_total = data.get('finish_total', order.finish_total)
    
    db.session.commit()
    return jsonify({"message": "Repair Order updated successfully"})

@repair_order_bp.route('/repair_order/<int:id_client>', methods=['DELETE'])
def delete_repair_order(id_client):
    order = Repair_order.query.filter_by(id_client=id_client).first()
    if not order:
        return jsonify({"error": "Repair Order not found"}), 404
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Repair Order deleted successfully"})