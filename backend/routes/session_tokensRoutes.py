from flask import Blueprint, request, jsonify
from backend import db
from backend.models.session_tokensModel import Session_tokens

# Blueprint para Session Tokens
session_tokens_bp = Blueprint('session_tokens', __name__)

@session_tokens_bp.route('/session_tokens', methods=['GET'])
def get_session_tokens():
    tokens = Session_tokens.query.all()
    return jsonify([{ 
        "id_user": token.id_user,
        "token": token.token,
        "creation_date": token.creation_date.isoformat(),
        "expiration_date": token.expiration_date.isoformat()
    } for token in tokens])

@session_tokens_bp.route('/session_tokens', methods=['POST'])
def create_session_token():
    data = request.json
    new_token = Session_tokens(
        id_user=data['id_user'],
        token=data['token'],
        creation_date=data['creation_date'],
        expiration_date=data['expiration_date']
    )
    db.session.add(new_token)
    db.session.commit()
    return jsonify({"message": "Session Token added"}), 201

@session_tokens_bp.route('/session_tokens/<int:id_user>', methods=['PUT'])
def update_session_token(id_user):
    token = Session_tokens.query.get(id_user)
    if not token:
        return jsonify({"error": "Token not found"}), 404
    
    data = request.json
    token.token = data.get('token', token.token)
    token.expiration_date = data.get('expiration_date', token.expiration_date)
    
    db.session.commit()
    return jsonify({"message": "Session Token updated successfully"})

@session_tokens_bp.route('/session_tokens/<int:id_user>', methods=['DELETE'])
def delete_session_token(id_user):
    token = Session_tokens.query.get(id_user)
    if not token:
        return jsonify({"error": "Token not found"}), 404
    
    db.session.delete(token)
    db.session.commit()
    return jsonify({"message": "Session Token deleted successfully"})