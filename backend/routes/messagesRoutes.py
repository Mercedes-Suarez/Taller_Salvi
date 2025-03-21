from flask import Blueprint, request, jsonify
#from backend.models import db
from backend.services.messagesServices import (
    get_all_messages, get_message_by_id, create_message,
    update_message, delete_message
)
#from backend.models.messagesModel import Message
#from datetime import datetime

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    try:
        messages = get_all_messages()
        return jsonify([
            {
                "id": m.id,
                "user_id": m.user_id,
                "name": m.name,
                "phone": m.phone,
                "email": m.email,
                "message_text": m.message_text,
                "sent_date": m.sent_date.isoformat() if m.sent_date else None,
                "status": m.status,
                "response_text": m.response_text,
                "response_date": m.response_date.isoformat() if m.response_date else None
            } for m in messages
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@messages_bp.route('/messages', methods=['POST'])
def create_message():
    try:
        data = request.json
        new_message = create_message(data)
        return jsonify({"message": "Message added", "id": new_message.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
@messages_bp.route('/messages/<int:id>', methods=['PUT'])
def update_message(id):
    try:
        data = request.json
        updated_message = update_message(id, data)
        if not updated_message:
            return jsonify({"error": "Message not found"}), 404

        return jsonify({"message": "Message updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
       
@messages_bp.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    try:
        deleted_message = delete_message(id)
        if not deleted_message:
            return jsonify({"error": "Message not found"}), 404
        
        return jsonify({"message": "Message deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500