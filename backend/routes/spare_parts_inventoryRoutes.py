from flask import Blueprint, request, jsonify
from backend.services.spare_parts_inventoryServices import (
    get_spare_parts_all, get_spare_parts_by_id,
    create_spare_part, update_spare_part, delete_spare_part
)
# Blueprint para Spare Parts Inventory
spare_parts_bp = Blueprint('spare_parts', __name__)

@spare_parts_bp.route('/spare_parts', methods=['GET'])
def get_spare_parts():
    try:
        spare_parts = get_spare_parts_all()
        return jsonify([{ 
            "id": sp.id,  
            "name": sp.name, 
            "description": sp.description, 
            "price": float(sp.price)  # Convertir Decimal a float
        } for sp in spare_parts])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@spare_parts_bp.route('/spare_parts/<int:spare_part_id>', methods=['GET'])
def get_spare_part(spare_part_id):
    try:
        spare_part = get_spare_parts_by_id(spare_part_id)
        if not spare_part:
            return jsonify({"error": "Spare Part not found"}), 404

        return jsonify({
            "id": spare_part.id,
            "name": spare_part.name,
            "description": spare_part.description,
            "price": float(spare_part.price)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500    

@spare_parts_bp.route('/spare_parts', methods=['POST'])
def create_spare_part(data):
    try:
        data = request.json
        new_spare_part = create_spare_part(data)
        return jsonify({"message": "Spare Part added", "id": new_spare_part.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Método PUT (Actualizar Spare Part)
@spare_parts_bp.route('/spare_parts/<int:id>', methods=['PUT'])
def update_spare_part(spare_part_id):
    try:
        data = request.json
        updated_spare_part = update_spare_part(spare_part_id, data)
        if not updated_spare_part:
            return jsonify({"error": "Spare Part not found"}), 404

        return jsonify({"message": "Spare Part updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
# Método DELETE 
@spare_parts_bp.route('/spare_parts/<int:id>', methods=['DELETE'])
def delete_spare_part(spare_part_id):
    try:
        deleted_spare_part = delete_spare_part(spare_part_id)
        if not deleted_spare_part:
            return jsonify({"error": "Spare Part not found"}), 404

        return jsonify({"message": "Spare Part deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500