from flask import Blueprint, request, jsonify
from backend import db
from models.sessionTokensModel import SessionToken
from datetime import datetime

# Blueprint para Session Tokens
session_tokens_bp = Blueprint('session_tokens', __name__)

@session_tokens_bp.route('/session_tokens', methods=['GET'])
def get_session_tokens():
    tokens = SessionToken.query.all()
    return jsonify([{ 
        "id": token.id,
        "user_id": token.user_id,
        "token": token.token,
        "creation_date": token.creation_date.isoformat(),
        "expiration_date": token.expiration_date.isoformat()
    } for token in tokens])

@session_tokens_bp.route('/session_tokens', methods=['POST'])
def create_session_token():
    try:
        data = request.json
        new_token = SessionToken(
            user_id=data['user_id'],
            token=data['token'],
            creation_date=datetime.fromisoformat(data['creation_date']) if 'creation_date' in data else datetime.utcnow(),
            expiration_date=datetime.fromisoformat(data['expiration_date'])
        )
        db.session.add(new_token)
        db.session.commit()
        return jsonify({"message": "Session Token added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@session_tokens_bp.route('/session_tokens/<int:id_user>', methods=['PUT'])
def update_session_token(id):
    token = SessionToken.query.get(id)
    if not token:
        return jsonify({"error": "Token not found"}), 404
    
    data = request.json
    token.token = data.get('token', token.token)
    token.expiration_date = datetime.fromisoformat(data['expiration_date']) if 'expiration_date' in data else token.expiration_date
    
    db.session.commit()
    return jsonify({"message": "Session Token updated successfully"})

@session_tokens_bp.route('/session_tokens/<int:id_user>', methods=['DELETE'])
def delete_session_token(id):
    token = SessionToken.query.get(id)
    if not token:
        return jsonify({"error": "Token not found"}), 404
    
    db.session.delete(token)
    db.session.commit()
    return jsonify({"message": "Session Token deleted successfully"})