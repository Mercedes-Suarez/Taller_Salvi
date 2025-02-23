from flask import Blueprint, request, jsonify
from backend import db
from backend.models.messagesModel import Message

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([{
        "id_message": m.id_message,
        "id_user": m.id_user,
        "name": m.name,
        "phone": m.phone,
        "email": m.email,
        "message_text": m.message_text,
        "shipping_date": m.shipping_date,
        "state": m.state,
        "response_text": m.response_text,
        "response_date": m.response_date
    } for m in messages])

@messages_bp.route('/messages', methods=['POST'])
def create_message():
    data = request.json
    new_message = Message(
        id_user=data['id_user'],
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        message_text=data['message_text'],
        shipping_date=data['shipping_date'],
        state=data['state']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Message added"}), 201

@messages_bp.route('/messages/<int:id>', methods=['PUT'])
def update_message(id):
    message = Message.query.get_or_404(id)
    data = request.json
    message.state = data.get('state', message.state)
    message.response_text = data.get('response_text', message.response_text)
    message.response_date = data.get('response_date', message.response_date)
    db.session.commit()
    return jsonify({"message": "Message updated"})

@messages_bp.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({"message": "Message deleted"})