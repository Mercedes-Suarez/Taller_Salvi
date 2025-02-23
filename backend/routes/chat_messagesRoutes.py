from flask import Blueprint, request, jsonify
from backend import db
from backend.models.chat_messagesModel import chat_messages

# Blueprint para Chat Messages
chat_messages_bp = Blueprint('chat_messages', __name__)

@chat_messages_bp.route('/chat_messages', methods=['GET'])
def get_chat_messages():
    messages = chat_messages.query.all()
    return jsonify([{ 
        "id_message": msg.id_message,
        "id_client": msg.id_client,
        "id_employee": msg.id_employee,
        "message_text": msg.message_text,
        "shipping_date": msg.shipping_date.isoformat(),
        "ready": msg.ready
    } for msg in messages])

@chat_messages_bp.route('/chat_messages', methods=['POST'])
def create_chat_message():
    data = request.json
    new_message = chat_messages(
        id_client=data['id_client'],
        id_employee=data['id_employee'],
        message_text=data['message_text'],
        shipping_date=data['shipping_date'],
        ready=data['ready']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Chat Message added"}), 201

@chat_messages_bp.route('/chat_messages/<int:id>', methods=['PUT'])
def update_chat_message(id):
    message = chat_messages.query.get(id)
    if not message:
        return jsonify({"error": "Message not found"}), 404
    
    data = request.json
    message.message_text = data.get('message_text', message.message_text)
    message.ready = data.get('ready', message.ready)
    
    db.session.commit()
    return jsonify({"message": "Chat Message updated successfully"})

@chat_messages_bp.route('/chat_messages/<int:id>', methods=['DELETE'])
def delete_chat_message(id):
    message = chat_messages.query.get(id)
    if not message:
        return jsonify({"error": "Message not found"}), 404
    
    db.session.delete(message)
    db.session.commit()
    return jsonify({"message": "Chat Message deleted successfully"})