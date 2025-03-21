from backend.models import db
from backend.models.vehicleModel import Vehicle

def get_all_vehicles():
    """Obtiene todos los vehículos."""
    return Vehicle.query.all()

def get_vehicle_by_id(vehicle_id):
    """Obtiene un vehículo por su ID."""
    return Vehicle.query.get(vehicle_id)

def create_vehicle(data):
    """Crea un nuevo vehículo."""
    required_fields = ["client_id", "brand", "model", "year", "number_frame"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"{field} is required")
        
    if not isinstance(data['year'], int):
        raise ValueError("year must be an integer")

    new_vehicle = Vehicle(
        client_id=data['client_id'],
        brand=data['brand'],
        model=data['model'],
        year=data['year'],
        number_frame=data['number_frame']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return new_vehicle

def update_vehicle(vehicle_id, data):
    """Actualiza la información de un vehículo."""
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return None

    if 'client_id' in data:

        vehicle.client_id = data['client_id']

    if 'brand' in data:

        vehicle.brand = data['brand']

    if 'model' in data:

        vehicle.model = data['model']

    if 'year' in data: 

        if not isinstance(data['year'], int):
            raise ValueError("year must be an integer")
        vehicle.year = data['year']
        
    if 'number_frame' in data: 

        vehicle.number_frame = data['number_frame']

    db.session.commit()
    return vehicle

def delete_vehicle(vehicle_id):
    """Elimina un vehículo."""
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return None

    db.session.delete(vehicle)
    db.session.commit()
    return vehicle