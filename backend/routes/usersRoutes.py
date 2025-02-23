from flask import Blueprint, request, jsonify
from backend import db
from backend.models.usersModel import Users

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([{
        "id_user": u.id_user,
        "name": u.name,
        "email": u.email,
        "user_type_id": u.user_type_id,
        "registration_date": u.registration_date
    } for u in users])

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = Users(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        user_type_id=data['user_type_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added"}), 201

@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get_or_404(id)
    data = request.json
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.user_type_id = data.get('user_type_id', user.user_type_id)
    db.session.commit()
    return jsonify({"message": "User updated"})

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})