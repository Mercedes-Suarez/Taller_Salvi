from flask import Blueprint, request, jsonify
from backend import db
from backend.models.repair_detailsModel import Repair_details

repair_details_bp = Blueprint('repair_details', __name__)

# Obtener todos los detalles de reparación
@repair_details_bp.route('/repair_details', methods=['GET'])
def get_repair_details():
    details = Repair_details.query.all()
    return jsonify([{
        "id_order": d.id_order,
        "description": d.description,
        "id_replacement": d.id_replacement,
        "amount": d.amount,
        "unit_price": str(d.unit_price)
    } for d in details])

# Obtener un detalle de reparación por ID de orden
@repair_details_bp.route('/repair_details/<int:id_order>', methods=['GET'])
def get_repair_detail(id_order):
    detail = Repair_details.query.get(id_order)
    if not detail:
        return jsonify({"error": "Detail not found"}), 404
    return jsonify({
        "id_order": detail.id_order,
        "description": detail.description,
        "id_replacement": detail.id_replacement,
        "amount": detail.amount,
        "unit_price": str(detail.unit_price)
    })

# Crear un nuevo detalle de reparación
@repair_details_bp.route('/repair_details', methods=['POST'])
def create_repair_detail():
    data = request.json
    new_detail = Repair_details(
        id_order=data['id_order'],
        description=data['description'],
        id_replacement=data['id_replacement'],
        amount=data['amount'],
        unit_price=data['unit_price']
    )
    db.session.add(new_detail)
    db.session.commit()
    return jsonify({"message": "Repair detail added"}), 201

# Eliminar un detalle de reparación
@repair_details_bp.route('/repair_details/<int:id_order>', methods=['DELETE'])
def delete_repair_detail(id_order):
    detail = Repair_details.query.get(id_order)
    if not detail:
        return jsonify({"error": "Detail not found"}), 404

    db.session.delete(detail)
    db.session.commit()
    return jsonify({"message": "Repair detail deleted"})