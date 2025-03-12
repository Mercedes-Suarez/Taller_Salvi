from flask import Blueprint, request, jsonify
from backend.models import db
from backend.models.vehicleModel import Vehicle

vehicles_bp = Blueprint('vehicle', __name__)

@vehicles_bp.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{
        "vehicle_id": v.vehicle_id,
        "brand": v.brand,
        "model": v.model,
        "year": v.year
    } for v in vehicles])

@vehicles_bp.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.json
    new_vehicle = Vehicle(
        client_id=data['client_id'],
        brand=data['brand'],
        model=data['model'],
        year=data['year'],
        number_frame=data['number_frame']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle added"}), 201

# Actualizar un vehículo
@vehicles_bp.route('/vehicles/<int:id>', methods=['PUT'])
def update_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404

    data = request.json
    vehicle.client_id = data.get('client_id', vehicle.client_id)
    vehicle.brand = data.get('brand', vehicle.brand)
    vehicle.model = data.get('model', vehicle.model)
    vehicle.year = data.get('year', vehicle.year)
    vehicle.number_frame = data.get('number_frame', vehicle.number_frame)

    db.session.commit()
    return jsonify({"message": "Vehicle updated successfully"})

# Eliminar un vehículo
@vehicles_bp.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404

    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle deleted successfully"}) 