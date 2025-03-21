from backend.models import db
from backend.models.repair_detailModel import Repair_detail

def get_all_repair_details():
    """Obtiene todos los detalles de reparación."""
    return Repair_detail.query.all()

def get_repair_detail_by_order_id(order_id):
    """Obtiene un detalle de reparación por ID de orden."""
    return Repair_detail.query.get(order_id)

def create_repair_detail(data):
    """Crea un nuevo detalle de reparación en la base de datos."""
    new_detail = Repair_detail(
        order_id=data['order_id'],
        description=data['description'],
        sparePartsInventory_id=data['sparePartsInventory_id'],
        amount=data['amount'],
        unit_price=data['unit_price']
    )
    db.session.add(new_detail)
    db.session.commit()
    return new_detail

def delete_repair_detail(order_id):
    """Elimina un detalle de reparación de la base de datos."""
    detail = Repair_detail.query.get(order_id)
    if not detail:
        return None
    
    db.session.delete(detail)
    db.session.commit()
    return detail