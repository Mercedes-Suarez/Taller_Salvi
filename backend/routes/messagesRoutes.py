from flask import Blueprint, request, jsonify
from backend.models import db
from backend.models.messagesModel import Message
from datetime import datetime

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    try:
        messages = Message.query.all()
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
        return jsonify({"message": "Message added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@messages_bp.route('/messages/<int:id>', methods=['PUT'])
def update_message(id):
    try:
        message = Message.query.get_or_404(id)
        data = request.json
        message.status = data.get('status', message.status)
        message.response_text = data.get('response_text', message.response_text)
        message.response_date = datetime.utcnow() if 'response_text' in data else message.response_date
        db.session.commit()
        return jsonify({"message": "Message updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@messages_bp.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    try:
        message = Message.query.get_or_404(id)
        db.session.delete(message)
        db.session.commit()
        return jsonify({"message": "Message deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500