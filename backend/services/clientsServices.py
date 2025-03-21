from backend.models import db
from backend.models.clientModel import Client

def get_all_clients():
    """Obtiene todos los clientes de la base de datos."""
    return Client.query.all()

def get_client_by_id(client_id):
    """Obtiene un cliente por su ID."""
    return Client.query.get(client_id)

def create_client(data):
    """Crea un nuevo cliente en la base de datos."""
    new_client = Client(
        users_id=data['users_id'],
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        address=data['address'],
        register_date=data['register_date']
    )
    db.session.add(new_client)
    db.session.commit()
    return new_client

def update_client(client_id, data):
    """Actualiza la información de un cliente existente."""
    client = Client.query.get(client_id)
    if not client:
        return None
    
    client.name = data.get('name', client.name)
    client.phone = data.get('phone', client.phone)
    client.email = data.get('email', client.email)
    client.address = data.get('address', client.address)
    
    db.session.commit()
    return client

def delete_client(client_id):
    """Elimina un cliente de la base de datos."""
    client = Client.query.get(client_id)
    if not client:
        return None
    
    db.session.delete(client)
    db.session.commit()
    return client