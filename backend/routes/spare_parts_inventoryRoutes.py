from flask import Blueprint, request, jsonify
from backend import db
from backend.models.spare_parts_inventoryModel import Spare_parts_inventory

# Blueprint para Spare Parts Inventory
spare_parts_bp = Blueprint('spare_parts', __name__)


@spare_parts_bp.route('/spare_parts', methods=['GET'])
def get_spare_parts():
    spare_parts = Spare_parts_inventory.query.all()
    return jsonify([{ 
        "id_part": sp.id_part, 
        "name": sp.name, 
        "description": sp.description, 
        "price": float(sp.price)  # Convertir Decimal a float
    } for sp in spare_parts])

@spare_parts_bp.route('/spare_parts', methods=['POST'])
def create_spare_part():
    data = request.json
    new_spare_part = Spare_parts_inventory(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    db.session.add(new_spare_part)
    db.session.commit()
    return jsonify({"message": "Spare Part added"}), 201

# Método PUT (Actualizar Spare Part)
@spare_parts_bp.route('/spare_parts/<int:id>', methods=['PUT'])
def update_spare_part(id):
    spare_part = Spare_parts_inventory.query.get(id)
    if not spare_part:
        return jsonify({"error": "Spare Part not found"}), 404
    
    data = request.json
    spare_part.name = data.get('name', spare_part.name)
    spare_part.description = data.get('description', spare_part.description)
    spare_part.price = data.get('price', spare_part.price)
    
    db.session.commit()
    
    return jsonify({"message": "Spare Part updated successfully"})

# Método DELETE (Eliminar Spare Part)
@spare_parts_bp.route('/spare_parts/<int:id>', methods=['DELETE'])
def delete_spare_part(id):
    spare_part = Spare_parts_inventory.query.get(id)
    if not spare_part:
        return jsonify({"error": "Spare Part not found"}), 404
    
    db.session.delete(spare_part)
    db.session.commit()
    
    return jsonify({"message": "Spare Part deleted successfully"})