from flask import Blueprint, request, jsonify
from backend import db
from backend.models.vehiclesModel import Vehicles

vehicles_bp = Blueprint('vehicles', __name__)

@vehicles_bp.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicles.query.all()
    return jsonify([{
        "id_vehicle": v.id_vehicle,
        "brand": v.brand,
        "model": v.model,
        "year": v.year
    } for v in vehicles])

@vehicles_bp.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.json
    new_vehicle = Vehicles(
        id_client=data['id_client'],
        brand=data['brand'],
        model=data['model'],
        year=data['year'],
        number_frame=data['number_frame']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle added"}), 201

# Actualizar un vehículo
@vehicles_bp.route('/vehicles/<int:id_vehicle>', methods=['PUT'])
def update_vehicle(id_vehicle):
    vehicle = Vehicles.query.get(id_vehicle)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404

    data = request.json
    vehicle.id_client = data.get('id_client', vehicle.id_client)
    vehicle.brand = data.get('brand', vehicle.brand)
    vehicle.model = data.get('model', vehicle.model)
    vehicle.year = data.get('year', vehicle.year)
    vehicle.number_frame = data.get('number_frame', vehicle.number_frame)

    db.session.commit()
    return jsonify({"message": "Vehicle updated successfully"})

# Eliminar un vehículo
@vehicles_bp.route('/vehicles/<int:id_vehicle>', methods=['DELETE'])
def delete_vehicle(id_vehicle):
    vehicle = Vehicles.query.get(id_vehicle)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404

    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle deleted successfully"})