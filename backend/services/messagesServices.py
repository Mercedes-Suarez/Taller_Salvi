from backend.models import db
from backend.models.messagesModel import Message
from datetime import datetime

def get_all_messages():
    """Obtiene todos los mensajes."""
    return Message.query.all()

def get_message_by_id(message_id):
    """Obtiene un mensaje por su ID."""
    return Message.query.get(message_id)

def create_message(data):
    """Crea un nuevo mensaje en la base de datos."""
    new_message = Message(
        user_id=data['user_id'],
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        message_text=data['message_text'],
        status=data.get('status', 'Pending')
    )
    db.session.add(new_message)
    db.session.commit()
    return new_message

def update_message(message_id, data):
    """Actualiza el estado o respuesta de un mensaje existente."""
    message = Message.query.get(message_id)
    if not message:
        return None

    message.status = data.get('status', message.status)
    message.response_text = data.get('response_text', message.response_text)
    
    if 'response_text' in data:
        message.response_date = datetime.utcnow()

    db.session.commit()
    return message

def delete_message(message_id):
    """Elimina un mensaje de la base de datos."""
    message = Message.query.get(message_id)
    if not message:
        return None

    db.session.delete(message)
    db.session.commit()
    return message