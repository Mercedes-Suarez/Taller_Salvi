from flask import Blueprint, request, jsonify
from backend.models import db
from backend.models.repair_detailModel import Repair_detail

repair_detail_bp = Blueprint('repair_detail', __name__)

# Obtener todos los detalles de reparación
@repair_detail_bp.route('/repair_detail', methods=['GET'])
def get_repair_details():
    details = Repair_detail.query.all()
    return jsonify([{
        "order_id": d.order_id,
        "description": d.description,
        "sparePartsInventory_id": d.sparePartsInventory_id,
        "amount": d.amount,
        "unit_price": str(d.unit_price)
    } for d in details])

# Obtener un detalle de reparación por ID de orden
@repair_detail_bp.route('/repair_detail/<int:id_order>', methods=['GET'])
def get_repair_detail(id_order):
    detail = Repair_detail.query.get(id_order)
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
def create_repair_detail():
    data = request.json
    new_detail = Repair_detail(
        order_id=data['order_id'],
        description=data['description'],
        sparePartsInventory_id=data['sparePartsInventory_id'],
        amount=data['amount'],
        unit_price=data['unit_price']
    )
    db.session.add(new_detail)
    db.session.commit()
    return jsonify({"message": "Repair detail added"}), 201

# Eliminar un detalle de reparación
@repair_detail_bp.route('/repair_detail/<int:id_order>', methods=['DELETE'])
def delete_repair_detail(id_order):
    detail = Repair_detail.query.get(id_order)
    if not detail:
        return jsonify({"error": "Detail not found"}), 404

    db.session.delete(detail)
    db.session.commit()
    return jsonify({"message": "Repair detail deleted"})