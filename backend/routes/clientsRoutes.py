from flask import Blueprint, request, jsonify
from backend.services.clientsServices import get_all_clients, get_client_by_id, create_client, update_client, delete_client
#from backend.models import db
#from backend.models.clientModel import Client

# Blueprint para Clients
clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = get_all_clients()
    return jsonify([{ 
        "client_id": client.client_id,
        "users_id": client.users_id,
        "name": client.name,
        "phone": client.phone,
        "email": client.email,
        "address": client.address,
        "register_date": client.register_date.isoformat()
    } for client in clients])

@clients_bp.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    """Ruta para obtener un cliente por su ID."""
    client = get_client_by_id(id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    return jsonify({ 
        "client_id": client.client_id,
        "users_id": client.users_id,
        "name": client.name,
        "phone": client.phone,
        "email": client.email,
        "address": client.address,
        "register_date": client.register_date.isoformat()
    })

@clients_bp.route('/clients', methods=['POST'])
def create_client():
    try: 

        data = request.json
        new_client = create_client(data)
        return jsonify({"message": "Client added", "client_id": new_client.client_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@clients_bp.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    client = update_client(id, request.json)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    
    return jsonify({"message": "Client updated successfully"})

@clients_bp.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = delete_client(id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    
    return jsonify({"message": "Client deleted successfully"})