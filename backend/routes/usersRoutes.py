from flask import Blueprint, request, jsonify
from backend.models import db
from backend.models.userModel import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "username": u.username,
        "email": u.email,
        "user_type_id": u.user_type_id,
        "registration_date": u.registration_date
    } for u in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        username=data['username'],
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
    user.username = data.get('username', user.username)
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