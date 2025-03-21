from backend.models import db
from backend.models.repair_orderModel import Repair_order

def get_all_repair_orders():
    """Obtiene todas las órdenes de reparación."""
    return Repair_order.query.all()

def get_repair_order_by_client_id(client_id):
    """Obtiene una orden de reparación por el ID del cliente."""
    return Repair_order.query.filter_by(client_id=client_id).first()

def create_repair_order(data):
    """Crea una nueva orden de reparación en la base de datos."""
    new_order = Repair_order(
        client_id=data['client_id'],
        vehicle_id=data['vehicle_id'],
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        status=data['status'],
        total=data['total'],
        entry_date=data['entry_date'],
        estimated_delivery=data['estimated_delivery'],
        estimated_total=data.get('estimated_total'),
        finish_total=data.get('finish_total')
    )
    db.session.add(new_order)
    db.session.commit()
    return new_order

def update_repair_order(client_id, data):
    """Actualiza una orden de reparación existente."""
    order = Repair_order.query.filter_by(client_id=client_id).first()
    if not order:
        return None
    
    order.status = data.get('status', order.status)
    order.end_date = data.get('end_date', order.end_date)
    order.total = data.get('total', order.total)
    order.estimated_total = data.get('estimated_total', order.estimated_total)
    order.finish_total = data.get('finish_total', order.finish_total)

    db.session.commit()
    return order

def delete_repair_order(client_id):
    """Elimina una orden de reparación de la base de datos."""
    order = Repair_order.query.filter_by(client_id=client_id).first()
    if not order:
        return None
    
    db.session.delete(order)
    db.session.commit()
    return order