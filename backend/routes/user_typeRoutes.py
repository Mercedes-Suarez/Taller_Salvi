from flask import Blueprint, request, jsonify
from backend import db
from backend.models.user_typeModel import UserType


# Blueprint para UserType
user_type_bp = Blueprint('user_type', __name__)

@user_type_bp.route('/user_types', methods=['GET'])
def get_user_types():
    user_types = UserType.query.all()
    return jsonify([{ "id_user_type": ut.id_user_type, "user_type_name": ut.user_type_name } for ut in user_types])

@user_type_bp.route('/user_types', methods=['POST'])
def create_user_type():
    data = request.json
    new_user_type = UserType(user_type_name=data['user_type_name'])
    db.session.add(new_user_type)
    db.session.commit()
    return jsonify({"message": "User Type added"}), 201

@user_type_bp.route('/user_types/<int:id>', methods=['PUT'])
def update_user_type(id):
    user_type = UserType.query.get(id)
    if not user_type:
        return jsonify({"error": "User Type not found"}), 404
    
    data = request.json
    user_type.user_type_name = data.get('user_type_name', user_type.user_type_name)  # Actualizar nombre
    db.session.commit()
    
    return jsonify({"message": "User Type updated successfully"})

@user_type_bp.route('/user_types/<int:id>', methods=['DELETE'])
def delete_user_type(id):
    user_type = UserType.query.get(id)
    if not user_type:
        return jsonify({"error": "User Type not found"}), 404
    
    db.session.delete(user_type)
    db.session.commit()
    
    return jsonify({"message": "User Type deleted successfully"})