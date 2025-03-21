from flask import Blueprint, request, jsonify
from backend.services.vehiclesServices import (
    get_all_vehicles, get_vehicle_by_id, create_vehicle as create_vehicle_service,
    update_vehicle as update_vehicle_service, delete_vehicle as delete_vehicle_service
)

vehicles_bp = Blueprint('vehicle', __name__)

@vehicles_bp.route('/vehicles', methods=['GET'])
def get_vehicles():
    try:
        vehicles = get_all_vehicles()
        return jsonify([{
           "vehicle_id": v.vehicle_id,
           "client_id": v.client_id,
           "brand": v.brand,
           "model": v.model,
           "year": v.year,
            "number_frame": v.number_frame
    } for v in vehicles])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@vehicles_bp.route('/vehicles', methods=['POST'])
def create_vehicle_route():
    try:
        data = request.json
        new_vehicle = create_vehicle_service(data)
        return jsonify({
            "message": "Vehicle created successfully",
            "vehicle_id": new_vehicle.vehicle_id
        }), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500       


# Actualizar un vehículo
@vehicles_bp.route('/vehicles/<int:id>', methods=['PUT'])
def update_vehicle_route(id):
    try:
        data = request.json
        updated_vehicle = update_vehicle_service(id, data)
        if not updated_vehicle:
            return jsonify({"error": "Vehicle not found"}), 404

        return jsonify({"message": "Vehicle updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Eliminar un vehículo
@vehicles_bp.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle_route(id):
    try:
        deleted_vehicle = delete_vehicle_service(id)
        if not deleted_vehicle:
            return jsonify({"error": "Vehicle not found"}), 404

        return jsonify({"message": "Vehicle deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500