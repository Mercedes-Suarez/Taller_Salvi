from flask import Blueprint, request, jsonify
from backend.services.chat_messagesServices import get_all_cmsg, get_cmsg_by_id, create_cmsg, update_cmsg , delete_cmsg
from backend.models import db
from backend.models.chatMessagesModel import ChatMessage
from datetime import datetime

chat_messages_bp = Blueprint('chat_messages', __name__)

@chat_messages_bp.route('/chat_messages', methods=['GET'])
def get_chat_messages():
    try:
        msges = get_all_cmsg()
        return jsonify([{
                "id": cmsg.id,
                "clients_id": cmsg.clients_id,
                "employees_id": cmsg.employees_id,
                "message_text": cmsg.message_text,
                "sent_date": cmsg.sent_date.isoformat() if cmsg.sent_date else None,
                "ready": cmsg.ready
            } for cmsg in msges])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_messages_bp.route('/chat_messages/<int:id>', methods=['GET'])
def get_chat_messages_by_id(id):
    try:
        cmsg = get_cmsg_by_id(id)
        return jsonify(
            {
                "id": cmsg.id,
                "clients_id": cmsg.clients_id,
                "employees_id": cmsg.employees_id,
                "message_text": cmsg.message_text,
                "sent_date": cmsg.sent_date.isoformat() if cmsg.sent_date else None,
                "ready": cmsg.ready
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@chat_messages_bp.route('/chat_messages', methods=['POST'])
def create_chat_message():
    try:
        data = request.json
        new_cmsg = create_cmsg(data)
        return jsonify({
            "id": new_cmsg.id,
            "clients_id": new_cmsg.clients_id,
            "employees_id": new_cmsg.employees_id,
            "message_text": new_cmsg.message_text,
            "sent_date": new_cmsg.sent_date.isoformat() if new_cmsg.sent_date else None,
            "ready": new_cmsg.ready
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_messages_bp.route('/chat_messages/<int:id>', methods=['PUT'])
def update_chat_message(id):
    try:
        data = request.json
        updated_cmsg = update_cmsg(id,data)
        return jsonify({
            "id": updated_cmsg.id,
            "clients_id": updated_cmsg.clients_id,
            "employees_id": updated_cmsg.employees_id,
            "message_text": updated_cmsg.message_text,
            "sent_date": updated_cmsg.sent_date.isoformat() if updated_cmsg.sent_date else None,
            "ready": updated_cmsg.ready
        })
    except ValueError as ve:
        return jsonify({"error":str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_messages_bp.route('/chat_messages/<int:id>', methods=['DELETE'])
def delete_chat_message(id):
    try:
        delete_cmsg(id)
        return jsonify({"message": "Chat message deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500