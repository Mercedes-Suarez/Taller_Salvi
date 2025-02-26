from flask import Blueprint, request, jsonify
from backend import db
from backend.models.chatMessagesModel import ChatMessage
from datetime import datetime

chat_messages_bp = Blueprint('chat_messages', __name__)

@chat_messages_bp.route('/chat_messages', methods=['GET'])
def get_chat_messages():
    try:
        messages = ChatMessage.query.all()
        return jsonify([
            {
                "id": msg.id,
                "client_id": msg.client_id,
                "employee_id": msg.employee_id,
                "message_text": msg.message_text,
                "sent_date": msg.sent_date.isoformat() if msg.sent_date else None,
                "ready": msg.ready
            } for msg in messages
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_messages_bp.route('/chat_messages', methods=['POST'])
def create_chat_message():
    try:
        data = request.json
        sent_date = data.get('sent_date')  # Obtener sent_date del JSON

        if sent_date:
            sent_date = datetime.fromisoformat(sent_date)  # Convertir a datetime si está presente
        else:
            sent_date = datetime.utcnow()  # Usar la fecha y hora actual si no está en el JSON

        new_message = ChatMessage(
            client_id=data['client_id'],
            employee_id=data['employee_id'],
            message_text=data['message_text'],
            sent_date=sent_date,  # Ahora está correctamente asignado
            ready=data.get('ready', False)
        )
        db.session.add(new_message)
        db.session.commit()
        return jsonify({"message": "Chat message added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_messages_bp.route('/chat_messages/<int:id>', methods=['PUT'])
def update_chat_message(id):
    try:
        message = ChatMessage.query.get_or_404(id)
        data = request.json
        message.message_text = data.get('message_text', message.message_text)
        message.ready = data.get('ready', message.ready)
        db.session.commit()
        return jsonify({"message": "Chat message updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_messages_bp.route('/chat_messages/<int:id>', methods=['DELETE'])
def delete_chat_message(id):
    try:
        message = ChatMessage.query.get_or_404(id)
        db.session.delete(message)
        db.session.commit()
        return jsonify({"message": "Chat message deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500