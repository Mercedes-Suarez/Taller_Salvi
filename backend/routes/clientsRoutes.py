from flask import Blueprint, request, jsonify
from backend import db
from backend.models.clientsModel import Client

# Blueprint para Clients
clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{ 
        "id_client": client.id_client,
        "id_user": client.id_user,
        "name": client.name,
        "phone": client.phone,
        "email": client.email,
        "address": client.address,
        "register_date": client.register_date.isoformat()
    } for client in clients])

@clients_bp.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client = Client(
        id_user=data['id_user'],
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        address=data['address'],
        register_date=data['register_date']
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({"message": "Client added"}), 201

@clients_bp.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    
    data = request.json
    client.name = data.get('name', client.name)
    client.phone = data.get('phone', client.phone)
    client.email = data.get('email', client.email)
    client.address = data.get('address', client.address)
    
    db.session.commit()
    return jsonify({"message": "Client updated successfully"})

@clients_bp.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    
    db.session.delete(client)
    db.session.commit()
    return jsonify({"message": "Client deleted successfully"})