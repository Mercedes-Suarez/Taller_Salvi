from flask import Blueprint, request, jsonify
from backend import db
from models.userModel import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "name": u.name,
        "email": u.email,
        "user_type_id": u.user_type_id,
        "registration_date": u.registration_date
    } for u in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        user_type_id=data['user_type_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added"}), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.user_type_id = data.get('user_type_id', user.user_type_id)
    db.session.commit()
    return jsonify({"message": "User updated"})

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})