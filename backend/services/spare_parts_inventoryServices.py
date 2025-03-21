from backend.models import db
from backend.models.sparePartsInventoryModel import SparePartsInventory

def get_spare_parts_all():
    """Obtiene todos los repuestos disponibles."""
    return SparePartsInventory.query.all()

def get_spare_parts_by_id(spare_part_id):
    """Obtiene un repuesto por su ID."""
    return SparePartsInventory.query.get(spare_part_id)

def create_spare_part(data):
    """Crea un nuevo repuesto en el inventario."""
    new_spare_part = SparePartsInventory(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    db.session.add(new_spare_part)
    db.session.commit()
    return new_spare_part

def update_spare_part(spare_part_id, data):
    """Actualiza un repuesto existente."""
    spare_part = SparePartsInventory.query.get(spare_part_id)
    if not spare_part:
        return None

    spare_part.name = data.get('name', spare_part.name)
    spare_part.description = data.get('description', spare_part.description)
    spare_part.price = data.get('price', spare_part.price)
    
    db.session.commit()
    return spare_part

def delete_spare_part(spare_part_id):
    """Elimina un repuesto del inventario."""
    spare_part = SparePartsInventory.query.get(spare_part_id)
    if not spare_part:
        return None

    db.session.delete(spare_part)
    db.session.commit()
    return spare_part