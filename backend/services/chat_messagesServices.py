from backend.models import db
from backend.models.chatMessagesModel import ChatMessage
from datetime import datetime

def get_all_cmsg():

    return ChatMessage.query.all()

def get_cmsg_by_id(msg_id):
    
    return ChatMessage.query.get_or_404(msg_id)

def create_cmsg(data):
    if 'clients_id' not in data or not isinstance(data['clients_id'], int):
        raise ValueError("clients_id must be an integer")

    if 'employees_id' not in data or not isinstance(data['employees_id'], int):
        raise ValueError("employees_id must be an integer")

    if 'message_text' not in data or not isinstance(data['message_text'], str) or not data['message_text'].strip():
        raise ValueError("message_text must be a non-empty string")

    sent_date = datetime.fromisoformat(data['sent_date']) if 'sent_date' in data else datetime.utcnow()
    ready = bool(data.get('ready', False))

    new_cmsg = ChatMessage(
        clients_id = data['clients_id'],
        employees_id = data['employees_id'],
        message_text = data['message_text'],
        sent_date = sent_date,
        ready = ready

    )
    db.session.add(new_cmsg)
    db.session.commit()
    return new_cmsg

def update_cmsg(cmsg_id, data):

    cmsg = ChatMessage.query.get_or_404(cmsg_id)

    required_fields = ['clients_id', 'employees_id', 'message_text']
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f"{field} is required")
        
    if not isinstance(data['clients_id'], int):
        raise ValueError("clients_id must be an integer")

    if not isinstance(data['employees_id'], int):
        raise ValueError("employees_id must be an integer")    
    
    if not isinstance(data['message_text'], str) or not data['message_text'].strip():
        raise ValueError("message_text must be a non-empty string")
    
    if 'sent_date' in data and data['sent_date'].strip():
    
        try:
            cmsg.sent_date = datetime.fromisoformat(data['sent_date'])
        except ValueError:
            raise ValueError("sent_date must be in ISO format (YYYY-MM-DDTHH:MM:SS)")

    if 'ready' in data:
        cmsg.ready = bool(data['ready'])
    
    cmsg.clients_id = data.get('clients_id', cmsg.clients_id)
    cmsg.employees_id = data.get('employees_id', cmsg.employees_id)
    cmsg.message_text = data.get('message_text', cmsg.message_text)
   
    db.session.commit()
    return cmsg

def delete_cmsg(cmsg_id):

    cmsg = ChatMessage.query.get_or_404(cmsg_id)
    db.session.delete(cmsg)
    db.session.commit()
    return cmsg