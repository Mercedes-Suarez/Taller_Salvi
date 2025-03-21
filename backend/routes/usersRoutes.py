from flask import Blueprint, request, jsonify
from backend.services.usersServices import (
    get_all_users, get_user_by_id, create_user, update_user, delete_user
)

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    try:

        users = get_all_users()
        return jsonify([{
        "id": u.id,
        "username": u.username,
        "email": u.email,
        "user_type_id": u.user_type_id,
        "registration_date": u.registration_date
    } for u in users])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = get_user_by_id(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "user_type_id": user.user_type_id,
            "registration_date": user.registration_date
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500    

@users_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        new_user = create_user(data)
        return jsonify({"message": "User added", "id": new_user.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        updated_user = update_user(user_id, data)
        if not updated_user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"message": "User updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        deleted_user = delete_user(user_id)
        if not deleted_user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"message": "User deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500