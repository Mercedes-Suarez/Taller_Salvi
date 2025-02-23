from flask import Blueprint, request, jsonify
from backend import db
from backend.models.repair_ordersModel import Repair_orders

# Blueprint para Repair Orders
repair_orders_bp = Blueprint('repair_orders', __name__)

@repair_orders_bp.route('/repair_orders', methods=['GET'])
def get_repair_orders():
    orders = Repair_orders.query.all()
    return jsonify([{ 
        "id_client": order.id_client,
        "id_vehicle": order.id_vehicle,
        "start_date": order.start_date.isoformat(),
        "end_date": order.end_date.isoformat() if order.end_date else None,
        "status": order.status,
        "total": str(order.total),
        "entry_date": order.entry_date.isoformat(),
        "estimated_delivery": order.estimated_delivery.isoformat(),
        "estimated_total": str(order.estimated_total) if order.estimated_total else None,
        "finish_total": str(order.finish_total) if order.finish_total else None
    } for order in orders])

@repair_orders_bp.route('/repair_orders', methods=['POST'])
def create_repair_order():
    data = request.json
    new_order = Repair_orders(
        id_client=data['id_client'],
        id_vehicle=data['id_vehicle'],
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

@repair_orders_bp.route('/repair_orders/<int:id_client>', methods=['PUT'])
def update_repair_order(id_client):
    order = Repair_orders.query.filter_by(id_client=id_client).first()
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

@repair_orders_bp.route('/repair_orders/<int:id_client>', methods=['DELETE'])
def delete_repair_order(id_client):
    order = Repair_orders.query.filter_by(id_client=id_client).first()
    if not order:
        return jsonify({"error": "Repair Order not found"}), 404
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Repair Order deleted successfully"})